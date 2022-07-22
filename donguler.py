#döngüler

krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan Alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"]

x = 0
for kredi in krediler: #döngü türü, o anki listede gezdiğine verdiğimiz takma isim "kredi", alias.
    print(f"{x+1}. kredi :  {kredi}")
    x += 1


for i in range(len(krediler)):
    print(krediler[i])

for i in range(3,10): # 3 dahil 10 dahil değil
    print(i)

for i in range(0, 11,2): # 0'dan başla, 11'e kadar, 2'şer yaz.
    print(i)
