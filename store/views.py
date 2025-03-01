from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

from random import randint
# Create your views here.

def homePage(request):
    allProducts = Product.objects.all()
    products  = Product.objects.all().order_by('-pk').filter(isNew=True)[:12]

    homeInfo = HomePage.objects.get()

    context={'products':products,'homeInfo':homeInfo,'allProducts':allProducts}
    return render(request,"store/home.html",context)

def newArriavalPage(request):
    sortType = request.GET.get('filter_by')
    
    productsNew  = SortingProducts(sortType,True)

    paginator = Paginator(productsNew, 16)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context={'sort':sortType,"page_obj": page_obj,"count":productsNew.count()}
    
    return render(request,"store/new-arrivals.html",context)

def CollectionsPage(request,pk):
    sortType = request.GET.get('filter_by')
    
    subs=Category.objects.get(name=pk)

    productsNew  = SortingProducts(sortType,False,subs)

    paginator = Paginator(productsNew, 16)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context={'sort':sortType,"page_obj": page_obj,"count":productsNew.count(),"subs":subs}
    return render(request,'store/Collection.html',context)

def SortingProducts(key,isNew,subCat=""):
    if subCat=="":
        if isNew:
            if key == "manual":
                return Product.objects.all().order_by('-pk').filter(isNew=True)
            if key == "HighToLow":
                return Product.objects.all().order_by('-price').filter(isNew=True)
            if key == "LowToHigh":
                return Product.objects.all().order_by('price').filter(isNew=True)
        else:
            if key == "manual":
                return Product.objects.all().order_by('-pk')
            if key == "HighToLow":
                return Product.objects.all().order_by('-price')
            if key == "LowToHigh":
                return Product.objects.all().order_by('price')
        return Product.objects.all()
    else:
        products= Product.objects.all().filter(category__name=subCat)
        if isNew:
            if key == "manual":
                return products.order_by('-pk').filter(isNew=True)
            if key == "HighToLow":
                return products.order_by('-price').filter(isNew=True)
            if key == "LowToHigh":
                return products.order_by('price').filter(isNew=True)
        else:
            if key == "manual":
                return products.order_by('-pk')
            if key == "HighToLow":
                return products.order_by('-price')
            if key == "LowToHigh":
                return products.order_by('price')
        return products



def ProductPage(request,pk):
    product=Product.objects.get(slug=pk)
    subs = product.category

    validIds= Product.objects.all().filter(category=subs).count()
    random_profiles_id_list = random.sample(range(validIds), 4)
    RandomProds = Product.objects.filter(id__in=random_profiles_id_list)

    context={'product':product,'subs':subs,'rands':RandomProds}
    return render(request,'store/product.html',context)


def ContactPage(request):
    info = WebSiteInfo.objects.get()

    context = {'info':info}
    return render(request,'store/Contact.html',context)

def CompanyPage(request):

    return render(request,'store/Company.html')

def AboutPage(request):

    return render(request,'store/About.html')

def TermsPage(request):

    return render(request,'store/Terms.html')

def PrivacyPage(request):

    return render(request,'store/Privacy.html')

def PolicyPage(request):

    return render(request,'store/Policy.html')

def WholesalePage(request):

    return render(request,'store/Wholesale.html')


#Cart
def cartView(request):
    
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    orderitems=[]
    order = {'get_total_items':0,'get_total_price':0}

    for i in cart:
        product =  Product.objects.get(id=i)
        price = product.price * cart[i]['quantity']
        order['get_total_price']+=price
        order['get_total_items']+=cart[i]['quantity']

        item = {
            'product':{
                'id':product.id,
                'name':product.name,
                'price':product.price,
                'url':product.image.url
            },
            'quantity':cart[i]['quantity'],
            'price': price,
        }
        orderitems.append(item)
    
    context = {'orderitems':orderitems, 'order':order}
    return render(request,'store/cart.html',context)