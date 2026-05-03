# Sistema de recomendación simple

def recomendar_producto(historial_usuario):
    productos = {
        "tecnologia": ["Laptop", "Audífonos", "Smartphone"],
        "ropa": ["Polera", "Jeans", "Chaqueta"],
        "hogar": ["Lámpara", "Silla", "Mesa"]
    }

    recomendaciones = []

    for categoria in historial_usuario:
        if categoria in productos:
            recomendaciones.extend(productos[categoria])

    return recomendaciones


usuario = ["tecnologia", "hogar"]
print("Recomendaciones:", recomendar_producto(usuario))
