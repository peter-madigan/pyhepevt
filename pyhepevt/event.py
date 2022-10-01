class HepEvtEvent(object):
    def __init__(self, nevhep, nhep, particles=None):
        self.nevhep = int(nevhep)
        self.nhep = int(nhep)
        self.particles = particles if particles is not None else list()

    @staticmethod
    def from_marley(*args):
        return HepEvtEvent(*args)

    def __repr__(self):
        if len(self.particles):
            return f'HepEvtEvent({self.nevhep}, {self.nhep}, particles=[... {len(self.particles)} ...])'
        return f'HepEvtEvent({self.nevhep}, {self.nhep}, particles=[])'

    def dump_marley(self):
        return_str = f'{self.nevhep} {self.nhep}'
        if len(self.particles):
            return_str += '\n'
            return_str += '\n'.join([p.dump_marley() for p in self.particles])

        return return_str

    def dump_edepsim(self):
        return_str = f'{self.nhep}'
        if len(self.particles):
            return_str += '\n'
            return_str += '\n'.join([p.dump_edepsim() for p in self.particles])

        return return_str    
            
