# Personal Tutor System

A three-part study system built around your 84 revision pack files. No accounts, no servers — everything runs locally.

---

## What's in this folder

| File | What it does |
|---|---|
| `study_app.html` | Interactive study app — open in browser |
| `study_data.js` | Parsed revision pack data (loaded by the app) |
| `study_data.json` | Same data in JSON format (for other tools) |
| `extract_study_data.py` | Rebuilds the data files from your revision packs |
| `TUTOR_PROMPT.md` | Copy-paste prompt for live Cursor tutoring sessions |

---

## Quick start

### 1. Open the study app

```bash
open study_app.html
```

Or double-click `study_app.html` in Finder. It opens in your default browser. No internet required (KaTeX CDN enhances formula display when online, but the app works fully offline).

### 2. Start a Cursor tutoring session

Open `TUTOR_PROMPT.md`, copy the prompt, paste it into a new Cursor chat along with today's topic filename. The AI acts as a Socratic tutor that drills you on the topic.

---

## Study app — feature guide

### Today tab (default view)

Shows your study plan for the current date:
- **Scheduled Today** — topics whose filename date matches today
- **Due for Review** — topics flagged by the spaced repetition tracker
- **Missed Topics** — past-dated topics you haven't started yet

Click any topic card to open its detail view.

### Dashboard tab

All 84 topics grouped by module (ST2187, ST3188, EC2020, ST3189, ST2134). Filter by module using the pills at the top.

Each topic card shows:
- Status dot (grey = not started, yellow = in progress, green = completed)
- Available modes (Flashcards, Quiz, Feynman)
- Your confidence rating if you've set one

Click a topic to see its full content and start a study mode.

### Topic detail view

Shows all sections from the revision pack (Feynman Explanation, High-Yield Core, Formula Bank, Worked Example, Timed Test, Model Answer Structure, Common Traps).

Action buttons at the top:
- **Flashcards** — drill formulas
- **Quiz** — timed exam questions
- **Feynman** — fill-in-the-blank on key concepts
- **Mark In Progress / Mark Completed** — update status
- **Confidence 1-5** — rate how well you know this topic

### Flashcards tab

Formula drill using flip cards from the Formula Bank (Section 2).

- Click the card or press **Space** to flip
- **Arrow keys** to move between cards
- Front shows the concept name, back shows the formula
- After the last card, rate your confidence and mark the topic as studied

### Quiz tab

Timed exam practice using questions from the Timed Test (Section 4).

1. Select a topic from the dropdown
2. Click **Start Timer** — it counts up (turns yellow at 50% of allocated time, red at 75%)
3. Type your answer in the text box
4. Click **Show Model Answer** to reveal the model answer structure and common traps
5. Click **Next Question** to continue

### Feynman tab

Tests whether you can recall key concepts from the Feynman Explanation (Section 0).

- Bold terms from the explanation are replaced with blank input fields
- Type what you think each term is
- Click **Check Answers** — correct answers turn green, incorrect turn red with the right answer shown
- Your score is displayed as a percentage

### Reviews tab

Spaced repetition tracker using expanding intervals: 1 day, 3 days, 7 days, 21 days.

- **Due Today** — topics that need review now (click Study or Mark Reviewed)
- **Upcoming** — future review dates
- Topics enter the review cycle when you mark them as completed

### Error Log tab

Record mistakes to review before exams.

1. Select the module
2. Type the topic name
3. Describe what you got wrong
4. Write the correction
5. Click **Add to Error Log**

Entries are sorted by date (newest first). Review this log in the final 3 days before each exam — it replaces all other study.

---

## Keyboard shortcuts

| Key | Action |
|---|---|
| Space / Enter | Flip flashcard |
| Left arrow | Previous flashcard |
| Right arrow | Next flashcard |
| Escape | Go back to previous view |

---

## Updating the data

If you edit or add revision pack files, regenerate the data:

```bash
cd ~/Desktop/exam_revision_2026/tutor_system
python3 extract_study_data.py
```

Then refresh the browser (Cmd+R).

---

## Your data

All progress (topic status, confidence ratings, review dates, error log) is stored in your browser's localStorage under the key `examRevision2026`. It persists across sessions.

To back up your progress, click **Export Progress** at the bottom of the Dashboard tab. This downloads a JSON file you can keep.

To reset everything, open browser DevTools (Cmd+Option+I), go to the Console tab, and run:

```javascript
localStorage.removeItem('examRevision2026')
```

---

## Daily workflow

| Time | Action |
|---|---|
| 6:30am (5 min) | Open app → Flashcards tab → pick yesterday's topic → drill formulas |
| Commute | Listen to NotebookLM audio overview for today's topic |
| 6:30pm | Open app → Today tab → click today's topic → read sections |
| 6:50pm | Flashcards → Quiz → review model answer |
| 7:15pm | Dinner break |
| 7:45pm | Quiz mode under timed conditions |
| 8:30pm | Check model answer → log errors → read Common Traps |
| 8:50pm | Mark topic as completed → rate confidence → check Reviews tab |
| Weekend | Open Cursor → paste TUTOR_PROMPT.md → do a full Socratic session |
