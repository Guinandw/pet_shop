
class Carrito():
    
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session['carrito']
        if not carrito:
            self.session['carrito'] = {}
            self.carrito = self.session['carrito']
        else:
            self.carrito = carrito
        
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]= {
                "producto_id": producto.id,
                "nomobre": producto.nombre,
                "sub-total": producto.precio,
                "cantidad": 1
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["sub-total"] += producto.precio
        self.guardar_carrito()
        
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["sub-total"] -= producto.precio
            if self.carrito[id]<=0: self.eliminar(producto)
            self.guardar_carrito()
            
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True