import vparser
from httpreq import HttpRequest

def _open_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()

def _set_test_data(filepath, mocker):
    _text = _open_file(filepath)
    response_mock = mocker.Mock()
    response_mock.status_code = 200
    response_mock.text = _text
    mocker.patch('requests.Session.get').return_value = response_mock

def test_json(mocker):
    '''
    The 'video' tab is at default positon (index 1).
    '''
    _set_test_data('tests/testdata/test.json', mocker)
    req = HttpRequest()
    source = vparser.get_source_json(req,'dummy_channel_id')
    vids = vparser.extract_video_ids(source)
    assert vids[0] == 'y5BvucpirC4'
    assert vids[1] == 'v78CVaYXRAM'
    assert vids[2] == '9YI_edrgrU0'
    assert vids[3] == '63YyvJrOLrc'
    assert vids[4] == '7AS6PRs-oy8'
    assert vids[5] == 'wz8YYFBsMHk'

def test_different_tab_position(mocker):
    '''
    The 'Videos' tab is diffrent from default position (index 2, not 1).
    '''
    _set_test_data('tests/testdata/test_cracked.json', mocker)
    req = HttpRequest()
    source = vparser.get_source_json(req,'dummy_channel_id')
    vids = vparser.extract_video_ids(source)
    assert vids[0] == 'y5BvucpirC4'
    assert vids[1] == 'v78CVaYXRAM'
    assert vids[2] == '9YI_edrgrU0'
    assert vids[3] == '63YyvJrOLrc'
    assert vids[4] == '7AS6PRs-oy8'
    assert vids[5] == 'wz8YYFBsMHk'
