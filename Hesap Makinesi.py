print("""
__________Hoşgeldin._________

 ================
[1]Toplama 
[2]Çıkarma
[3]Çarpma
[4]Üssünü Alma
[5]Bölme
==================
""")
                                  

veri = input("İşlem :")
if veri =="1":
	x = input("İlk Sayı :")
	x = float(x)
	y = input("İkinci Sayı :")
	y = float(y)
	print("Sonuç :",x + y)


elif veri =="2":
	x = input("İlk Sayı :")
	x = float(x)
	y = input("İkinci Sayı :")
	y = float(y)
	print("Sonuç :",x - y)


elif veri =="3":
	x = input("İlk Sayı :")
	x = float(x)
	y = input("İkinci Sayı :")
	y = float(y)
	print("Sonuç :",x * y)

elif veri =="4":
	x = input("İlk Sayı :")
	x = float(x)
	y = input("İkinci Sayı :")
	y = float(y)
	print("Sonuç :",x ** y)

elif veri =="5":
	x = input("İlk Sayı :")
	x = float(x)
	y = input("İkinci Sayı :")
	y = float(y)
	print("Sonuç :",x / y)

else:
	print("Yanlış Seçim :(")
	print("Program Kapaanıyor")
	quit()
