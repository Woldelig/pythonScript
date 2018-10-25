import json
import sys
filnavn = sys.argv[1]
formatertFilnavn = 'Formatert-'+filnavn
with open(filnavn, 'r') as inputfil:
    with open(formatertFilnavn, 'w') as outputfil:
        print('[', file=outputfil)
        for line in inputfil:
            line = line.rstrip('\n') + ','
            print(line, file=outputfil)
        print(']',file=outputfil)
        print('Husk å fjern komma fra det siste json objektet!')