import os

class Musteri():
    def __init__(self,TC,SIFRE,ISIM):
        self.tc = TC
        self.sifre = SIFRE
        self.isim = ISIM
        self.bakiye = 0


class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self,TC,SIFRE,ISIM):
        self.musteriler.append(Musteri(TC,SIFRE,ISIM))
        print("Internet Bankacılığına Kayıt Olduğnuz için Teşekkürler..")


banka = Banka()


while True:
    os.system("cls")
    print("""
    1) Musteriyim
    2)Musteri olmak istiyorum
    
    """)
    secim = int(input("Seçiminiz : "))

    if secim == 1:
        tcx = [a.tc for a in banka.musteriler]
        TC = input("Enter TC : ")
        if TC in tcx:
            for musteri in banka.musteriler:
                if TC == musteri.tc:
                    sifre = input("Enter a password : ")
                    if sifre == musteri.sifre:
                        print("Welcome Mr {}".format(musteri.isim))
                        while True:
                            os.system("cls")
                            print("""
                                                    1) Bakiye Sorgula
                                                    2)Para Yatır [ Kendi hesabıma ]
                                                    3)Para Yatır [Başka Hesaba ]
                                                    4)Para Çek
                                                    Q)çıkıs

                                                    """)
                            secim2 = (input("İşlem No Girin : "))

                            if secim2 == "1":
                                print("Bakiyeniz : {}".format(musteri.bakiye))
                                input("press enter to back the main menu")
                            elif secim2 == "2":
                                miktar = int(input("miktarı girin"))
                                onay = input(
                                    "Kendi hesabınıza {} tl para yatırmayı onaylıyor musunuz? E/H\n".format(miktar))
                                if onay == "E" or onay == "e":
                                    musteri.bakiye += miktar
                                    print("Paranız yatırıldı")
                                    input("Press enter to back to the main menu")
                                elif onay == "H" or onay == "h":
                                    print("Işlem iptal edildi")
                                    input("press enter to back to the main menu")

                                else:
                                    print("hatalı giriş yaptınız,Işlem iptal edildi")
                                    input("press enter to back to the main menu")
                            elif secim2 == "3":
                                arananTC = input("Musteri TC : ")
                                if arananTC in tcx:
                                    for digerMusteri in banka.musteriler:

                                        if arananTC == digerMusteri.tc:

                                            miktar = int(input("Miktar : "))
                                            if miktar <= musteri.bakiye:

                                                onay = input(
                                                    "{} adlı müşterimize {} tutarında TL tutarında para yuatırmayı onaylıyor musunuz ? E/H\n".format(
                                                        digerMusteri.isim, digerMusteri.miktar))

                                                if onay == "E" or onay == "e":
                                                    digerMusteri.bakiye += miktar
                                                    musteri.bakiye -= miktar
                                                    print("Money has been transferred")
                                                    input("Press enter to back to the main menu")

                                                elif onay == "H" or onay == "h":
                                                    print("Islem iptal edildi")
                                                    input("Press enter to back to the main menu")
                                                else:
                                                    print("Hatalı giris islem iptal edildi")
                                                    input("Press enter to back to the main menu")
                                            else:
                                                print("Bakiyeniz yeterisiz")
                                                input("Press enter to back to the main menu")
                                    else:
                                         print("Müsteri bulunamadı")
                                elif secim2 == "4":
                                    miktar = int(input("Miktar : "))
                                    if miktar <= musteri.bakiye:
                                        musteri.bakiye -= miktar
                                        print("Islem tamamlandı,paranızı alınız")
                                        input("press enter to back to main menu")

                                    else:
                                        print("Yetersiz Bakiye")
                                        input("Press enter to back to the main menu")
                                elif secim2 == "q" or secim2 == "Q":
                                    break


    elif secim == 2:
        a = input("TC :")
        b = input("isim girin : ")
        c = input("sifreyi girin : ")
        banka.musteri_ol(a,c,b)
        input("Press enter to back to the main menu")

    else:
        print("You made a wrong choice")
