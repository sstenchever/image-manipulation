""" This script will process image files in "./images", rotate them 90 degrees anti-clockwise, 
resize them to 128x128, convert them to JPEG, and save them to "./finished_images" directory  
"""

from PIL import Image
import os

# Stores list of paths to images to be changed
unedited_files = []

for root, dirs, files in os.walk('./images'):
    for name in files:
        # Don't process this one
        if name == '.DS_Store':
            continue
        else:
            unedited_files.append('./images/'+ name)

for filename in unedited_files:
    with Image.open(filename).convert('RGB') as im:
        # Rotate the image 90 degrees anti-clockwise and resize to 128x128
        new_im = im.rotate(270).resize((128,128))
        # Save the image to the new file location and change it to JPEG
        new_im.save('./finished_images/'+filename[9:], "JPEG")