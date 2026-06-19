# Automated File Organizer

**Intern ID:** CITS4010
**Intern Name:** Raziq Saifi
**Internship Duration:** 4 Weeks
**Project Name:** Automated File Organizer
**Domain:** Python Programming

## Project Scope

Manually sorting a cluttered folder (like Downloads or Desktop) into
categories is repetitive and time-consuming. This project automates
that process: it scans a target folder and automatically moves every
file into a category sub-folder — Images, Documents, Videos, Audio,
Archives, Scripts, or Others — based on its file extension. It
includes a safe **dry-run mode** to preview changes before anything
is moved, duplicate-name handling so files are never overwritten, and
a log file recording every action taken.

## Features

- Automatically classifies files into 7 categories by extension
- `--dry-run` flag to preview the organization without moving files
- Automatic duplicate handling (renames instead of overwriting)
- Generates a timestamped `.log` file of every action performed
- Easily customizable category/extension mapping in the code
- Works on any OS (Windows/Mac/Linux) since it uses only Python's
  built-in `os` and `shutil` modules

## Tech Stack

- Python 3
- Built-in modules: `os`, `shutil`, `argparse`, `logging`, `datetime`

## Folder Structure

```
01_Automated_File_Organizer/
├── file_organizer.py        # main script
├── README.md                 # this file
├── documentation.md          # detailed documentation
└── screenshots/
    └── before_after_run.png  # sample run output
```

## How to Run

```bash
# Preview what would happen (no files are moved)
python3 file_organizer.py "C:/Users/You/Downloads" --dry-run

# Actually organize the folder
python3 file_organizer.py "C:/Users/You/Downloads"
```

## Sample Output

See `screenshots/before_after_run.png` for a sample run showing the
terminal log and the resulting folder structure.

## Deliverables Included

- [x] Source Code (`file_organizer.py`)
- [x] README File
- [x] Screenshots / Output Images
- [x] Documentation (`documentation.md`)

## Author

**Raziq Saifi** | Intern ID: CITS4010 | Python Programming Internship
