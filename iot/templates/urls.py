from django.urls import path,include

from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.first,name='first'),
    path('second',views.second,name='second'),
    path('templive',views.live,name='live'),
    path('tempgraph',views.temp,name='tempgraph'),
    path('presslive',views.presslive,name='livep'),
    path('pressgraph',views.press,name='pressgraph'),
    path('altgraph',views.alt,name='altgraph'),
    path('allgraph',views.all,name='all'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)