x = 7
y = 2

if x > y:
    print(x, "sayısı", y, "sayısından büyüktür" )
elif x < y:
    print(y, "sayısı", x, "sayısından büyüktür")
else:
    print(" ")

print("******-------******")

k = 10
l = 20
m = 30

if k>l and k>m:
    print(k, "değeri hepsinin en büyüğüdür.")
elif l>k and l>m:
    print(l,"değeri hepsinin en büyüğüdür.")
else:
    print(m, "değeri hepsinin en büyüğüdür.")
    

if k<l and k<m:
    print(k, "değeri hepsinin en küçüğüdür.")
elif l<k and l<m:
    print(l,"değeri hepsinin en küçüğüdür.")
else:
    print(m, "değeri hepsinin en küçüğüdür.")


dolarDun = 7.65
dolarBugun = 7.75

if dolarDun > dolarBugun:
    print("Azalış oku")
    print("Bitti")
elif dolarDun< dolarBugun:
    print("Artış oku")
else:
    print("Eşittir oku")
    
print("Bitti")

#if dolarDun<dolarBugun:
    #print("Artış oku")

#if dolarDun==dolarBugun:
    #print("Eşittir oku")