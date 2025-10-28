# NameChallenge

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)
![Last Commit](https://img.shields.io/github/last-commit/hrosicka/NameChallenge?logo=git&color=orange)
![Name Genius](https://img.shields.io/badge/Name%20Genius-100%25-brightgreen?style=flat-square&logo=star&logoColor=yellow)
![License](https://img.shields.io/github/license/hrosicka/NameChallenge?color=informational)

A small interactive desktop game that challenges the user to guess the gender associated with a given first name. The application is written in Python and uses a GUI based on Tkinter. It queries the free Genderize.io API to guess the likely gender for a name. ️‍♀️ ️‍♂️

---

## Features

- Simple GUI game that displays a name and asks the user to guess the gender (male/female).
- Uses the Genderize.io API to determine the likely gender for a given name.
- Keeps basic success statistics (correct / total guesses).
- Ability to load custom name lists from a file (one name per line).
- Logic separated into `name_challenge_logic.py` (game logic) and `main.py` (GUI).

---

## Requirements

- Python 3.7+ (tested with 3.8+)
- The `requests` library
- `tkinter` (usually included with standard Python on Windows/macOS/Linux desktops)

---

## Screenshots

**New name screen**

![New name screen](https://raw.githubusercontent.com/hrosicka/NameChallenge/master/doc/new_name.png)

**Load names from file**

![Load file dialog](https://raw.githubusercontent.com/hrosicka/NameChallenge/master/doc/load_file.png)

**Choose a file to load names**

![Choose file](https://raw.githubusercontent.com/hrosicka/NameChallenge/master/doc/choose_file.png)

**Check answer / result**

![Check name result](https://raw.githubusercontent.com/hrosicka/NameChallenge/master/doc/check_name.png)

---

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/hrosicka/NameChallenge.git
   cd NameChallenge
   ```

2. Run the GUI:
   ```
   python main.py
   ```

3. In the GUI:
   - Click "New name" (or equivalent button) to get a new random name.
   - Select male/female and click "Check" to verify your guess.
   - Use the "Load file" / "Choose file" button to load a custom list of names (one per line).

Notes:
- Default example names are included inside `name_challenge_logic.py`. To use your own names, prepare a simple text file (one name per line) and load it via the GUI.

---

## Limitations and notes

- Genderize.io is a free public API with rate limits and no guaranteed coverage for all names. It returns probabilistic results, and some names may be ambiguous.
- No API key is required for basic usage, but heavy use may hit rate limits.
- The application currently does not store statistics persistently or handle offline operation.
- The gender detection is based on name frequency data and might fail for uncommon names or cross-cultural usage.

---

## Project structure

- `main.py` — Tkinter GUI
- `name_challenge_logic.py` — game logic, Genderize.io calls, and name management
- `doc/` — screenshots and documentation images

---

## Author
Lovingly crafted by [Hanka Robovska](https://github.com/hrosicka)

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details. Free to use, modify, and distribute as needed.
