from django.shortcuts import render
from .models import Item

def populate_cats():
    cats = ['Whiskers', 'Mittens', 'Snowball', 'Luna', 'Simba']  # Список імен котів
    
    # Додайте кожне ім'я кота до бази даних
    for cat_name in cats:
        cat = Item(name=cat_name)
        cat.save()



def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})
