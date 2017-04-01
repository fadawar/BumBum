from unittest.mock import Mock
from bumbum.bumbum import BumBum


def test_uses_youtube_dl():
    lib = Mock()
    lib.process_ie_result.return_value = {'formats': ['first format']}
    bum = BumBum(lib)

    bum.download('https://www.youtube.com/watch?v=liW-kWFiXtQ')

    assert lib.process_info.called
