from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.

def show_katalog(request):
    return render(request, "katalog.html", context)

data_barang_catalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_catalog,
    'nama': 'Moreno Wibisana',
    'npm': '2106752003'
}
