"""DavysPets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from paypal.standard.ipn import urls as paypal_urls
from DavysPets.settings import MEDIA_ROOT
from accounts import views as accounts_views
from blog.views import get_contacts, get_index, get_about, get_gallery, get_contact_us
from paypal_store import views as paypal_views
from products import views as product_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index'),
    url(r'^contacts/', get_contacts),
    url(r'^about/$' , get_about, name='about'),
    url(r'^contact_us/$' , get_contact_us, name='contact_us'),
    url(r'^gallery/$' , get_gallery, name='gallery'),
    url(r'', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^static/(?P<path>.*)$', serve),
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/$', paypal_views.paypal_return),
    url(r'^paypal-cancel/$', paypal_views.paypal_cancel),
    url(r'^products/$', product_views.all_products),
    url(r'', include('cart.urls')),
]
