from django.shortcuts import render

# Create your views here.
def jinja2(request):
    d={'name':'Aishu','age':22}
    return render(request,'jinja2.html',context=d)