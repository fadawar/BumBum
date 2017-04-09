import os
import sys
from PyQt5.QtCore import QUrl, QThread
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
import youtube_dl


class BumBum:
    """Pretty & simple video downloader"""

    def __init__(self, youtube_dl_obj):
        self.dl = youtube_dl_obj
        self.worker = None

    def download(self, url, finished_hook):
        self.worker = VideoDownloadThread(url, self.dl)
        self.worker.finished.connect(lambda: finished_hook())
        self.worker.start()


class VideoDownloadThread(QThread):
    def __init__(self, url: str, dl, parent=None):
        super().__init__(parent)
        self.url = url
        self.dl = dl

    def run(self):
        self.download()

    def download(self):
        ie_result = self.dl.extract_info(url=self.url, download=False, process=False)
        info_dict = self.dl.process_ie_result(ie_result, download=False)
        info_dict['format'] = info_dict['formats'][-1]
        self.dl.process_info(info_dict)


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)

    view = QQuickView()
    view.setTitle('BumBum')
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(
        QUrl.fromLocalFile(os.path.join(os.path.dirname(__file__), 'gui/gui.qml'))
    )
    view.show()
    root = view.rootObject()

    bum = BumBum(youtube_dl.YoutubeDL())
    download = lambda url: bum.download(url, lambda: root.setStatus('Finished'))
    root.downloadVideo.connect(download)

    sys.exit(app.exec_())
