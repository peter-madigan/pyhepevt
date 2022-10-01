from .particle import HepEvtParticle
from .event import HepEvtEvent

class HepEvtReader(object):
    ''' Base class for implementing HepEvt file reading '''
    def __init__(self, filename):
        self.filename = filename
        
        self._fh = None

        print(self)

    def __repr__(self):
        return f'{type(self).__name__}(filename={self.filename})'

    def open(self):
        if self._fh is None:
            self._fh = open(self.filename, 'r')

    def close(self):
        if self._fh is not None:
            self._fh.close()
            self._fh = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def __iter__(self):
        return self

    def __next__(self):
        if self._fh is None:
            raise RuntimeError('File is not open!')

        event = self._read_next(self._fh)
        if event is None:
            raise StopIteration
        return event

    def _read_next(self, fh):
        return None

class HepEvtReaderMARLEY(HepEvtReader):
    def _read_next(self, fh):
        event = None
        for line in self._fh:
            event_data = line.strip(' ').split(' ')
            if len(event_data) != 2:
                raise RuntimeError(f'Encountered invalid event record (expected 2 fields, got {len(event_data)})!')
            
            event = HepEvtEvent.from_marley(*event_data)

            particles = list()
            for _ in range(int(event_data[1])):
                line = self._fh.readline()
                data = line.strip(' ').split(' ')
                if len(data) != 15:
                    raise RuntimeError(f'Encountered invalid particle record (expected 15 fields, got {len(data)})!')

                next_particle = HepEvtParticle.from_marley(*data)
                next_particle.event = event
                particles.append(next_particle)

            event.particles = particles

            break
        return event

class HepEvtReaderEDepSim(HepEvtReader):
    def _read_next(self, fh):
        event = None
        for line in self._fh:
            event_data = line.strip(' ').split(' ')
            if len(event_data) != 1:
                raise RuntimeError(f'Encountered invalid event record (expected 1 fields, got {len(event_data)})!')
            
            event = HepEvtEvent.from_edepsim(*event_data)

            particles = list()
            for _ in range(int(event_data[0])):
                line = self._fh.readline()
                data = line.strip(' ').split(' ')
                if len(data) != 8:
                    raise RuntimeError(f'Encountered invalid particle record (expected 8 fields, got {len(data)})!')

                next_particle = HepEvtParticle.from_edepsim(*data)
                next_particle.event = event
                particles.append(next_particle)

            event.particles = particles

            break
        return event
