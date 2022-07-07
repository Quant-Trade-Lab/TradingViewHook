"""tradingview_webhook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from ninja import Schema
from record.models import Record

api = NinjaAPI()


class Signal(Schema):
    type: int


@api.post("/trade")
def trade(request, item: Signal):
    employee = Record.objects.create(type=item.type)
    print(item.type)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
