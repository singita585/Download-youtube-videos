from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

link = input("Enter the YouTube video URL: ")
Download(link)
#
#

#
#
#
# https://youtu.be/fJGkdRl8dVE?si=oxYgOhmKGVv3uYIP
#
#
#
#
#
#
#
#
#

#
#
# https://www.youtube.com/live/WvJ69wtAI-g?si=bCS_S0TtV0-CPtoz
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#https://www.youtube.com/watch?v=qSwxmpU6t80&list=TLPQMTUwNjIwMjO03ny-rZzaNA&index=45
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#