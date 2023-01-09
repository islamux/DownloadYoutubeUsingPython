import sys                           
  1 from pytube import YouTube
  2  
  3 # Get the YouTube video URL from the 
  4 video_url: str  = sys.argv[1]
  5  
  6 # Create a YouTube object
  7 yt: YouTube  = YouTube(video_url)
  8  
  9 # Get a list of available video strea
 10 video_streams: List[Stream]  = yt.str
 11  
 12 # Print the available video streams
 13 print("Available video streams:")
 14 for i, stream in enumerate(video_stre
 15     print(f"{i+1}: {stream.resolution
 16  
 17 # Get the user's selection for the vi
 18 selection: int  = int(input("Enter th
 19  
 20 # Select the video stream with the de
 21 video_stream: Stream  = video_streams
 22  
 23 # Download the video stream and save 
 24 video_stream.download(filename=yt.title)
 25  
