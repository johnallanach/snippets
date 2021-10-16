from pytube import YouTube
    

def main():
    video_url = input('Enter YouTube video URL: ')
    
    yt = YouTube(video_url)
    download_path = 'downloads'
    yt.streams.filter(adaptive=True, 
        only_audio=True).first().download(download_path)


if __name__ == '__main__':
    main()
