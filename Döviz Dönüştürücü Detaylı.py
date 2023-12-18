from bs4 import BeautifulSoup
import requests

while True:
    print("""
YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ.
[1] DOLAR - TL PARİTESİ
[2] EURO - TL PARİTESİ
[Q] ÇIKIŞ
""")
    seçim = input("Yapmak İstediğiniz İşlemi Tuşlayınız: ")
    if seçim == "q" or seçim == "Q":
        break
    
    veri = float(input("Çevirmek İstediğiniz Dolar Miktarını Giriniz: "))

    r = requests.get("https://kur.doviz.com/serbest-piyasa/amerikan-dolari")
    soup = BeautifulSoup(r.content, "lxml")
    usd = float(soup.find("div", {"class":"text-xl font-semibold text-white"}).text.replace(",", "."))

    t = requests.get("https://kur.doviz.com/serbest-piyasa/euro")
    soup_2 = BeautifulSoup(t.content, "lxml")
    euro = float(soup_2.find("div", {"class":"text-xl font-semibold text-white"}).text.replace(",", "."))



    try:
        if seçim == "1":
            işlem = (veri*usd)
            print(f"{veri} Dolar {işlem} TL'dir.")
        elif seçim == "2":
            işlem_2 = (veri*euro)
            print(f"{veri} Euro {işlem_2} TL'dir.")
    except:
        print("Çevirmek İstediğiniz Miktarı Yazarken Sadece Rakam Kullanınız...")
        break


