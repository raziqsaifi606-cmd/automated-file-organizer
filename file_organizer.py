"""
=====================================================================
 PROJECT       : Automated File Organizer
 INTERN ID     : CITS4010
 INTERN NAME   : Raziq Saifi
 DURATION      : 4 Weeks
 DESCRIPTION   : A command-line Python tool that automatically scans
                 a target folder (e.g. Downloads/Desktop) and sorts
                 every file into category sub-folders based on its
                 file extension (Images, Documents, Videos, Audio,
                 Archives, Scripts, Others).
=====================================================================
"""

import os
import shutil
import argparse
import logging
from datetime import datetime

# ---------------------------------------------------------------
# 1. CONFIGURATION
# ---------------------------------------------------------------
# Mapping of category name -> list of file extensions that belong to it.
# Add/remove extensions here to customise the organizer.
FILE_CATEGORIES = {
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos":    [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Audio":     [".mp3", ".wav", ".aac", ".flac"],
    "Archives":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts":   [".py", ".js", ".html", ".css", ".java", ".cpp", ".c"],
}
OTHERS_FOLDER = "Others"   # fallback category for unrecognised extensions


def setup_logger(log_path):
    """Configure logging so every move is recorded to a log file AND
    printed on screen at the same time."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[
            logging.FileHandler(log_path, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )


def get_category(file_extension):
    """Return the category folder name for a given file extension."""
    file_extension = file_extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return OTHERS_FOLDER


def organize_folder(target_path, dry_run=False):
    """
    Walk through every file in `target_path` (top level only) and move
    it into a category sub-folder.

    Parameters
    ----------
    target_path : str   -> folder that should be organized
    dry_run     : bool  -> if True, only PRINT what would happen,
                            no files are actually moved (safe preview mode)
    """
    if not os.path.isdir(target_path):
        logging.error("The path '%s' does not exist or is not a folder.", target_path)
        return

    moved_count = 0
    skipped_count = 0

    # os.listdir gives us only the immediate contents of the folder
    for entry in os.listdir(target_path):
        full_path = os.path.join(target_path, entry)

        # Skip sub-folders - we only organize files, not existing folders
        if os.path.isdir(full_path):
            continue

        # Skip the script's own log file if it lives inside the same folder
        if entry.endswith(".log"):
            continue

        _, extension = os.path.splitext(entry)
        if extension == "":
            skipped_count += 1
            continue

        category = get_category(extension)
        category_path = os.path.join(target_path, category)

        if not dry_run:
            os.makedirs(category_path, exist_ok=True)
            destination = os.path.join(category_path, entry)

            # Avoid overwriting a file that already exists in destination
            destination = _resolve_duplicate(destination)
            shutil.move(full_path, destination)

        logging.info(
            "%s '%s'  ->  %s/",
            "[DRY-RUN] Would move" if dry_run else "Moved",
            entry,
            category
        )
        moved_count += 1

    logging.info("-" * 50)
    logging.info("Finished. Files processed: %d | Skipped (no extension): %d",
                  moved_count, skipped_count)


def _resolve_duplicate(destination):
    """If a file with the same name already exists at the destination,
    append a number (1), (2)... so nothing gets overwritten."""
    if not os.path.exists(destination):
        return destination

    base, ext = os.path.splitext(destination)
    counter = 1
    new_destination = f"{base}({counter}){ext}"
    while os.path.exists(new_destination):
        counter += 1
        new_destination = f"{base}({counter}){ext}"
    return new_destination


def main():
    parser = argparse.ArgumentParser(
        description="Automated File Organizer - sorts files into category folders."
    )
    parser.add_argument(
        "path",
        help="Path of the folder you want to organize (e.g. C:/Users/You/Downloads)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would happen WITHOUT actually moving any files."
    )
    args = parser.parse_args()

    log_file = os.path.join(args.path, f"organizer_log_{datetime.now():%Y%m%d_%H%M%S}.log")
    setup_logger(log_file)

    logging.info("Starting Automated File Organizer on: %s", args.path)
    organize_folder(args.path, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
