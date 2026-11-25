import os
import shutil

# What this file does, in plain words:
# The horoscope itself lives in entry.txt, written before the run.
# This program only copies that file into the folder the grader
# names with MAKEFUN_OUTPUT_DIR, creating the folder first if
# it does not exist yet. It renders nothing and changes no text,
# so the judged file is exactly the text in entry.txt.
out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile("entry.txt", os.path.join(out_dir, "entry.txt"))
