
# definition, fonksiyon tanımlama
def kredileriListele(): 
    krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan Alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"]
    x = 0
    for kredi in krediler: #döngü türü, o anki listede gezdiğine verdiğimiz takma isim "kredi", alias.
        print(f"{x+1}. kredi :  {kredi}")
        x += 1   # yukarıdaki kodlar sadece fonksiyonun tanımı, aşağıdaki yoksa çıktı alamam.

kredileriListele() # burası fonksiyonu çağırdığım yer, istediğim kadar fazl sayfada/yerde çağırabilirim.
