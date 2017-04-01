import youtube_dl


class BumBum:
    """Pretty & simple video downloader"""

    def __init__(self, youtube_dl_library):
        self.dl = youtube_dl_library

    def download(self, url):
        ie_result = self.dl.extract_info(url=url, download=False, process=False)
        info_dict = self.dl.process_ie_result(ie_result, download=False)
        info_dict['format'] = info_dict['formats'][-1]
        self.dl.process_info(info_dict)

if __name__ == '__main__':
    bum = BumBum(youtube_dl.YoutubeDL())
    bum.download('https://www.youtube.com/watch?v=liW-kWFiXtQ')
