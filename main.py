import os
from os import scandir, rename
from os.path import splitext, exists, join, expanduser
from shutil import move
from time import sleep

import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


source_dir = r"C:\Users\USERNAME\Downloads"  # Change USERNAME to set your root directory path
dest_folder_music = r"C:\Users\USERNAME\Music"  # Set destination directory path for music
dest_folder_img = r"C:\Users\USERNAME\Pictures"  # Set destination directory path for pictures
dest_folder_video = r"C:\Users\USERNAME\Videos"  # Set destination directory path for videos
dest_folder_docs = r"C:\Users\Documents"  # Set destination directory path for documents
dest_folder_books = r"C:\Users\USERNAME\Downloads\Downloaded books"  # Destination directory and file extentions
# may vary on your needs. For example, I hardcoded the path for my kindle downloads to go to Downloaded books

# supported image types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", 
                    ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", 
                    ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# supported Video types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# supported Audio types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# supported Document types
document_extensions = [".doc", ".docx", ".odt", 
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".psd", ".msi"]
books_extensions = [".epub"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        rename(old_name, new_name)
    move(entry, dest)


class MoveFiles(FileSystemEventHandler):
    """THIS FUNCTION WILL RUN WHENEVER THERE IS A CHANGE IN 'source_dir'
    .upper is for not missing out on files with uppercase extensions"""
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                if any(name.endswith(ext) or name.endswith(ext.upper()) for ext in audio_extensions):
                    self.check_audio_files(entry, name)
                elif any(name.endswith(ext) or name.endswith(ext.upper()) for ext in video_extensions):
                    self.check_video_files(entry, name)
                elif any(name.endswith(ext) or name.endswith(ext.upper()) for ext in image_extensions):
                    self.check_image_files(entry, name)
                elif any(name.endswith(ext) or name.endswith(ext.upper()) for ext in document_extensions):
                    self.check_document_files(entry, name)
                elif any(name.endswith(ext) or name.endswith(ext.upper()) for ext in books_extensions):
                    self.check_book_files(entry, name)

    def check_audio_files(self, entry, name):  # Checks for Audio Files in Downloads folder
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                move_file(dest_folder_music, entry, name)
                logging.info(f"Moved audio file: {name}")

    def check_video_files(self, entry, name):  # Checks for Video Files in Downloads folder
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_folder_video, entry, name)
                logging.info(f"Moved video file: {name}")

    def check_image_files(self, entry, name):  # Checks for Image Files in Downloads folder
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_folder_img, entry, name)
                logging.info(f"Moved image file: {name}")

    def check_document_files(self, entry, name):  # Checks for Document Files in Downloads folder
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_folder_docs, entry, name)
                logging.info(f"Moved document file: {name}")

    def check_book_files(self, entry, name):  # Checks for ebooks in Downloads folder
        for books_extension in books_extensions:
            if name.endswith(books_extension) or name.endswith(books_extension.upper()):
                move_file(dest_folder_books, entry, name)
                logging.info(f"Moved ebook file: {name}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Get the user's home directory
    home_dir = expanduser("~")

    # Set the Downloads folder path
    downloads_folder = join(home_dir, "Downloads")

    # Set up the observer to monitor the Downloads folder
    event_handler = MoveFiles()
    observer = Observer()
    observer.schedule(event_handler, downloads_folder, recursive=True)

    # Start the observer
    observer.start()

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    # Wait for the observer to finish
    observer.join()
