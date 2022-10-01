class HepEvtParticle(object):
    def __init__(self, isthep, idhep, jmohep1, jmohep2, jdahep1, jdahep2, phep1, phep2, phep3, phep4, phep5, vhep1, vhep2, vhep3, vhep4, event=None):
        self.isthep = int(isthep)
        self.idhep = int(idhep)
        self.jmohep1 = int(jmohep1)
        self.jmohep2 = int(jmohep2)
        self.jdahep1 = int(jdahep1)
        self.jdahep2 = int(jdahep2)
        self.phep1 = float(phep1)
        self.phep2 = float(phep2)
        self.phep3 = float(phep3)
        self.phep4 = float(phep4)
        self.phep5 = float(phep5)
        self.vhep1 = float(vhep1)
        self.vhep2 = float(vhep2)
        self.vhep3 = float(vhep3)
        self.vhep4 = float(vhep4)
        self.event = event if event is not None else None

    def __repr__(self):
        return f'HepEvtParticle({self.isthep}, {self.idhep}, {self.jmohep1}, {self.jmohep2}, {self.jdahep1}, {self.jdahep2}, {self.phep1}, {self.phep2}, {self.phep3}, {self.phep4}, {self.phep5}, {self.vhep1}, {self.vhep2}, {self.vhep3}, {self.vhep4}, event={self.event})'

    @staticmethod
    def from_marley(*args):
        return HepEvtParticle(*args)

    def dump_marley(self):
        return f'{self.isthep} {self.idhep} {self.jmohep1} {self.jmohep2} {self.jdahep1} {self.jdahep2} {self.phep1} {self.phep2} {self.phep3} {self.phep4} {self.phep5} {self.vhep1} {self.vhep2} {self.vhep3} {self.vhep4}'

    def dump_edepsim(self):
        return f'{self.isthep} {self.idhep} {self.jmohep1} {self.jmohep2} {self.phep1} {self.phep2} {self.phep3} {self.phep4}'

    @property
    def jmohep(self):
        return [self.jmohep1, self.fmohep2]

    @jmohep.setter
    def jmohep(self, obj):
        self.jmohep1 = int(obj[0])
        self.jmohep2 = int(obj[1])

    @property
    def jdahep(self):
        return [self.jdahep1, self.fdahep2]

    @jdahep.setter
    def jdahep(self, obj):
        self.jdahep1 = int(obj[0])
        self.jdahep2 = int(obj[1])

    @property
    def phep(self):
        return [self.phep1, self.phep2, self.phep3, self.phep4, self.phep5]

    @phep.setter
    def phep(self, obj):
        self.phep1 = float(obj[0])
        self.phep2 = float(obj[1])
        self.phep3 = float(obj[2])
        self.phep4 = float(obj[3])
        self.phep5 = float(obj[4])

    @property
    def vhep(self):
        return [self.vhep1, self.vhep2, self.vhep3, self.vhep4]

    @vhep.setter
    def vhep(self, obj):
        self.vhep1 = float(obj[0])
        self.vhep2 = float(obj[1])
        self.vhep3 = float(obj[2])
        self.vhep4 = float(obj[3])
        
