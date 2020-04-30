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

    assert vids['y5BvucpirC4'] == 'Night Jazz: Exquisite Night Jazz Playlist - Sensual Piano Jazz & Lights of Night Home for Relax'
    assert vids['v78CVaYXRAM'] == 'My Home Jazz: Relaxing Jazz Radio & Sweet Bossa Nova for Relaxing at Home'
    assert vids['9YI_edrgrU0'] == 'Study Cafe: Concentrate Study & Work Jazz & Bossa Nova Music for Brain Power'
    assert vids['63YyvJrOLrc'] == 'Chill Piano: Beautiful Piano Music - Relaxing Music, Study Music, Stress Relief, Sleep Music'
    assert vids['7AS6PRs-oy8'] == 'Nature Guitar: Easy Listening Music - Beautiful Background Guitar Music for Work, Study'
    assert vids['wz8YYFBsMHk'] == 'Hawaiian Cafe: Relaxing Tropical Music - Hawaiian Ukulele Instrumental Music at Home'


def test_different_tab_position(mocker):
    '''
    The 'Videos' tab is diffrent from default position (index 2, not 1).
    '''
    _set_test_data('tests/testdata/test_cracked.json', mocker)
    req = HttpRequest()
    source = vparser.get_source_json(req,'dummy_channel_id')
    vids = vparser.extract_video_ids(source)
    assert vids['y5BvucpirC4'] == 'Night Jazz: Exquisite Night Jazz Playlist - Sensual Piano Jazz & Lights of Night Home for Relax'
    assert vids['v78CVaYXRAM'] == 'My Home Jazz: Relaxing Jazz Radio & Sweet Bossa Nova for Relaxing at Home'
    assert vids['9YI_edrgrU0'] == 'Study Cafe: Concentrate Study & Work Jazz & Bossa Nova Music for Brain Power'
    assert vids['63YyvJrOLrc'] == 'Chill Piano: Beautiful Piano Music - Relaxing Music, Study Music, Stress Relief, Sleep Music'
    assert vids['7AS6PRs-oy8'] == 'Nature Guitar: Easy Listening Music - Beautiful Background Guitar Music for Work, Study'
    assert vids['wz8YYFBsMHk'] == 'Hawaiian Cafe: Relaxing Tropical Music - Hawaiian Ukulele Instrumental Music at Home'
