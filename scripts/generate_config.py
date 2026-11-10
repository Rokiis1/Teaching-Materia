from pathlib import Path
import sys

import yaml


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT

def resolve_navigation(value, nav_dir: Path, active=None) -> list:
    if active is None:
        active = set()

    if isinstance(value, list):
        navigation = []

        for item in value:
            navigation.extend(
                resolve_navigation(item, nav_dir, active)
            )

        return navigation

    if isinstance(value, dict):
        if "$include" in value:
            if len(value) != 1:
                raise ValueError(
                    "$include must be the only key in its mapping"
                )

            filename = value["$include"]

            if not isinstance(filename, str):
                raise TypeError(
                    "$include must contain a file path"
                )

            root = nav_dir.resolve()
            include_path = (nav_dir / filename).resolve()

            if not include_path.is_relative_to(root):
                raise ValueError(
                    f"Include outside navigation directory: {filename}"
                )

            if include_path in active:
                raise ValueError(
                    f"Circular navigation include: {filename}"
                )

            if not include_path.is_file():
                raise FileNotFoundError(
                    f"Navigation include not found: {include_path}"
                )

            with include_path.open("r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or []

            if not isinstance(data, list):
                raise ValueError(
                    f"Included navigation must be a list: {include_path}"
                )

            return resolve_navigation(
                data,
                nav_dir,
                active | {include_path},
            )

        if len(value) != 1:
            raise ValueError(
                "Navigation dictionaries must contain exactly one key"
            )

        key, nested_value = next(iter(value.items()))

        return [
            {
                key: resolve_navigation(
                    nested_value,
                    nav_dir,
                    active,
                )
            }
        ]

    if isinstance(value, str):
        return [value]

    raise TypeError(
        f"Unsupported navigation value: {type(value).__name__}"
    )

def load_navigation(nav_dir: Path) -> list:
    navigation = []
    domains_dir = nav_dir / "domains"

    if domains_dir.is_dir():
        for nav_file in sorted(domains_dir.glob("*.yml")):
            with nav_file.open("r", encoding="utf-8") as file:
                data = yaml.safe_load(file) or []

            if not isinstance(data, list):
                raise ValueError(
                    f"Navigation must be a list: {nav_file}"
                )

            navigation.extend(
                resolve_navigation(
                    data,
                    nav_dir,
                    {nav_file.resolve()},
                )
            )

    for nav_file in sorted(nav_dir.glob("*.yml")):
        with nav_file.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or []

        if not isinstance(data, list):
            raise ValueError(
                f"Navigation must be a list: {nav_file}"
            )

        navigation.extend(
            resolve_navigation(
                data,
                nav_dir,
                {nav_file.resolve()},
            )
        )

    return navigation


def toml_string(value: str) -> str:
    escaped = (
        value
        .replace("\\", "\\\\")
        .replace('"', '\\"')
    )

    return f'"{escaped}"'


def toml_value(value, indent=0) -> str:
    space = " " * indent

    if isinstance(value, str):
        return toml_string(value)

    if isinstance(value, list):
        if not value:
            return "[]"

        lines = ["["]

        for item in value:
            lines.append(
                f"{space} {toml_value(item, indent + 2)},"
            )

        lines.append(f"{space}]")
        return "\n".join(lines)

    if isinstance(value, dict):
        if len(value) != 1:
            raise ValueError(
                "Navigation dictionaries must contain exactly one key"
            )

        key, nested_value = next(iter(value.items()))

        return (
            "{ "
            f"{toml_string(str(key))} = "
            f"{toml_value(nested_value, indent)}"
            " }"
        )

    raise TypeError(
        f"Unsupported navigation value: {type(value).__name__}"
    )


def generate(language: str) -> Path:
    source_config = ROOT / f"zensical.{language}.toml"
    nav_dir = ROOT / "config" / "nav" / language

    if not source_config.exists():
        raise FileNotFoundError(
            f"Config file not found: {source_config}"
        )

    if not nav_dir.exists():
        raise FileNotFoundError(
            f"Navigation directory not found: {nav_dir}"
        )

    navigation = load_navigation(nav_dir)

    if not navigation:
        raise ValueError(
            f"No navigation entries found in: {nav_dir}"
        )

    config = source_config.read_text(encoding="utf-8")

    nav_toml = f"nav = {toml_value(navigation)}"

    marker = "# Navigation is generated from config/nav/"

    if marker not in config:
        raise ValueError(
            f'Missing navigation marker in "{source_config.name}".'
        )

    config = config.replace(
        marker,
        nav_toml,
        1,
    )

    output = OUTPUT_DIR / f"zensical.{language}.generated.toml"
    output.write_text(config, encoding="utf-8")

    return output


def main():
    languages = sys.argv[1:] or ["en", "lt"]

    for language in languages:
        output = generate(language)
        print(f"Generated: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
