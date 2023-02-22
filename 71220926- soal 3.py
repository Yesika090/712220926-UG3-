awal = int(input("Masukkan Awal deret : "))
akhir = int(input("Masukkan Akhir deret : "))

for i in range(awal, akhir) :
    if i % 4 == 1 :
        if i % 45 != 0 :
            if i % 6 != 0 :
                print(i,end=" ")



awal = int(input("Masukkan Awal deret : "))
akhir = int(input("Masukkan Akhir deret : "))

for i in range(awal, akhir) :
    if i % 10 == 1 :
        if i % 45 != 0 :
            if i % 20 != 0 :
                print(i,end=" ")
                    