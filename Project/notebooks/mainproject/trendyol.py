import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
from itertools import product 
import mysql.connector
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)


mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="ahmet2000",
  database="proje"
)
mycursor = mydb.cursor()



header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}

pages=np.arange(1,5,1)
for a in pages:
    r=requests.get("https://www.trendyol.com/laptop-x-c103108?pi="+str(a) ,headers=header,verify=False)
    soup=BeautifulSoup(r.content,"html.parser")
    st1=soup.find_all(["div","a"],attrs={"class":"p-card-wrppr"})

    for store in st1:
        store=store.find("a")
        link_sonu=store["href"]
        link_basi="https://www.trendyol.com/"

        trendyol_link=link_basi+link_sonu

        flink = "https://www.trendyol.com/"
        link = flink+store["href"]

        #print(link_tamami)
        
        markaa=store.find("span",attrs={"class":"prdct-desc-cntnr-ttl"})
        try:
           marka=markaa.get_text()
        except:
            marka='0'   
        trendyolprice=store.find("div",attrs={"class":"prc-box-dscntd"})
        model_ismii=store.find("span",attrs={"class":"prdct-desc-cntnr-name"})
        try:
           model_ismi=model_ismii.get_text()
        except:
            model_ismi='0'
        site_ismi="trendyol"
        site_resmi="trendyol.jpeg"
        urunresmi=str(marka)+ ".jpeg"

        fiyat=trendyolprice.get_text()
       

        trendyoldetay=requests.get(link,headers=header)

        trendyoldetay_soup=BeautifulSoup(trendyoldetay.content,"lxml")

        trendyoltechnic_details=trendyoldetay_soup.find_all("ul",attrs={"class":"detail-attr-container"})
        
        for technic in trendyoltechnic_details:

            trendyola = technic.find_all("li",attrs={"class":"detail-attr-item"})
            for i in trendyola:
                    trendyoltext1 = i.find("span").text
                    if(trendyoltext1=="İşlemci Tipi"):
                        islemci_tipi=i.find("b").text
                    if(trendyoltext1=="SSD Kapasitesi"):   
                        disk_kapasitesi=i.find("b").text
                    if(trendyoltext1=="İşletim Sistemi"):
                        isletim_sistemi=i.find("b").text 

                    if(trendyoltext1=="Ram (Sistem Belleği)"): 
                        bellek_kapasitesi=i.find("b").text 

                    if(trendyoltext1=="Ekran Kartı"):
                        ekrankarti_modeli= i.find("b").text 
            mycursor.execute("INSERT INTO mainproject_notebook (marka, modelismi,link,fiyat,isletimsistemi,islemcimodeli,diskkapasitesi,bellekkapasitesi,ekrankartimodeli,siteismi,resim) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(marka,model_ismi,link,str(fiyat),isletim_sistemi,islemci_tipi,str(disk_kapasitesi),str(bellek_kapasitesi),ekrankarti_modeli,site_ismi,str(urunresmi)))
            mydb.commit()                          
                     
                
                           