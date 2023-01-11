import sys
from pytube import YouTube

# Get the YouTube video URL from the command line argument
video_url = sys.argv[1]

# Create a YouTube object
yt = YouTube(video_url)

# Get a list of available video streams
video_streams = yt.streams.filter(type="video").all()

# Print the available video streams
print("Available video streams:")
for i, stream in enumerate(video_streams):
    print(f"{i+1}: {stream.resolution}")

# Get the user's selection for the video stream
selection = int(input("Enter the number of the desired video stream: "))

# Select the video stream with the desired resolution
video_stream = video_streams[selection-1]

# Download the video stream and save it to the current directory
video_stream.download(filename=yt.title)

