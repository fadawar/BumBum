from unittest.mock import Mock
from bumbum.bumbum import VideoDownloadThread


def test_uses_youtube_dl():
    lib = Mock()
    lib.process_ie_result.return_value = {'formats': ['first format']}
    vid = VideoDownloadThread('https://www.youtube.com/watch?v=liW-kWFiXtQ', lib)

    vid.download()

    assert lib.process_info.called
