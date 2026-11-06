from zipfile import ZipFile
from pathlib import Path

# I will create the dummy files
Path("subfolder").mkdir(exist_ok=True)
Path("content1.txt").write_text("This is content 1")
Path("content2.txt").write_text("This is content 2")
Path("subfolder/content3.txt").write_text("This is content 3")
Path("subfolder/content4.txt").write_text("This is content 4")

with ZipFile("test.zip", "w") as zp:
    zp.write("content1.txt")
    zp.write("content2.txt")
    zp.write("subfolder/content3.txt")
    zp.write("subfolder/content4.txt")

with ZipFile("test.zip") as zp:
    zp.extract("content1.txt", "extract_zip")
    zp.extract("subfolder/content3.txt", "extract_zip")