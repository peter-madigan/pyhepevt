from pyhepevt import HepEvtReaderMARLEY

marley_test_file = 'test/test_marley.hepevt'

def test_reader_marley():
    with HepEvtReaderMARLEY(marley_test_file) as r:
        for e in r:
            print(e)
