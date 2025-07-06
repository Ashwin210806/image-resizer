import os
from PIL import Image

folder = "sample"        # Your image folder name
new_size = (500, 500)    # New size: (width, height)


if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Created folder '{folder}' - Please add your images there!")
    print("Then run the script again.")
    exit()


image_files = [f for f in os.listdir(folder) if f.endswith(('.jpg', '.png', '.jpeg'))]
if not image_files:
    print(f"No images found in '{folder}' folder!")
    print("Please add some JPG or PNG images and run again.")
    exit()

for filename in image_files:
   
    img = Image.open(folder + "/" + filename)
    
    
    img = img.resize(new_size)
    
    
    img.save(folder + "/small_" + filename)
    
    print("Done:", filename)

print("All images resized!")