import os
import requests
import subprocess

# URL of the image to be downloaded
image_url = "https://www.linuxlookup.com/sites/default/files/pages/distro/debian.jpg"

# Create the directory if it does not exist
directory = "/home/islamux/Download/imagesDownloaded"
if not os.path.exists(directory):
    os.makedirs(directory)

# Download the image file
response = requests.get(image_url)

# Open a file to save the image
filename = os.path.join(directory, "debian.jpg")
with open(filename, "wb") as f:
    # Write the image data to the file
    f.write(response.content)

# Open the directory in the default file manager
subprocess.run(["xdg-open", directory])

