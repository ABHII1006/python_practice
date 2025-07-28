#
# import os
# import shutil
#
# SOURCE_DIR = r"C:\Users\Admin\Downloads"
#
# FILE_TYPES = {
#     "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
#     "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
#     "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
#     "Audio": [".mp3", ".wav", ".aac", ".flac"],
#     "Videos": [".mp4", ".avi", ".mov", ".mkv"],
#     "Executables": [".exe", ".msi"],
#     "Scripts": [".py", ".js", ".sh", ".bat"]
# }
# DEST_DIR = os.path.join(SOURCE_DIR, "OrganizedCopies")
#
# def organize_and_copy_files(source_dir, dest_dir):
#     for file in os.listdir(source_dir):
#         source_file_path = os.path.join(source_dir, file)
#
#         # Skip folders
#         if os.path.isdir(source_file_path):
#             continue
#
#         _, ext = os.path.splitext(file)
#         ext = ext.lower()
#
#         copied = False
#         for folder, extensions in FILE_TYPES.items():
#             if ext in extensions:
#                 target_folder = os.path.join(dest_dir, folder)
#                 os.makedirs(target_folder, exist_ok=True)
#                 shutil.copy2(source_file_path, os.path.join(target_folder, file))
#                 # print(f"Copied: {file} → {folder}/")
#                 copied = True
#                 break
#
#         if not copied:
#             other_folder = os.path.join(dest_dir, "Others")
#             os.makedirs(other_folder, exist_ok=True)
#             shutil.copy2(source_file_path, os.path.join(other_folder, file))
#             # print(f"Copied: {file} → Others/")


# organize_and_copy_files(SOURCE_DIR, DEST_DIR)


import schedule
import time

# def job():
#     organize_and_copy_files(SOURCE_DIR, DEST_DIR)
#     print("Running automation task")
#
# schedule.every().day.at("18:00").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)

def job() :
    print("running a task")


# schedule.every(10).seconds.do(job)

# schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()
