def bobot(nilai):
    if (nilai >= 85 and nilai <= 100):
        return 4
    elif (nilai >= 70 and nilai <85 ):
        return 3
    elif (nilai >= 50 and nilai <70):
        return 2
    elif(nilai >= 1 and nilai <50):
        return 1
    else :
        print("!!! Input yang anda masukan salah !!!")


print("#"*30)
print("-"*7,"Menghitung Ipk","-"*7)
print("#"*30)

algoritma = float(input("Masukan Nilai Algoritma :"))
sksAlgoritma = float(input("Masukan jumlah SKS Algoritma :"))
print("Bobot nilai Algoritma anda :",bobot(algoritma))
perancanganObjek = float(input("Masukan Nilai perancangan Objek :"))
sksPerancanganObjek = float(input("Masukan jumlah SKS Perancangan Objek :"))
print("Bobot nilai perancangan objek anda :",bobot(perancanganObjek))
kalkulus = float(input("Masukan Nilai kalkulus :"))
sksKalkulus = float(input("Masukan jumlah SKS Kalkulus :"))
print("Bobot nilai kalkulus anda :",bobot(kalkulus))
etikaProfesi = float(input("Masukan Nilai etika Profesi :"))
sksEtikaProfesi = float(input("Masukan jumlah SKS Etika Profesi :"))
print("Bobot nilai etika Profesi anda :",bobot(etikaProfesi))
dataBase = float(input("Masukan Nilai data Base :"))
sksDataBase = float(input("Masukan jumlah SKS Data Base :"))
print("Bobot nilai data base anda :",bobot(dataBase))
english = float(input("Masukan Nilai english :"))
sksEnglish = float(input("Masukan jumlah SKS English :"))
print("Bobot nilai English anda :",bobot(english))



totalSks = sksAlgoritma + sksPerancanganObjek + sksKalkulus + sksEtikaProfesi +sksDataBase + sksEnglish

totalNilaiAlgoritma = bobot(algoritma) * sksAlgoritma
totalNilaiPerancanganObjek = bobot(perancanganObjek) * sksPerancanganObjek
totalNilaiKalkulus = bobot(kalkulus) * sksKalkulus
totalNilaiEtikaProfesi = bobot(etikaProfesi) * sksEtikaProfesi
totalNilaiDataBase = bobot(dataBase) * sksDataBase
totalNilaiEnglish = bobot(english) * sksEnglish

totalSemuaNilai = totalNilaiAlgoritma + totalNilaiPerancanganObjek + totalNilaiKalkulus + totalNilaiEtikaProfesi + totalNilaiDataBase + totalNilaiEnglish

ipk = totalSemuaNilai / totalSks

print("#"*30)
print("Ipk Anda Adalah : ",ipk)
print("#"*30)

# totalSks  = jumlsh semua sks
# totalNilai = bobot*sks
# totalSemuaNilai = jumlah total semua nilau
# ipk = totalSks / totalSemuaNilai

# print(bobotAlgoritma(algoritma))
# print(bobotAlgoritma(perancanganObjek))
# print(bobotAlgoritma())
# (nilai >=70 and nilai <= 70 )