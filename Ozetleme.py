import os
from hashlib import sha256
from hashlib import md5
import csv

vtKaydet="1"
dosya="c:/sozluk.txt"
secim="-1"

def secimFonk(metin):
        if secim=="1":
            a=userInput(" Metni giriniz :")
            print(md5Hash(a))
        elif secim=="2":
            a=userInput(" Metni giriniz :")
            print(shaHash(a))
        elif secim=="3":
            pass
        elif secim=="4":
            pass
        elif secim=="0":
            quit()
        else:
            print ("Hatalı seçim")
            quit()

def userInput(metin):
    return input(metin)

def md5Hash(metin):
    print("\n",metin," kelimesinin MD5 özeti :\n")
    h=md5()
    text=metin.encode("utf-8")
    h.update(text)
    ozett=h.hexdigest()
    if vtKaydet=="1":
        saveToDB(metin, ozett,"md5")
    return ozett

def shaHash(metin):
    print("\n",metin," kelimesinin SHA-256 özeti :\n")
    h=sha256()
    text=metin.encode("utf-8")
    h.update(text)
    ozett=h.hexdigest()
    if vtKaydet=="1":
        saveToDB(metin, ozett,"sha")
    return ozett

def saveToDB(metin,ozet,tur):
    """ metin : salt metin; ozet : ozet deger, tur: md5/hash"""
    dosya=open("sozluk.txt","w")
    sozluk=[metin,ozet,tur]
    with open("sozluk.csv","w") as csvdosya:
        csv_writer=csv.writer(csvdosya,delimiter=",")
        csv_writer.writerow(sozluk)

def ayarlar():
    vtKaydet=input(" MD5 ve SHA değerleri veritabanına kaydedilsin mi 1: Evet, 0: Hayır")
    dosya=input(" Sözlük dosyası: ")

if __name__=="__main__":
    print("""
*******************************************************
*******************************************************
********                                    ***********
********         MD5 ve SHA256              ***********
********        Python Uygulama             ***********
********                                    ***********
*******************************************************
*******************************************************
""")
    print(" Lütfen işlem seçiniz ")
    print("""

  md5 Hash :       (1)
  sha Hash :       (2)
  Sozluk saldirisi (3)
  Ayarlar          (4)
  Çıkış için       (0)
""")

while secim!="0":
    secim=input("Lütfen işleminizi seçini (1 -4) :")
    secimFonk(secim)
    
    
