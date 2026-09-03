import os
import shutil
import subprocess
import threading
import time
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


WATCH_PATHS = [
    Path("docs"),
    Path("config/nav"),
    Path("zensical.en.toml"),
    Path("zensical.lt.toml"),
]

BUILD_COMMANDS = [
    ["uv", "run", "zensical", "build", "-f", "zensical.en.generated.toml"],
    ["uv", "run", "zensical", "build", "-f", "zensical.lt.generated.toml"],
]


def copy_shared_assets():
    for language in ["en", "lt"]:
        assets_dir = Path(f"docs/{language}/assets")
        stylesheets_dir = Path(f"docs/{language}/stylesheets")

        assets_dir.mkdir(parents=True, exist_ok=True)
        stylesheets_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy2(
            "docs/shared/assets/techin-brand.svg",
            assets_dir / "techin-brand.svg",
        )

        shutil.copy2(
            "docs/shared/stylesheets/extra.css",
            stylesheets_dir / "extra.css",
        )

def build():
    print("\nCopying shared assets")
    copy_shared_assets()

    print("\nGenerating navigation configs")
    subprocess.run(
        ["uv", "run", "python", "scripts/generate_config.py"],
        check=True,
    )

    print("\nBuilding English version")
    subprocess.run(BUILD_COMMANDS[0], check=True)

    print("Building Lithuanian version")
    subprocess.run(BUILD_COMMANDS[1], check=True)

    print("Build complete\n")


def get_modified_times():
    files = {}

    for path in WATCH_PATHS:
        if path.is_file():
            files[path] = path.stat().st_mtime

        elif path.is_dir():
            for root, _, filenames in os.walk(path):
                for filename in filenames:
                    file_path = Path(root) / filename

                    if file_path.suffix in {
                        ".md",
                        ".css",
                        ".js",
                        ".svg",
                        ".png",
                        ".gif",
                        ".webp",
                        ".toml",
                        ".yml",
                        ".yaml",
                    }:
                        files[file_path] = file_path.stat().st_mtime

    return files


def watch():
    previous = get_modified_times()

    while True:
        time.sleep(0.5)

        current = get_modified_times()

        if current != previous:
            print("Change detected. Rebuilding")

            try:
                build()
            except subprocess.CalledProcessError:
                print("Build failed. Waiting for next change")

            previous = current


def serve():
    handler = partial(
        SimpleHTTPRequestHandler,
        directory="site",
    )

    server = ThreadingHTTPServer(
        ("127.0.0.1", 8000),
        handler,
    )

    print("Serving Learning Materials at http://127.0.0.1:8000")
    print("English: http://127.0.0.1:8000/en/")
    print("Lithuanian: http://127.0.0.1:8000/lt/")
    print("Watching for changes\n")

    server.serve_forever()


if __name__ == "__main__":
    build()

    watcher = threading.Thread(
        target=watch,
        daemon=True,
    )

    watcher.start()

    serve()