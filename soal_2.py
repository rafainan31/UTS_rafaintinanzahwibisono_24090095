tahun = int(input('masukan tahun : '))

if tahun / 400:
    print(f'tahun{tahun} tersebut adalah kabisat')
else: 
    print(f'tahun{tahun} tersebut bukan kabisat')