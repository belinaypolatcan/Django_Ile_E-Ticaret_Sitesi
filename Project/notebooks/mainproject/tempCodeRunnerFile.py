from operator import mod
from os import link
from re import L
from xml.sax.xmlreader import AttributesImpl 
import numpy as np
import requests
from bs4 import BeautifulSoup
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


    k=requests.get("http://www.n11.com/bilgisayar/dizustu-bilgisayar?ipg="+str(a),headers=header,verify=False)
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117"}
    n11soup=BeautifulSoup(k.content,"html.parser")
    st1=n11soup.find_all("li",attrs={"class":"column"})
    for store in st1:
        n11fiyat_link=store.find_all("div",attrs={"class":"columnContent"})
        for j in n11fiyat_link:
            j=j.find("a")
            n11link=j["href"]
            resim="n11.jpeg" 
            print(n11link)
            n11price=store.find("span",attrs={"class":"newPrice"})
            n11tittle=store.find("h3",attrs={"class":"productName"}) 
                                                    
            n11detay=requests.get(n11link,headers=header,verify=False)

            n11detay_soup=BeautifulSoup(n11detay.content,"html.parser")

            n11technic_details=n11detay_soup.find_all("ul",attrs={"class":"unf-prop-list"})
                                            
            for technic in n11technic_details:
                # print("Site İsmi ===== n11")
                n11site_ismi='n11'
                n11resim="n11.jpeg"                                   
                #print("Ürün Linki  ===  "+link_tamami)
                try:

                  #print("Marka  ===  "+n11tittle.get_text())
                  n11model_ismi=n11tittle.get_text()
                                                            
                except:
                    print("Marka  ===  0") 
                try:

                    #print("Fiyat  ===  "+n11price.get_text().strip())
                    n11fiyat=n11price.get_text().strip()
                except:
                    print("Fiyat  ===  0")
                a = technic.find_all("li",attrs={"class":"unf-prop-list-item"})
                for i in a:
                    n11etiket = i.find("p",attrs={"class":"unf-prop-list-title"})
                    n11deger = i.find("p",attrs={"class":"unf-prop-list-prop"})
                    if(str(n11etiket.get_text())== "İşlemci"):
                        #print(str(n11etiket.get_text()) + " === " +str(n11deger.get_text()))
                        n11islemcimodeli=n11deger.get_text()
                                                            
                    if((str(n11etiket.get_text())== "İşletim Sistemi")):
                        #print(str(n11etiket.get_text()) + " === " +str(n11deger.get_text()))
                        n11isletim_sistemi=n11deger.get_text()
                                                                
                    if((str(n11etiket.get_text())== "Marka")):
                        #print(str(n11etiket.get_text()) + " === " +str(n11deger.get_text()))
                        n11marka=n11deger.get_text()
                        n11resim=n11marka+'.jpeg'
                                                                
                    if((str(n11etiket.get_text())== "Model")):
                        print(str(n11etiket.get_text()) + " === " +str(n11deger.get_text()))
                        n11model=str(n11deger.get_text())
                        
                                                            
                    if((str(n11etiket.get_text())== "Ekran Kartı Modeli")):
                        #print(str(n11etiket.get_text()) + " === " +str(n11deger.get_text()))
                        n11ekrankarti_modeli=n11deger.get_text()
                                                                
                    if((str(n11etiket.get_text())== "Bellek Kapasitesi")):
                        #print(str(n11etiket.get_text()) + " === " +str(n11deger.get_text()))
                        n11bellek_kapasitesi=n11deger.get_text()
                                                                
                    if((str(n11etiket.get_text())== "Disk Kapasitesi")):
                        #print(str(n11etiket.get_text()) + " === " +str(n11deger.get_text()))
                        n11disk_kapasitesi=n11deger.get_text()
                                                                
                    if((str(n11etiket.get_text())== "Disk Türü")):
                        #print(str(n11etiket.get_text()) + " === " +str(n11deger.get_text()))
                        n11disk_turu=n11deger.get_text()
                                                            
                                                       
                                    
                mycursor.execute("INSERT INTO mainproject_notebook (marka, modelismi,link,fiyat,isletimsistemi,islemcimodeli,diskkapasitesi,bellekkapasitesi,ekrankartimodeli,siteismi,resim) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(n11marka,n11model_ismi,n11link,str(n11fiyat),n11isletim_sistemi,n11islemcimodeli,str(n11disk_kapasitesi),str(n11bellek_kapasitesi),n11ekrankarti_modeli,n11site_ismi,n11resim))
                mydb.commit()                           


                    
                        
                