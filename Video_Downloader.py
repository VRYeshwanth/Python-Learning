from pytube import YouTube
url_list = []
n = int(input("How many videos : "))
for i in range(n):
    url_list.append(input(f"Enter the url of video {i+1} : "))

for url in url_list:
    yt = YouTube(url)
    try:
        yd = yt.streams.get_highest_resolution()
        yd.download(r"C:\Users\yeshw\Downloads")
        print(f"{url} downloaded successfully")
    except:
        print(f"We had an error downloading {url}")
