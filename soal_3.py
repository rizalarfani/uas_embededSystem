print("program untuk menghitung nilai indeks prestasi kumulatif mahasiswa")
print('=================================================================== \n')
tugas = float(input('Masukan nilai tugas anda: '))
uts = float(input('Masukan nilai UTS anda: '))
uas = float(input('Masukan nilai UAS anda: '))

presentasiTugas = 0.30
presetasiUTS = 0.30
presentasiUAS = 0.40

total = (float(tugas) * presentasiTugas) + (float(uts) * presetasiUTS) + (float(uas) * presentasiUAS)

if total > 80:
    nilai = 'A'
elif (total >= 70) & (total <= 80):
    nilai = 'B'
elif (total >= 55) & (total <= 70):
    nilai = 'C'
elif (total >= 40) & (total <= 50):
    nilai = 'D'
elif total < 40:
    nilai = 'E'

print("============================================")
print('Nilai Akhir: ', int(total))
print('Niali index: ', nilai)