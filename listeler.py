# array, liste

krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan Alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"]

print(krediler) #köşeli parantez içerisinde yazar
print(krediler[0]) #array'de hangi index numarasını istersem onu yazar
print(krediler[1])
print(krediler[2])

print(len(krediler), "kredi imkanınız var.") #lenght, kaç eleman var

krediler[0] = "Çabuk Kredi" #0 ıncı elemana atama yaptık
print(krediler[0])

#print(krediler[5]) #burada okuyacak değeri yok.


ogrenciler = ["Yaren", "Nilay", "Halit", "Mert"]
print(ogrenciler)
print(len(ogrenciler),"öğrenciniz var.")
ogrenciler[1] = "Deniz"
print(ogrenciler)
