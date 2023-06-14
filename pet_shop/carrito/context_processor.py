def total_carrito(request):
    total = 0
    
    
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += value["subtotal"]
    return {"total_carrito": total}

def cantidad_productos(request):
    cantidad_productos = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            
            for key, value in request.session["carrito"].items():
                cantidad_productos += value["cantidad"]
    return { "cantidad_productos":cantidad_productos}
    