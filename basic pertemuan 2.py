/// Opening file in python
myfile = open("perangkat.txt") // summon file lain
content = myfile.read()
myfile.close()
print(content)

python open_file.py
exit()

myfile = open("perangkat.txt")
type(myfile) // melihat tipe

myfile.read() // untuk membaca
myfile.seek(0)
myfile.read()

///Processing file Content
"Hello\nWorld".splitlines() // memecah kata menjadi sebuah list
"abc" in ['abc','asd','awqe'] // memeriksa


/// For loop
a = [1,2,3]
print(a[2])

for item in a :
    print(item)

b="Hello"
for item in b :
    print(item)

TwiceIsBetterThanBlackPink = {"Lisa","Jennie","Rose","Ji-Soo"}
for pin in TwiceIsBetterThanBlackPink :
    print(pin)

a = [1,3,5,7,9]
for i in a:
    b = i + 10
    print(b)

// If else
mylist = [3,4,6,11,2,17,90]
for i in mylist:
    if (i>5):
            print(i)
for hasil in temeratures:
    print(cel_to_fahr(hasil))

/// writing text to file
myfile=open("pegawai.txt","w") // membuat file
myfile.write("Bams") // menghitung isi
myfile.write("\n john") // menghitung isi
myfile.close()
