class HepEvtEvent(object):
    ''' Internal representation of an event record. '''
    
    def __init__(self, nevhep, particles=None):
        '''
        Event records are defined by::
        
         - an event number ``nevhep`` (``int``)
         - a number of associated particles ``nhep`` (``int``)
         - a collection of particles ``particles`` (``list`` of ``HepEvtParticle``)

        '''
        
        self.nevhep = int(nevhep)
        self.particles = particles if particles is not None else list()

    def __repr__(self):
        if len(self.particles):
            return f'HepEvtEvent({self.nevhep}, particles=[... {len(self.particles)} ...])'
        return f'HepEvtEvent({self.nevhep}, particles=[])'

    @property
    def nhep(self):
        return len(self.particles)
        
    @staticmethod
    def from_marley(*args):
        ''' Parse the header of an MARLEY-formatted event record '''
        return HepEvtEvent(args[0])

    def dump_marley(self):
        ''' Dump the full MARLEY-formatted event record string '''
        return_str = f'{self.nevhep} {self.nhep}'
        if self.nhep != 0:
            return_str += '\n'
            return_str += '\n'.join([p.dump_marley() for p in self.particles])

        return return_str

    @staticmethod
    def from_edepsim(*args):
        ''' Parse the header of an EDepSim-formatted event record '''
        return HepEvtEvent(args[0])

    def dump_edepsim(self):
        ''' Dump the full EDepSim-formatted event record string '''
        return_str = f'{self.nhep}'
        if len(self.particles):
            return_str += '\n'
            return_str += '\n'.join([p.dump_edepsim() for p in self.particles])

        return return_str    
            
