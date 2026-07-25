# ExcuseEngine

*A randomizer for people who are not entirely sure they want a truly honest randomizer.*

You know that moment. Should you watch a movie you don't really feel like watching? Should you have one more slice of cake at midnight? (YES! YES! YES!!!)

Deep down you already know the answer. But sometimes you need a gentle push — or a credible excuse. That's what **ExcuseEngine** is for.

You set the probability with a slider (or type it directly), press the button, and get your answer: **Yes** or **No**. Green means go. Red means "well, you asked for it."

Built with Python and customtkinter. Looks clean, works offline, and speaks 14 languages.

## What it looks like

- **Probability slider** — 0% to 100%, step by 1, with `0%` / `100%` labels
- **Numeric input** — type the percentage and hit Enter or ✓
- **Yes / No result** — green "Yes", red "No", inside a rounded frame with a colored border
- **Edge cases** — 0% always says "No" (you knew it), 100% always says "Yes" (you wanted it)
- **14 languages** — auto-detected from your system locale, with a dropdown to switch manually
- **Dice icon** — a tilted die in the title bar, because randomness deserves a mascot

## Supported languages

RU, EN, ES, PT, DE, FR, IT, PL, TR, AR, HI, JA, ZH, KO

## Running from source

```bash
# Create and activate venv
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux / macOS

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

## Building a standalone .exe

```bash
pip install pyinstaller
python -m PyInstaller --onefile --windowed --icon=icons/icon_dice.ico --add-data "icons/icon_dice.ico;icons" --name "ExcuseEngine" main.py
```

The executable will be in `dist/`.

## Project structure

```
excuse-engine/
├── main.py           # Application source
├── requirements.txt  # Python dependencies
├── .gitignore
├── README.md
├── README.ru.md      # Russian version
└── icons/
    └── icon_dice.ico # App icon
```

## When to use

| Situation | Recommended setting |
|---|---|
| "Should I watch that thing I bookmarked 3 years ago?" | 30% |
| "One more cookie before bed?" | 85% |
| "Is today the day I finally start exercising?" | 10% |
| "Should I reply to that email right now?" | 50% |
| "Am I really going to learn Japanese this year?" | 7% |

*(Settings were not scientifically tested. Results may vary. The cake is always a yes.)*

## License

MIT — do whatever you want. The randomizer won't judge you. Probably.