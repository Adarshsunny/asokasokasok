import os
import glob

# Path to the directory
dir_path = r'd:\\porfolio\\portfolio'

# Find all WhatsApp images
whatsapp_images = glob.glob(os.path.join(dir_path, 'WhatsApp Image*.jpeg'))

# Sort them to have a deterministic order
whatsapp_images.sort()

# Rename them starting from gallery-5.jpg
start_index = 5
for img_path in whatsapp_images:
    new_name = f'gallery-{start_index}.jpg'
    new_path = os.path.join(dir_path, new_name)
    os.rename(img_path, new_path)
    start_index += 1

print(f"Renamed {len(whatsapp_images)} images up to gallery-{start_index-1}.jpg")
