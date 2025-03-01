from .models import Category,WebSiteInfo
import json

def store_menu(request):
    menu_items = Category.objects.all()

    logo = logoURL()
    return {'menu_items':menu_items,'logo':logo}

def logoURL():
    try:
        logo = WebSiteInfo.objects.get().Logo.url
        return logo
    except:
        return ''

def cart_badge(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    cart_items=0
    for i in cart:
        cart_items += int(cart[i]['quantity'])

        print(int(cart[i]['quantity']))
    return {'cart_items':cart_items} 