from multiprocessing import context
from django.shortcuts import render,redirect
from mainproject.models import  Hepsiburada, Notebook
  
notebook_list = [
    {
        "id":1,
        "notebook_name": "Casper Nirvana",
        "statement": "aciklama",
        "image": "1.jpeg"

    },
    {
        "id":2,
        "notebook_name": "Lenovo",
        "statement": "aciklama",
        "image": "2.jpeg"

    },
    {
        "id":3,
        "notebook_name": "Mac",
        "statement": "aciklama",
        "image": "3.jpeg"

    },
    {
        "id":4,
        "notebook_name": "Casper",
        "statement": "aciklama",
        "image": "4.jpeg"

    }
        

]


def home(request):
    data = {
        
        "notebooks": notebook_list
    }
    return render(request, "index.html", data)



def details(request, id):
    notebooks=Notebook.objects.all()
    selectedNotebook=None

    for notebook in notebooks:
        if getattr(notebook, 'id')==id:
            selectedNotebook=notebook
        
    
    
    return render(request, "details.html",{

    "notebook":selectedNotebook
        
    })


def notebooks(requests):
    notebooks=Notebook.objects.all()
    
    
    return render(requests,'notebooks.html',{
        "notebooks":notebooks,
        
        
       
    })


#def hepsiburada(requests):
    hepsiburada=Hepsiburada.objects.all()
    return render(requests,'notebooks.html',{

        "hepsiburada":hepsiburada
       
    })

def maxprice(requests):
    notebooksmaxprice=Notebook.objects.all().order_by('-fiyat')
    return render(requests,'maxprice.html',{

        "notebooks":notebooksmaxprice
    })

def minprice(requests):
    notebooksminprice=Notebook.objects.extra(select={"custom":"fiyat = 0"}, order_by=["custom","fiyat"]).all()
    return render(requests,'minprice.html',{

        "notebooks":notebooksminprice
    })

def search(requests):
    q=requests.GET['q']
    notebooks=Notebook.objects.all().filter(modelismi__icontains=q,).order_by('-id')
    return render(requests,'search.html',{
        'notebooks':notebooks,
    })  






'''def show(request):
    notebooks = Notebook.objects.all()
    return render(request,"show.html",{'notebook':notebooks})
'''