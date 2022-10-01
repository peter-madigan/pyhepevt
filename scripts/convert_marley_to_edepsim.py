import sys
import time

from pyhepevt import HepEvtReaderMARLEY, HepEvtWriterEDepSim

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]

with HepEvtReaderMARLEY(INPUT_FILE) as reader:
    with HepEvtWriterEDepSim(OUTPUT_FILE, 'w') as writer:        
        start = time.time()
        last = start
        i = 0
        for i,event in enumerate(reader):
            writer.write(event)
            if time.time() - last > 0.1:
                print('event',i+1,f'elapsed time: {time.time()-start:0.2e}s',end='\r')
                last = time.time()
        print('event',i+1,f'elapsed time: {time.time()-start:0.2e}s')

print('Done!')
