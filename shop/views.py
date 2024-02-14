from django.shortcuts import render
from django.views import View
from .models import *

class Home(View):
    def get(self,request):
        content={
            "products": Product.objects.all(),
            "categories":Category.objects.all()
        }
        return render(request, "index.html", content)