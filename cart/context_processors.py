from .cart import Cart

def cart(request):
    session = request.session
    cart = session.get("cart",{})
    return {"cart":cart}