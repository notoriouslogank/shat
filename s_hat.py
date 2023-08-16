"""Sorting Hat (shat)

This script allows the user to sort a large folder containing many
files of various file types into subfolders which all contain filetypes
consistent with the content of the files.

For example, once run, any files with extensions that are deemed audio 
files (.mp3, .wav, etc) will be placed into a folder called 'audio'.
Any created folders which do not ultimately contain files of its type
will be deleted.

The total count of the files moved by this script will be printed to 
the console for convenience.ls 

s_hat.py(src, dst)

"""

import glob
import os
import shutil
import sys

# CONSTANTS
SRC_PATH = str(sys.argv[1])
DST_PATH = str(sys.argv[2])

DST_MOVIES = os.path.join(DST_PATH, "movies/")
DST_PHOTOS = os.path.join(DST_PATH, "photos/")
DST_DOCUMENTS = os.path.join(DST_PATH, "documents/")
DST_AUDIO = os.path.join(DST_PATH, "audio/")
DST_APPLICATIONS = os.path.join(DST_PATH, "applications/")
DST_MISC = os.path.join(DST_PATH, "misc/")
DST_DIRS = [
    DST_MOVIES,
    DST_PHOTOS,
    DST_DOCUMENTS,
    DST_AUDIO,
    DST_APPLICATIONS,
    DST_MISC,
]

TOTAL_FILES = str(len(os.listdir(SRC_PATH)))

USE_MISC = input("Use ../misc folder? [y/N]")


# FUNCTIONS
def prep_dst():
    """Checks destination path for existence of destination folders;
    creates them if necessary.
    """
    print(" ")
    src_exist = os.path.exists(SRC_PATH)
    if src_exist == True:
        print(f"Sorting {TOTAL_FILES} files in total.")
        print("---")
        for dir in DST_DIRS:
            isExist = os.path.exists(dir)
            if isExist == True:
                pass
            else:
                os.mkdir(dir)
    else:
        print("No such path exists.")


def movies():
    """Move all files with relevant file extensions to movies
    destination folder.
    """
    dst = DST_MOVIES

    dst_count = 0
    patterns = [
        "/*.wmv",
        "/*.avi",
        "/*.mov",
        "/*.flv",
        "/*.mkv",
        "/*.mp4",
        "/*.webm",
        "/*.3gp",
    ]
    for pattern in patterns:
        files = glob.glob(SRC_PATH + pattern)

        for file in files:
            file_name = os.path.basename(file)
            shutil.move(file, dst + file_name)
            dst_count += 1
    if dst_count > 0:
        print(f"Moved {str(dst_count)} file(s) to {dst}")
    else:
        pass


def photos():
    """Move all files with relevant file extensions to photos
    destination folder.
    """
    dst = DST_PHOTOS
    dst_count = 0
    patterns = [
        "/*.jpg",
        "/*.JPG",
        "/*.jpeg",
        "/*.JPEG",
        "/*.png",
        "/*.PNG",
        "/*.gif",
        "/*.GIF",
    ]
    for pattern in patterns:
        files = glob.glob(SRC_PATH + pattern)

        for file in files:
            file_name = os.path.basename(file)
            shutil.move(file, dst + file_name)
            dst_count += 1
    if dst_count > 0:
        print("Moved " + str(dst_count) + " file(s) to " + dst)
    else:
        pass


def applications():
    """Move all files with relevant file extensions to applications
    destination folder.
    """
    dst = DST_APPLICATIONS
    dst_count = 0
    patterns = ["/*.exe", "/*.py", "/*.sh", "/*.dll", "/*.ps1", "/*.bat", "/*.msi"]
    for pattern in patterns:
        files = glob.glob(SRC_PATH + pattern)

        for file in files:
            file_name = os.path.basename(file)
            shutil.move(file, dst + file_name)
            dst_count += 1
    if dst_count > 0:
        print("Moved " + str(dst_count) + " file(s) to " + dst)
    else:
        pass


def audio():
    """Move all files with relevant file extensions to audio
    destination folder.
    """
    dst = DST_AUDIO
    dst_count = 0
    patterns = ["/*.m4a", "/*.flac", "/*.wav", "/*.mp3", "/*.wma", "/*.aac"]
    for pattern in patterns:
        files = glob.glob(SRC_PATH + pattern)

        for file in files:
            file_name = os.path.basename(file)
            shutil.move(file, dst + file_name)
            dst_count += 1
            print("Moved " + str(dst_count) + " file(s) to " + DST_AUDIO)
    if dst_count > 0:
        print("Moved " + str(dst_count) + " file(s) to " + dst)
    else:
        pass


def documents():
    """Move all files with relevant file extensions to documents
    destination folder.
    """
    dst = DST_DOCUMENTS
    dst_count = 0
    patterns = [
        "/*.txt",
        "/*.pdf",
        "/*.txt",
        "/*.doc",
        "/*.docx",
        "/*.html",
        "/*.HTML",
        "/*.xls",
    ]
    for pattern in patterns:
        files = glob.glob(SRC_PATH + pattern)

        for file in files:
            file_name = os.path.basename(file)
            shutil.move(file, dst + file_name)
            dst_count += 1
    if dst_count > 0:
        print("Moved " + str(dst_count) + " file(s) to " + dst)
    else:
        pass


def misc():
    dst_count = 0
    if USE_MISC == "y":
        dst = DST_MISC
        patterns = ["/*"]
        for pattern in patterns:
            files = glob.glob(SRC_PATH + pattern)

            for file in files:
                file_name = os.path.basename(file)
                shutil.move(file, dst + file_name)
                dst_count += 1

        print("Moved " + str(dst_count) + " file(s) to " + dst)
    else:
        remain_dir = str(len(os.listdir(SRC_PATH)))
        print(f"{remain_dir} file(s) not moved.")


def sort():
    """Sort all files in directory by file extension and move them to
    the relevant destination folder.
    """
    movies()
    photos()
    audio()
    documents()
    applications()
    misc()
    print("---")


def cleanup():
    """Check whether any destination folders for contents and delete if
    empty.
    """
    for dst in DST_DIRS:
        size_on_disk = len(os.listdir(dst))
        if size_on_disk <= 0:
            os.rmdir(dst)
        else:
            print(f"{dst} contains {str(size_on_disk)} file(s),")


def debug():
    print("SRC_PATH = " + SRC_PATH)
    print("DST_PATH = " + DST_PATH)
    print("DST_MOVIES = " + DST_MOVIES)
    print("DST_PHOTOS = " + DST_PHOTOS)
    print("DST_AUDIO = " + DST_AUDIO)
    print("DST_DOCUMENTS = " + DST_DOCUMENTS)
    print("DST_APPLICATIONS = " + DST_APPLICATIONS)
    print("DST_DIRS = " + str(DST_DIRS))
    print("TOTAL_FILES [../unsorted] = " + TOTAL_FILES)


def main():
    # debug()
    prep_dst()
    sort()
    cleanup()

if __name__ == '__main__':
    main()

# TODO: Give an option to use misc folder, delete files,
