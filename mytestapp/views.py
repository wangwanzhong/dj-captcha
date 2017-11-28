from django.views.generic.base import View
from django.shortcuts import render

from .forms import MyForm


class IndexView(View):
    def get(self, request):
        myform = MyForm()
        return render(request, 'mytestapp/index.html', {'myform': myform})

    def post(self, request):
        myform = MyForm(request.POST)
        if myform.is_valid():
            clean_data = myform.cleaned_data
            email = clean_data.get('email', '')
            msg = 'Your submit is valid, email is {}'.format(email)
            return render(request, 'mytestapp/index.html', {'myform': myform, 'msg': msg})
        else:
            return render(request, 'mytestapp/index.html', {'myform': myform})
