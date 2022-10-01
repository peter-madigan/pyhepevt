class HepEvtWriter(object):
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode.lower()
        
        self._fh = None

        print(self)

    def __repr__(self):
        return f'{type(self).__name__}(filename={self.filename}, mode={self.mode})'

    def open(self):
        if self._fh is None:
            self._fh = open(self.filename, self.mode)

    def close(self):
        if self._fh is not None:
            self._fh.close()
            self._fh = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def write(self, event):
        if self._fh is None:
            raise RuntimeError('File is not open!')

        return_string = self._dump_event(event) + '\n'
        self._fh.write(return_string)

        return return_string

    def _dump_event(self, event):
        raise NotImplementedError
        

class HepEvtWriterEDepSim(HepEvtWriter):
    def _dump_event(self, event):
        """
        Saves to the custom EDepSim HepEvt format
        """
        return event.dump_edepsim()

    
class HepEvtWriterMARLEY(HepEvtWriter):
    def _dump_event(self, event):
        """
        Saves to the custom MARLEY HepEvt
        """
        return event.dump_marley()
