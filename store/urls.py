from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('',homePage,name="home"),
    path('new_arrivals',newArriavalPage,name="new-arrivals"),
    path('collection/<str:pk>/',CollectionsPage,name='collection'),
    re_path(r'product/(?P<pk>[-\w]+)/$',ProductPage,name='product'),#fixed unicode in URL with regex
    path('contact/',ContactPage,name='contact'),

    path('company/',CompanyPage,name='company'),
    path('about-us/',AboutPage,name='about-us'),
    path('terms/',TermsPage,name='terms'),
    path('privacy/',PrivacyPage,name='privacy'),
    path('policy/',PolicyPage,name='policy'),
    path('wholesale/',WholesalePage,name='wholesale'),
]