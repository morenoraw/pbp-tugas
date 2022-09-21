from mywatchlist.models import WatchlistItem
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers

# TODO: Create your views here.

def show_watchlist(request):
    data_film_mywatchlist = WatchlistItem.objects.all()
    pesan = ""
    watched_counter = 0
    not_watched_counter = 0
    for data in data_film_mywatchlist:
        if data.watched == "Yes":
            watched_counter += 1
        else:
            not_watched_counter += 1
    if watched_counter >= not_watched_counter:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_film': data_film_mywatchlist,
        'nama': 'Moreno Wibisana',
        'npm': '2106752003',
        'pesan' : pesan
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

