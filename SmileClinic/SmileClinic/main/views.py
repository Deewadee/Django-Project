from django.shortcuts import render
from django.views.generic.base import View

from .models import Specialists


def main(request):
    return render(request, 'main/main.html')


class Index(View):

    def get(self, request):
        specialist = Specialists.objects.all()
        return render(request, "index/index.html", {"Specialists": specialist})


def about_company(request):
    return render(request, 'about_company/about_company.html')


class AllSpec(View):

    def get(self, request):
        specialist = Specialists.objects.all()
        return render(request, "allspec/allspec.html", {"Specialists": specialist})


def contacts(request):
    return render(request, 'contacts/contacts.html')


def my_notes(request):
    return render(request, 'my_notes/my_notes.html')
