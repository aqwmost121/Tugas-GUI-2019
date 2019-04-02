pins = {"Wildan":1212,"toto":1111,"oppo":1414}
pins["Wildan"]
type(pins["toto"]) // cek tipe int
pins.keys()
pins.values()
pins["Nia"]=3333 // tambah
pins
pins.pop("Nia") // hapus
pins["elok"] = "AB123" // nilai string

//Buat inputan
masukan = input("Masukkan Nama anda :")
bilangan = input("Masukkan angka :")
print(masukan)
bilangan = int(input("masukkan angka : ")) // angka
print(bilangan**2)
pecahan = float(input("masukkan angka : ")) // pecahan
print(pecahan**2)

//Conditional
kode in pins.values() // apakah kode ada di pins key

if 1<5:
    tab print("Yes")
else:
    tab print("No")
    enter 2x

// Multiple Condition
user_input = float(input("Masukkan Angka : "))
if user_input > 100:
        print("Greater")
else:
        print("Smaller")
enter 2x

if user_input > 100:
        print("Lebih Besar")
elif user_input == 88:
        print("Sama Kok")
else:
        print("Lebih Kecil")
enter 2x

// Function
def printing():
        print("Hallo")
        print("Dunia")
enter 2x
printing() // untuk memanggil fucntion

def luas_persegi(sisi):
        luas = sisi * sisi
        return luas
enter 2x
luas_persegi(6)

// Menghitung luas segitiga
def luas_segitiga(alas,tinggi):
    luas = (alas*tinggi)/2
    print("Luas segitiga : %d" %luas
enter 2x
luas_segitiga(100,50)
