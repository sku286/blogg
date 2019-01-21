from django.contrib import admin
from django.urls import path
from sblog.views import CreateDataApiView
from django.conf.urls import url
from sblog.views import CreateDataApiView

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('$/', CreateDataApiView),
    url(r'^$',CreateDataApiView.as_view(),name = 'blog'),
]
