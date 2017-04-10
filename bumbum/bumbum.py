import os
from os.path import expanduser
import sys
from PyQt5.QtCore import QUrl, QThread
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQuick import QQuickView
import youtube_dl


class App:
    """Pretty & simple video downloader"""

    def __init__(self, youtube_dl_obj):
        self.dl = youtube_dl_obj
        self.worker = None

    def download(self, url, finished_hook):
        self.worker = VideoDownloadThread(url, self.dl)
        self.worker.finished.connect(lambda: finished_hook())
        self.worker.start()

    def executable_dir(self):
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        return os.path.dirname(__file__)


class VideoDownloadThread(QThread):
    def __init__(self, url: str, dl, parent=None):
        super().__init__(parent)
        self.url = url
        self.dl = dl

    def run(self):
        self.download()

    def download(self):
        output = os.path.join(expanduser("~"), '%(title)s.%(ext)s')
        self.dl.params['outtmpl'] = output
        ie_result = self.dl.extract_info(url=self.url, download=False, process=False)
        info_dict = self.dl.process_ie_result(ie_result, download=False)
        info_dict['format'] = info_dict['formats'][-1]
        self.dl.process_info(info_dict)


if __name__ == '__main__':
    app = App(youtube_dl.YoutubeDL())
    app_gui = QGuiApplication(sys.argv)

    print('Path: {}'.format(os.path.join(app.executable_dir(), 'gui/gui.qml')))

    view = QQuickView()
    view.setTitle('BumBum')
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(
        QUrl.fromLocalFile(os.path.join(app.executable_dir(), 'gui/gui.qml'))
    )
    view.show()
    root = view.rootObject()

    download = lambda url: app.download(url, lambda: root.setStatus('Finished (look to {})'.format(expanduser("~"))))
    root.downloadVideo.connect(download)

    sys.exit(app_gui.exec_())
