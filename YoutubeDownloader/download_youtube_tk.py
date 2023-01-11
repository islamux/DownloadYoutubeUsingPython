import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import youtube_dl

def download():
    # Get the video URL and save location
    url = url_entry.get()
    save_location = filedialog.asksaveasfilename(defaultextension='.mp4')

    # Set options for the video download
    options = {
        'format': 'best',
        'outtmpl': save_location
    }

    # Download the video
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])

# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a Label for the URL entry
url_label = ttk.Label(root, text="Enter the video URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

# Create an Entry widget for the URL
url_entry = ttk.Entry(root)
url_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

# Create a button to download the video
download_button = ttk.Button(root, text="Download", command=download)
download_button.grid(row=1, column=1, padx=5, pady=5)

root.mainloop()

