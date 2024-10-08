from django.shortcuts import render, redirect
from django.views import View

class TreatmentListView(View):

    def get(self, request):
        return render(request, 'treatment-list.html')

class TreatmentResultView(View):

    def get(self, request):
        return render(request, 'treatment-result.html')
    