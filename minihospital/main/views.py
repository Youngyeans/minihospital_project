from django.shortcuts import render, redirect
from django.views import View

class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')
    
class ContactView(View):

    def get(self, request):
    
        return render(request, 'contact.html')