import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from itertools import product 
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="ahmet2000",
  database="proje"
)
mycursor = mydb.cursor()


disable_warnings(InsecureRequestWarning)
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}

pages=np.arange(1,2,1)
for a in pages:
    r=requests.get("https://www.turkcell.com.tr/pasaj/bilgisayar-tablet/bilgisayarlar?page="+str(a)+"&sortBy=popular&sortType=desc" ,headers=header,verify=False)
    soup=BeautifulSoup(r.content,"html.parser")
    st1=soup.find_all(["div","a"],attrs={"class":"m-grid-col-4"})
    for store in st1:
        store=store.find("a")
        link_sonu=store["href"]
        link_basi="https://www.turkcell.com.tr/"
        link_tamami=link_basi+link_sonu
        urun_linki=link_tamami
        
        title=store.find("span",attrs={"class":"m-p-pc__title"})
        price=store.find("div",attrs={"class":"m-p-pc__price"})
        detay=requests.get(link_tamami,headers=header,verify=False)
        detay_soup=BeautifulSoup(detay.content,"html.parser")
        technic_details=detay_soup.find_all("div",attrs={"class":"m-product-detail-features__container"})
        for technic in technic_details:
                    print("Site İsmi ===== Turkcell")
                    site_ismi='Turkcell'
                    site_resmi="Turkcell.jpeg"
                    
                    print("Ürün Linki  ===  "+link_tamami)
                    try:

                        print("Marka  ===  "+title.get_text())
                        model_ismi=title.get_text()
                    except:
                        print("Marka  ===  0") 
                    try:
                        print("Fiyat  ===  "+price.get_text().strip())
                        urun_fiyat=price.get_text().strip()
                    except:
                        print("Fiyat  ===  0")
                        urun_fiyat=0
                    x = technic.find_all("div",attrs={"class":"m-product-detail-features__wrap"})
                    for j in x:
                        etiket = j.find("div",attrs={"class":"m-product-detail-features__title"})
                        deger = j.find("div",attrs={"class":"m-product-detail-features__text"})
                        if(str(etiket.get_text())== "İşlemci Markası (cpu)"):
                                #print(str(etiket.get_text()) + " === " +str(deger.get_text()))
                                islemci_marka=str(deger.get_text())
                        if(str(etiket.get_text())== "İşlemci Modeli (cpu)"):
                                #print(str(etiket.get_text()) + " === " +str(deger.get_text()))
                                islemci_modeli=deger.get_text()         
                        if(str(etiket.get_text())== "İşletim Sistemi"):
                                #print(str(etiket.get_text()) + " === " +str(deger.get_text()))
                                isletim_sistemi=str(deger.get_text())
                        if((str(etiket.get_text())== "Ürün Model Adı")):
                                #print(str(etiket.get_text()) + " === " +str(deger.get_text()))
                                model=str(deger.get_text())
                                markaa=model.split(" ")
                                marka=markaa[0]
                                urunresmi=marka+".jpeg"
                        if((str(etiket.get_text())== "Ekran Kartı")):
                                #print(str(etiket.get_text()) + " === " +str(deger.get_text()))
                                ekrankarti_modeli=str(deger.get_text())
                        if((str(etiket.get_text())== "Bellek Ram")):
                                #print(str(etiket.get_text()) + " === " +str(deger.get_text()))
                                bellek_kapasitesi=str(deger.get_text())
                        if((str(etiket.get_text())== "Sabit Disk Ssd Boyutu")):
                                #print(str(etiket.get_text()) + " === " +str(deger.get_text()))
                                disk_kapasitesi=str(deger.get_text())
                    mycursor.execute("INSERT INTO mainproject_notebook (marka, modelismi,link,fiyat,isletimsistemi,islemcimodeli,diskkapasitesi,bellekkapasitesi,ekrankartimodeli,siteismi,resim) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(marka,model_ismi,urun_linki,str(urun_fiyat),isletim_sistemi,islemci_marka,str(disk_kapasitesi),str(bellek_kapasitesi),ekrankarti_modeli,site_ismi,urunresmi))
                    mydb.commit()             


                             
                                
                        

                    
        print(" ")
        print(" ")
