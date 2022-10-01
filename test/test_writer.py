from pyhepevt import HepEvtWriterMARLEY, HepEvtReaderMARLEY, HepEvtWriterEDepSim

marley_test_file = 'test/test.marley.hepevt'

def test_write_marley():
    with HepEvtReaderMARLEY(marley_test_file) as reader:
        with HepEvtWriterMARLEY(marley_test_file + '.marley.hepevt', 'w') as writer:
            for ev in reader:
                writer.write(ev)

def test_write_edepsim():
    with HepEvtReaderMARLEY(marley_test_file) as reader:
        with HepEvtWriterEDepSim(marley_test_file + '.edepsim.hepevt', 'w') as writer:
            for ev in reader:
                writer.write(ev)                
