import re
import sys
import pyttsx3
import random

def terbilang( val):
    # terbilang: mengubah bilangan menjadi rangkaian kata

    # master
    digit = ['nol', 'satu', 'dua', 'tiga', 'empat', 'lima', \
            'enam', 'tujuh', 'delapan', 'sembilan']
    unit1 = ['ratus', 'puluh', '']
    unit3 = ['', 'ribu', 'juta', 'miliar', 'triliun']

    # hanya menerima digit 0-9
    if not val.isnumeric() or len(val) > 3*len(unit3):
        print('Parameter harus berisi angka dg panjang ' \
                +'maks {} digit'.format( 3*len(unit3)))
        sys.exit(1)

    # init empty return value
    retval = []

    for i3 in range(len(unit3)):

        # potong dan proses 3 angka terakhir
        val2 = val[-3:].zfill(3)
        val = val[:-3]
        # siapkan penampungan
        t = []
        for i in range(3):
            if val2[i] != '0':
                t.append(digit[int(val2[i])])
                if unit1[i]: t.append(unit1[i])

        if unit3[i3]: t.append(unit3[i3]+',')
        ts = ' '.join(t)

        # ganti terminologi dengan yang baku
        ts = re.sub('^satu ribu', 'seribu', ts)
        ts = re.sub('^satu ratus', 'seratus', ts)
        ts = re.sub('satu puluh', 'sepuluh', ts)
        ts = re.sub('sepuluh satu', 'sebelas', ts)
        for i in range(2, 10):
            ts = re.sub('sepuluh '+digit[i], digit[i]+' belas', ts)

        # sisip di depan 
        retval.insert(0, ts)
        if val == '':
            break

    return ' '.join(retval) if retval[0] else 'nol'


if __name__ == '__main__':

    print('TERBILANG')

    while True:

        val = input('\nEntri bilangan, '\
                +'atau blank untuk random, atau "q" untuk quit: ')
        if 'q' in val: break
        if not val:
            nd = int('9'*random.randint(1,15))
            val = str(random.randint(0, nd))
    
        txt = terbilang(val)

        print('\nBilangan :', val)
        print('Terbilang:', txt)

