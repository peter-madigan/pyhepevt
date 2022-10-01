pyhepevt
--------

This is a lightweight python library to facilitate conversion and manipulation of HepEvt
records using python. To install ::

    pip install .

usage
=====

Conversion scripts between HepEvt formats are provided within `scripts/`. These can be used
to convert HepEvt records of one type to another, e.g. ::

   python scripts/convert_marley_to_edepsim.py <MARLEY HepEvt file> <EDepSim HepEvt file>

Within python, file parsing is broken into reading a file (``HepEvtReader``) and writing
a file (``HepEvtWriter``). Sub-classes are provided for each file format that can be parsed
with a naming convention of (``HepEvtReader<SoftwarePackage>``/``HepEvtWriter<SoftwarePackage>``).

To facilitate the conversion, files are read into intermediate data object(s)
(``HepEvtEvent``/``HepEvtParticle``). These objects use the fields listed in the MARLEY HepEvt
format to store the representation of the event and particle. A ``HepEvtEvent`` also has a
``particles`` attribute that stores all of the particles associated with that event record.
Similarly, a ``HepEvtParticle`` has an ``event`` attribute that stores a reference to the
parent ``HepEvtEvent``.

Below I provide a short example of how to open a file, modify an attribute and then save the
data to a new file ::

    from pyhepevt import HepEvtReaderMARLEY, HepEvtWriterEDepSim

    with HepEvtReaderMARLEY(<input file>) as reader:
        with HepEvtWriterEDepSim(<output file>, 'w'): as writer:
       	    for event in reader:
	        event.phep = [0, 0, 0,] + [event.phep[-1]]*2 # force the particle momentum to zero
	        writer.write(event)

extending
=========

To add read compatibility with a new HepEvt format, one needs to:

 1. implement the ``from_<package>(*args)`` method of the ``HepEvtEvent`` and ``HepEvtParticle``

 2. create a new ``HepEvtReader<SoftwarePackage>`` class inheriting from ``HepEvtReader``

 3. implement the ``_read_next(fh)`` method of the new reader class

To add write compatibility with a new HepEvt format, one needs to:

 1. implement the ``dump_<package>(*args)`` method of the ``HepEvtEvent`` and ``HepEvtParticle``

 2. create a new ``HepEvtWriter<SoftwarePackage>`` class inheriting from ``HepEvtWriter``

 3. implement the ``_write_event(event)`` method of the new reader class