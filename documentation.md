# Documentation - Automated File Organizer

## 1. Objective

Build a Python utility that reduces manual effort spent organizing
messy folders by automatically sorting files into category folders
based on file type.

## 2. How It Works (Logic Flow)

1. The user provides a target folder path as a command-line argument.
2. The script lists every item directly inside that folder (it does
   not go into sub-folders, to avoid re-organizing already-sorted
   files).
3. For each file, it reads the file extension (e.g. `.jpg`, `.pdf`).
4. The extension is looked up in the `FILE_CATEGORIES` dictionary to
   determine which category it belongs to (Images, Documents, Videos,
   Audio, Archives, Scripts). Anything unrecognized goes to `Others`.
5. A folder for that category is created (if it doesn't already
   exist) and the file is moved into it.
6. If a file with the same name already exists at the destination,
   the script automatically renames the incoming file (e.g.
   `report(1).pdf`) instead of overwriting it.
7. Every action is written both to the screen and to a `.log` file
   with a timestamp, for an auditable record of what happened.

## 3. Key Design Decisions

- **Dry-run mode** was added so users can safely preview the result
  before committing to real file moves — important when working with
  important personal files.
- **Top-level only scanning** prevents the script from repeatedly
  re-organizing files it has already sorted on previous runs.
- **Extension mapping as a dictionary** makes the tool easy to extend
  — adding a new category or extension is a one-line change.

## 4. Possible Future Improvements

- Add a GUI (e.g. using Tkinter) for non-technical users
- Add a `--undo` feature that reverses the last run using the log file
- Add scheduling (e.g. with `schedule` library) to run automatically
  every day/week
- Support organizing by file creation date in addition to type

## 5. Testing Performed

The script was tested with a sample folder containing one file of
each type (`.jpg`, `.png`, `.pdf`, `.txt`, `.mp3`, `.mp4`, `.zip`,
`.py`, and one file with no extension). All files were correctly
sorted into their respective category folders, and the no-extension
file was correctly skipped and reported in the summary count.
