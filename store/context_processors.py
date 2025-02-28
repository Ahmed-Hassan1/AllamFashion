from .models import Category,WebSiteInfo,Order
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

# def cart_badge(request):
#     if request.user.is_authenticated and request.user.is_customer:
#         try:
#             customer = request.user.customer
#             order, created = Order.objects.get_or_create(customer=customer, complete=False)
#             cart_items = order.get_total_items
#         except Exception as e:
#             cart_items=0
#     else:
#         try:
#             cart = json.loads(request.COOKIES['cart'])
#         except:
#             cart = {}
#         cart_items=0
#         for i in cart:
#             cart_items += int(cart[i]['quantity'])

#     return {'cart_items':cart_items}