import youtube_dl # Youtube_dl is used for download the video

ydl_opt = {"outtmpl" : "/videos/%(title)s.%(ext)s", "format": "mp4"} # Here we give some advanced settings. outtmpl is used to define the path of the video that we are going to download

def operation(link):
    """
    Start the download operation
    """
    try:
        with youtube_dl.YoutubeDL(ydl_opt) as yd: # The method YoutubeDL() take one argument which is a dictionary for changing default settings
            video = yd.download([link]) # Start the download
        print("Your video has been downloaded !")
    except Exception:
        print("Sorry, we got an error.")

#operation("https://www.youtube.com/watch?v=3YqPKLZF_WU&ab_channel=Coldplay")

"""link = input("Give the URL to the video : ")
operation(link)"""