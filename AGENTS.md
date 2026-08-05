# Coding Skill Tree — Instructions for Codex

## Project goal

This repository tracks Giuseppe's one-year journey to become strong and
confident in technical coding assessments, especially for AI engineering,
data engineering, consulting and technology roles.

The project is both:

1. a structured learning system;
2. a measurable progress tracker;
3. a public technical portfolio.

## How to work in this repository

Before creating or reviewing exercises, read:

- `README.md`
- `PLAYER.md`
- `SKILL_TREE.md`
- `LESSONS_LEARNED.md`
- `mistakes/mistakes.md`
- the most recent weekly review
- the most recent monthly report, when available

Use those files as the source of truth for Giuseppe's current level,
strengths, weaknesses, solved patterns and recurring mistakes.

## Weekly training rules

Each weekly quest should contain:

- 4 progressive Python exercises;
- all 4 exercises in a single Jupyter notebook;
- realistic coding-assessment style problems;
- at least 1 recently learned or new pattern;
- recommended time for each exercise;
- difficulty and skills trained;
- examples and expected outputs;
- no solution or implementation hints unless explicitly requested.

Exercises should not be trivial or repetitive.

Prefer realistic patterns from:

- technical interviews;
- CodeSignal-style assessments;
- data manipulation tasks;
- AI and data engineering scenarios;
- backend and analytics problems.

## Adaptive difficulty

Adjust the following week's difficulty using:

- correctness;
- completion time;
- edge cases missed;
- implementation efficiency;
- code clarity;
- ability to recognize the underlying pattern;
- recurring mistakes.

Increase difficulty gradually when a pattern is mastered.

When a pattern is weak, propose a different exercise that trains the same
concept rather than repeating the identical problem.

## Reviews

When reviewing a solution, evaluate:

1. correctness;
2. complexity;
3. readability;
4. edge-case handling;
5. pattern recognition;
6. time management.

Do not rewrite the complete solution immediately.

First identify:

- what is correct;
- the first important issue;
- a useful question or minimal hint.

Provide the complete solution only when Giuseppe explicitly asks for it.

During reviews, Codex is responsible for designing and running additional
edge-case and performance tests. Do not require Giuseppe to invent personal
tests unless he explicitly asks to train that skill.

## Progress tracking

After each completed weekly quest, update:

- `SKILL_TREE.md`
- `LESSONS_LEARNED.md`
- `mistakes/mistakes.md`
- the week's `review.md`
- XP and progress logs
- the progressive LaTeX handbook in `dispensa/`, when the week introduced a
  new algorithm or exposed an implementation that did not satisfy the stated
  complexity constraints

Never award mastery based on one successful exercise.

A pattern is considered mastered only after it is solved independently,
correctly and within the target time on multiple occasions.

## Progressive LaTeX handbook

The repository maintains a single cumulative, offline handbook built from
`dispensa/main.tex`. Add the chapter for a week only after its solutions have
been reviewed; the handbook must never reveal hints or solutions before the
quest is complete.

Create or update `dispensa/chapters/week_XXX.tex` when at least one of these
conditions holds:

- a new algorithm or reusable pattern was encountered in the assessment;
- the submitted implementation was functionally correct but inefficient;
- the implementation failed correctness, scale or resource constraints in a
  way that yields a reusable algorithmic lesson.

Each chapter must use professional, technically precise Italian and include,
where applicable:

1. problem model, assumptions and notation;
2. the initial approach and the exact reason it is inadequate;
3. the efficient algorithm and its invariant;
4. a concise correctness argument;
5. time and space complexity;
6. edge cases and pattern-recognition cues;
7. visually distinct code boxes for the inadequate and corrected
   implementations.

Preserve Giuseppe's submitted code in the red comparison box except for
clearly marked omissions made only for presentation. Never overwrite the
submission in the notebook. Use the green box for the reviewed reference
implementation. Distinguish a logically incorrect program from one that is
correct on outputs but non-compliant with scale constraints.

After a meaningful handbook update, compile the PDF, render every page to
images and inspect the result for clipping, overflow and readability. The
canonical generated artifact is `output/pdf/dispensa_algoritmi.pdf`.

## Assessment strategy

Reinforce these rules:

- scan all exercises before committing;
- secure easy points first;
- timebox blocked problems;
- prefer a correct simple solution before optimizing;
- run the visible tests; Codex will add edge-case and performance tests during
  review;
- do not spend excessive time because a solution feels “almost finished”.

## Repository hygiene

- Keep durable context in Markdown files.
- Do not rely on previous chat history being available.
- Do not overwrite Giuseppe's submitted solutions.
- Keep each weekly quest in one notebook to make the training flow easy to
  follow.
- Keep exercises and reviews in their corresponding weekly folder.
- Use clear commit messages.
