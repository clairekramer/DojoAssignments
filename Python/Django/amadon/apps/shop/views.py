from django.shortcuts import render, redirect

items = [
    {
        "id": 1015,
        "name": "Xbox",
        "price": 199.99
    },
    {
        "id": 1016,
        "name": "PS4",
        "price": 350.00
    },
    {
        "id": 1017,
        "name": "Nintendo 64",
        "price": 65.00
    }
]

def index(request):
    if 'cart' in request.session.keys():
        del request.session['cart']
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'total_items' not in request.session:
        request.session['total_items'] = 0
    context = {
        'items': items
    }
    return render(request, 'shop/index.html', context)

def buy(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            cost = item['price'] * int(request.POST['quantity'])
    request.session['total'] += cost
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['cart'] = cost
    return redirect('/checkout')

def checkout(request):
    return render(request, 'shop/checkout.html')
