from django.shortcuts import render,HttpResponse,redirect
from .models import Category
from .models import Images
from django.contrib import messages


# Create your views here.

def home(request):
    cats = Category.objects.all()
    image = Images.objects.all()
    return render(request,'home.html',{'image': image,'cats':cats})



def show_category(request , cid):
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    image = Images.objects.filter(cat=category)
    return render(request,'home.html',{'image':image,'cats':cats})


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        image = []

       
    # image = Images.objects.all()
    else:
        imagetitle = Images.objects.filter(title__icontains=query)
        imagedesc = Images.objects.filter(desc__icontains=query)
        image = imagetitle.union(imagedesc)
      
        
        
   
    if image.count() == 0:
        messages.warning(request, 'No search results found.please refine Your query')
    
   
    param = {'image':image ,'query':query}
    return render(request,'search.html',param)



    
    
   


 

    