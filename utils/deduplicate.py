"""
Used to remove duplicate images from a directory full of duplicates by hashing their contents and renaming the file
to that hash
"""
from hashlib import sha1
from os import listdir, rename

IMAGE_DIR = "images/raw"


def get_hash(file_buffer):
    """
    Returns the hex digest of the given file
    """
    data = file_buffer.read()
    hasher = sha1()
    hasher.update(data)
    return hasher.hexdigest()


# Get all the images that exist inside the given dir
image_files = [f for f in listdir(IMAGE_DIR)]
total_images = len(image_files)
print("Found {0} files in {1}".format(total_images, IMAGE_DIR))

# Hash them each to remove duplicates (by renaming them)
num_checked = 0
for file_name in image_files:
    if num_checked % 100 == 0:
        print("Checked {0:.2f}%".format(100 * num_checked / total_images))

    full_path = "{0}/{1}".format(IMAGE_DIR, file_name)
    with open(full_path, 'rb') as infile:
        file_hash = get_hash(infile)
        rename(full_path, "{0}/{1}".format(IMAGE_DIR, file_hash))

    num_checked += 1

print("Checked 100%")
