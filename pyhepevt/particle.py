class HepEvtParticle(object):
    def __init__(self, ist, id, jmo1, jmo2, jda1, jda2, p1, p2, p3, p4, m, v1, v2, v3, v4, event=None):
        self.ist = int(ist)
        self.id = int(id)
        self.jmo = [int(jmo1), int(jmo2)]
        self.jda = [int(jda1), int(jda2)]
        self.p = [float(p1), float(p2), float(p3), float(p4)]
        self.m = float(m)
        self.v = [float(v1), float(v2), float(v3), float(v4)]
        self.event = event if event is not None else None

    def __repr__(self):
        return f'HepEvtParticle({self.ist}, {self.id}, {self.jmo[0]}, {self.jmo[1]}, {self.jda[0]}, {self.jda[1]}, {self.p[0]}, {self.p[1]}, {self.p[2]}, {self.p[3]}, {self.m}, {self.v[0]}, {self.v[1]}, {self.v[2]}, {self.v[3]}, event={self.event})'

    @staticmethod
    def from_marley(*args):
        return HepEvtParticle(*args)

    def dump_marley(self):
        return f'{self.ist} {self.id} {self.jmo[0]} {self.jmo[1]} {self.jda[0]} {self.jda[1]} {self.p[0]} {self.p[1]} {self.p[2]} {self.p[3]} {self.m} {self.v[0]} {self.v[1]} {self.v[2]} {self.v[3]}'

    @staticmethod
    def from_edepsim(*args):
        return HepEvtParticle(*args[:4], 0, 0, *args[4:], 0, 0, 0, 0, 0)
    
    def dump_edepsim(self):
        return f'{self.ist} {self.id} {self.jmo[0]} {self.jmo[1]} {self.p[0]} {self.p[1]} {self.p[2]} {self.p[3]}'
