from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from Garments.models import Formalshirt, Orders
from Garments.models import Trousers,Orders
from django.db.models import Q
from django.contrib import messages
from Garments.forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def formalshirts(request):
    qs = Formalshirt.objects.all()
    return render(request, 'formalshirts.html', {'lst':qs})
def trousers(request):
    qs = Trousers.objects.all()
    return render(request,'trousers.html', {'lst':qs}) 
def search_list(request):
    str = request.GET.get('query')
    if str:
        match1 =  Formalshirt.objects.filter(Q(name__icontains = str) | Q(desc__icontains = str))
        match2 =  Trousers.objects.filter(Q(name__icontains = str) | Q(desc__icontains = str))
        if match1 or match2:
            return render(request, 'search_list.html', {'match1': match1, 'match2': match2})
        else:
            messages.error(request, 'no results found')
    else:
        return HttpResponseRedirect('search_list')
    return render(request, 'search_list.html') 

def contactus(request):
    form = ContactForm
    return render(request, 'contactus.html', {'form':form})

def cart(request, id):
    #item = Formalshirt.objects.get(pk=id)
    item1 = get_object_or_404(Formalshirt, pk = id),
    if item1:
        obj1 = Orders(formalshirt=item1)
        obj1.save()
    return formalshirts(request)
def cart(request,id):
    item2 = get_object_or_404(Trousers, pk = id)
    if item2:
        obj2 = Orders(trousers=item2)
        obj2.save()
    return trousers(request)

'''
def cart(request, id):
    #item = Trousers.objects.get(pk=id)
    item = get_object_or_404(Trousers, pk = id)
    if item:
        obj = Orders(trousers = item)
        obj.save()
    return trousers(request)
'''

def shoppingcart(request):
    qs = Orders.objects.all()
    n = len(qs)
    tot = 0
    for i in qs:
        tot = tot+i.formalshirt.price + i.trousers.price
    return render(request, 'shoppingcart.html', {'lst':qs, 'n':n, 'tot':tot})

def clearcart(request):
    qs = Orders.objects.all()
    for i in qs:
        i.delete()
    return render(request, 'shoppingcart.html')

 
 