from pyhepevt import HepEvtReaderMARLEY, HepEvtReaderEDepSim

marley_test_file = 'test/test.marley.hepevt'
edepsim_test_file = 'test/test.edepsim.hepevt'

def test_reader_marley():
    with HepEvtReaderMARLEY(marley_test_file) as r:
        for e in r:
            print(e)

def test_reader_edepsim():
    with HepEvtReaderEDepSim(edepsim_test_file) as r:
        for e in r:
            print(e)            
