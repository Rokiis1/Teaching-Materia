
const QUIZ_STORAGE_PREFIX = "knowledge-check:";
const QUIZ_EXPIRATION_MS = 5 * 60 * 1000;

function shuffle(array) {
  const items = [...array];

  for (let i = items.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [items[i], items[j]] = [items[j], items[i]];
  }

  return items;
}

function getQuizStorageKey(containerIndex) {
  return `${QUIZ_STORAGE_PREFIX}${location.pathname}:${containerIndex}`;
}

function loadQuizState(key) {
  try {
    const raw = localStorage.getItem(key);

    if (!raw) return null;

    const state = JSON.parse(raw);

    if (
      !state ||
      typeof state.expiresAt !== "number" ||
      Date.now() >= state.expiresAt
    ) {
      localStorage.removeItem(key);
      return null;
    }

    return state;
  } catch (error) {
    console.warn("Could not load quiz state:", error);
    return null;
  }
}

function saveQuizState(key, state) {
  try {
    localStorage.setItem(key, JSON.stringify(state));
  } catch (error) {
    console.warn("Could not save quiz state:", error);
  }
}

function initializeQuizzes() {
  document.querySelectorAll(".knowledge-check").forEach((container, containerIndex) => {
    if (container.dataset.initialized === "true") return;

    const questions = Array.from(
      container.querySelectorAll(":scope > .knowledge-question")
    );

    if (questions.length === 0) return;

    const key = getQuizStorageKey(containerIndex);
    const savedState = loadQuizState(key);

    // Use original question positions as stable identifiers
    questions.forEach((question, index) => {
      question.dataset.quizId = String(index);
    });

    const questionOrder = savedState?.questionOrder?.length === questions.length
      ? savedState.questionOrder
      : shuffle(questions.map((question) => question.dataset.quizId));

    const state = savedState || {
      expiresAt: Date.now() + QUIZ_EXPIRATION_MS,
      questionOrder,
      answers: {},
      selections: {},
    };

    // Restore or create question order
    questionOrder.forEach((id) => {
      const question = questions.find(
        (item) => item.dataset.quizId === id
      );

      if (question) container.appendChild(question);
    });

    questions.forEach((question) => {
      const questionId = question.dataset.quizId;
      const originalCorrect = question.dataset.answer;
      const explanation = question.dataset.explanation || "";
      const feedback = question.querySelector(".quiz-feedback");
      const optionsContainer = question.querySelector(".quiz-options");

      if (!feedback || !optionsContainer) return;

      const buttons = Array.from(
        optionsContainer.querySelectorAll("button[data-option]")
      );

      if (buttons.length !== 4) return;

      const correctButton = buttons.find(
        (button) => button.dataset.option === originalCorrect
      );

      if (!correctButton) return;

      // Original data-option values identify answer content
      const buttonById = new Map(
        buttons.map((button) => [button.dataset.option, button])
      );

      const savedOrder = state.answers[questionId];
      const answerOrder = Array.isArray(savedOrder) && savedOrder.length === 4
        ? savedOrder
        : shuffle(buttons.map((button) => button.dataset.option));

      const letters = ["A", "B", "C", "D"];
      const orderedButtons = answerOrder
        .map((id) => buttonById.get(id))
        .filter(Boolean);

      orderedButtons.forEach((button, index) => {
        // Keep the original answer identity separate from its displayed letter
        const originalId = answerOrder[index];
        const answerText = button.textContent
          .trim()
          .replace(/^[A-D]\.\s*/, "");

        button.dataset.answerId = originalId;
        button.dataset.option = letters[index];
        button.textContent = `${letters[index]}. ${answerText}`;

        optionsContainer.appendChild(button);
      });

      state.answers[questionId] = answerOrder;

      const correctLetter = correctButton.dataset.option;

      function showSelection(selectedButton) {
        const isCorrect = selectedButton === correctButton;

        orderedButtons.forEach((button) => {
          button.disabled = true;

          if (button === correctButton) {
            button.classList.add("quiz-correct");
          } else if (button === selectedButton) {
            button.classList.add("quiz-incorrect");
          }
        });

        feedback.textContent = isCorrect
          ? `Correct! ${explanation}`
          : `Incorrect. The correct answer is ${correctLetter}. ${explanation}`;
      }

      orderedButtons.forEach((button) => {
        button.addEventListener("click", () => {
          if (state.selections[questionId]) return;

          // Save original answer identity, not shuffled letter
          state.selections[questionId] = button.dataset.answerId;

          saveQuizState(key, state);
          showSelection(button);
        });
      });

      // Restore a previous selection after refresh
      const selectedId = state.selections[questionId];

      if (selectedId) {
        const selectedButton = orderedButtons.find(
          (button) => button.dataset.answerId === selectedId
        );

        if (selectedButton) showSelection(selectedButton);
      }
    });

    container.dataset.initialized = "true";
    saveQuizState(key, state);
  });
}

// Initial page load
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initializeQuizzes);
} else {
  initializeQuizzes();
}

// Zensical instant navigation
if (typeof document$ !== "undefined") {
  document$.subscribe(initializeQuizzes);
}

