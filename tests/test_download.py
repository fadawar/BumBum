from unittest import mock
from unittest.mock import Mock
from bumbum.bumbum import App, VideoDownloadThread


def test_uses_youtube_dl():
    lib = Mock()
    lib.process_ie_result.return_value = {'formats': ['first format']}
    lib.params = {}
    vid = VideoDownloadThread('https://www.youtube.com/watch?v=liW-kWFiXtQ', lib)

    vid.download()

    assert lib.process_info.called


@mock.patch('bumbum.bumbum.os')
def test_find_correct_path_to_application(mock_os):
    mock_os.path.dirname.return_value = 'test_path'
    app = App(youtube_dl_obj=None)

    assert app.executable_dir() == 'test_path'


@mock.patch('bumbum.bumbum.sys')
@mock.patch('bumbum.bumbum.os')
def test_find_correct_path_to_application_in_frozen(mock_os, mock_sys):
    mock_os.path.dirname.return_value = 'test_path_frozen'
    mock_sys.frozen = True
    mock_sys.executable = 'test_executable'
    app = App(youtube_dl_obj=None)

    assert app.executable_dir() == 'test_path_frozen'
    mock_os.path.dirname.assert_called_with('test_executable')
