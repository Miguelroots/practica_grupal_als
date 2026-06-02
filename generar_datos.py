import pandas as pd
import numpy as np
import random

# Para reproducibilidad
np.random.seed(42)
random.seed(42)

print("Iniciando la generación del dataset de Créditos Económicos...")

# 1. Registro de 35 productos reales de Créditos Económicos
productos_data = [
    # Tecnología
    {"id_producto": 1, "nombre": "Celular Samsung Galaxy A54 128GB", "categoria": "Tecnologia", "marca": "Samsung", "tienda": "Creditos Economicos", "precio": 349.99},
    {"id_producto": 2, "nombre": "Celular Xiaomi Redmi Note 12 128GB", "categoria": "Tecnologia", "marca": "Xiaomi", "tienda": "Creditos Economicos", "precio": 199.99},
    {"id_producto": 3, "nombre": "Celular iPhone 14 Pro 128GB", "categoria": "Tecnologia", "marca": "Apple", "tienda": "Creditos Economicos", "precio": 1099.99},
    {"id_producto": 4, "nombre": "Celular Honor X8a 128GB", "categoria": "Tecnologia", "marca": "Honor", "tienda": "Creditos Economicos", "precio": 249.99},
    {"id_producto": 5, "nombre": "Celular Samsung Galaxy S23 Ultra", "categoria": "Tecnologia", "marca": "Samsung", "tienda": "Creditos Economicos", "precio": 1199.99},
    {"id_producto": 6, "nombre": "Laptop HP 15-dy2024la Core i3", "categoria": "Tecnologia", "marca": "HP", "tienda": "Creditos Economicos", "precio": 499.99},
    {"id_producto": 7, "nombre": "Laptop Asus VivoBook 15 Core i5", "categoria": "Tecnologia", "marca": "Asus", "tienda": "Creditos Economicos", "precio": 649.99},
    {"id_producto": 8, "nombre": "Laptop Lenovo IdeaPad 3 Ryzen 5", "categoria": "Tecnologia", "marca": "Lenovo", "tienda": "Creditos Economicos", "precio": 529.99},
    {"id_producto": 9, "nombre": "MacBook Air 13'' Chip M2 256GB", "categoria": "Tecnologia", "marca": "Apple", "tienda": "Creditos Economicos", "precio": 1299.99},
    {"id_producto": 10, "nombre": "Tablet Lenovo Tab M10 HD", "categoria": "Tecnologia", "marca": "Lenovo", "tienda": "Creditos Economicos", "precio": 179.99},
    
    # TV y Audio (Entretenimiento)
    {"id_producto": 11, "nombre": "Smart TV LG 55'' UHD 4K", "categoria": "TV y Audio", "marca": "LG", "tienda": "Creditos Economicos", "precio": 489.99},
    {"id_producto": 12, "nombre": "Smart TV Samsung 65'' Crystal 4K", "categoria": "TV y Audio", "marca": "Samsung", "tienda": "Creditos Economicos", "precio": 699.99},
    {"id_producto": 13, "nombre": "Smart TV Sony Bravia 75'' 4K HDR", "categoria": "TV y Audio", "marca": "Sony", "tienda": "Creditos Economicos", "precio": 1399.99},
    {"id_producto": 14, "nombre": "Smart TV TCL 43'' Full HD", "categoria": "TV y Audio", "marca": "TCL", "tienda": "Creditos Economicos", "precio": 279.99},
    {"id_producto": 15, "nombre": "Soundbar Samsung HW-T450 Bluetooth", "categoria": "TV y Audio", "marca": "Samsung", "tienda": "Creditos Economicos", "precio": 149.99},
    {"id_producto": 16, "nombre": "Consola PlayStation 5 Slim 1TB", "categoria": "TV y Audio", "marca": "Sony", "tienda": "Creditos Economicos", "precio": 649.99},
    {"id_producto": 17, "nombre": "Consola Nintendo Switch OLED 64GB", "categoria": "TV y Audio", "marca": "Nintendo", "tienda": "Creditos Economicos", "precio": 399.99},
    {"id_producto": 18, "nombre": "Audífonos Gamer HyperX Cloud II", "categoria": "Tecnologia", "marca": "HyperX", "tienda": "Creditos Economicos", "precio": 89.99},
    {"id_producto": 19, "nombre": "Reloj Inteligente Huawei Watch GT 4", "categoria": "Tecnologia", "marca": "Huawei", "tienda": "Creditos Economicos", "precio": 229.99},
    
    # Electrodomésticos
    {"id_producto": 20, "nombre": "Refrigeradora Indurama RI-485 390L", "categoria": "Electrodomesticos", "marca": "Indurama", "tienda": "Creditos Economicos", "precio": 629.99},
    {"id_producto": 21, "nombre": "Cocina Indurama Montecarlo 4Q a Gas", "categoria": "Electrodomesticos", "marca": "Indurama", "tienda": "Creditos Economicos", "precio": 459.99},
    {"id_producto": 22, "nombre": "Lavadora Samsung WA19T6260BY 19kg", "categoria": "Electrodomesticos", "marca": "Samsung", "tienda": "Creditos Economicos", "precio": 679.99},
    {"id_producto": 23, "nombre": "Refrigeradora LG No Frost 400L", "categoria": "Electrodomesticos", "marca": "LG", "tienda": "Creditos Economicos", "precio": 799.99},
    {"id_producto": 24, "nombre": "Cocina Mabe a Gas 4 quemadores", "categoria": "Electrodomesticos", "marca": "Mabe", "tienda": "Creditos Economicos", "precio": 299.99},
    {"id_producto": 25, "nombre": "Microondas Mabe 20 Litros Negro", "categoria": "Electrodomesticos", "marca": "Mabe", "tienda": "Creditos Economicos", "precio": 109.99},
    {"id_producto": 26, "nombre": "Licuadora Oster Reversible 2 Velocidades", "categoria": "Electrodomesticos", "marca": "Oster", "tienda": "Creditos Economicos", "precio": 95.00},
    {"id_producto": 27, "nombre": "Freidora de Aire Black & Decker 4.5L", "categoria": "Electrodomesticos", "marca": "Black & Decker", "tienda": "Creditos Economicos", "precio": 85.00},
    {"id_producto": 28, "nombre": "Cafetera Hamilton Beach de Goteo 12tz", "categoria": "Electrodomesticos", "marca": "Hamilton Beach", "tienda": "Creditos Economicos", "precio": 55.00},
    
    # Climatización e Hogar
    {"id_producto": 29, "nombre": "Aire Acondicionado LG Split 12000 BTU", "categoria": "Climatizacion", "marca": "LG", "tienda": "Creditos Economicos", "precio": 469.99},
    {"id_producto": 30, "nombre": "Ventilador de Pedestal Taurus 16''", "categoria": "Climatizacion", "marca": "Taurus", "tienda": "Creditos Economicos", "precio": 45.00},
    {"id_producto": 31, "nombre": "Colchon Chaide Imperial 2 plazas", "categoria": "Hogar", "marca": "Chaide", "tienda": "Creditos Economicos", "precio": 289.99},
    {"id_producto": 32, "nombre": "Sofa Cama Plegable Microfibra", "categoria": "Hogar", "marca": "Generico", "tienda": "Creditos Economicos", "precio": 229.99},
    {"id_producto": 33, "nombre": "Juego de Comedor 4 puestos Madera", "categoria": "Hogar", "marca": "Generico", "tienda": "Creditos Economicos", "precio": 349.99},
    {"id_producto": 34, "nombre": "Escritorio Gamer Xtratech Fibra Carbono", "categoria": "Hogar", "marca": "Xtratech", "tienda": "Creditos Economicos", "precio": 119.99},
    {"id_producto": 35, "nombre": "Silla de Oficina Ergonomica Ejecutiva", "categoria": "Hogar", "marca": "Generico", "tienda": "Creditos Economicos", "precio": 79.99}
]

df_productos = pd.DataFrame(productos_data)

# 2. Definición de perfiles de consumo
# Cada perfil define:
# - afinidad_categoria: dict de categoría -> valor (positivo o negativo)
# - afinidad_marca: dict de marca -> valor (positivo o negativo)
# - presupuesto: precio de referencia para penalización
# - sensibilidad_precio: multiplicador para la penalización de precio
perfiles = {
    "Tecnologico_Gamer": {
        "afinidad_categoria": {"Tecnologia": 1.5, "TV y Audio": 1.2, "Hogar": -0.5, "Electrodomesticos": -0.8, "Climatizacion": 0.0},
        "afinidad_marca": {"Apple": 0.8, "Asus": 0.8, "Sony": 0.8, "Samsung": 0.5, "Nintendo": 0.8, "Xtratech": 0.6, "HyperX": 0.8, "LG": 0.3},
        "presupuesto": 1200.0,
        "sensibilidad_precio": 0.05
    },
    "Hogar_Familiar": {
        "afinidad_categoria": {"Electrodomesticos": 1.5, "Hogar": 1.2, "Climatizacion": 0.8, "TV y Audio": 0.6, "Tecnologia": -0.8},
        "afinidad_marca": {"Indurama": 0.8, "Mabe": 0.8, "LG": 0.7, "Samsung": 0.5, "Chaide": 0.8, "Oster": 0.6, "Apple": -1.2, "Asus": -1.0},
        "presupuesto": 600.0,
        "sensibilidad_precio": 0.4
    },
    "Estudiante_Ahorrador": {
        "afinidad_categoria": {"Tecnologia": 1.0, "Hogar": -0.2, "Electrodomesticos": -0.5, "TV y Audio": 0.0, "Climatizacion": -0.5},
        "afinidad_marca": {"Xiaomi": 0.8, "Lenovo": 0.8, "HP": 0.6, "TCL": 0.5, "Taurus": 0.6, "Apple": -1.5, "Sony": -1.0},
        "presupuesto": 250.0,
        "sensibilidad_precio": 2.0  # Penalización alta si supera presupuesto
    },
    "Fitness_EstilodeVida": {
        "afinidad_categoria": {"Tecnologia": 0.8, "Electrodomesticos": 0.8, "Hogar": 0.0, "TV y Audio": -0.5, "Climatizacion": 0.0},
        "afinidad_marca": {"Huawei": 0.8, "Oster": 0.8, "Black & Decker": 0.8, "Samsung": 0.4, "Sony": -0.4},
        "presupuesto": 400.0,
        "sensibilidad_precio": 0.6
    }
}

# Crear 35 clientes (ID 1 al 35) asignándoles un perfil
clientes = []
perfil_keys = list(perfiles.keys())
for i in range(1, 36):
    # Distribuir equitativamente los perfiles
    perfil = perfil_keys[i % len(perfil_keys)]
    clientes.append({"id_usuario": i, "perfil": perfil})

df_clientes = pd.DataFrame(clientes)

# 3. Generación de la Matriz de Utilidad / Interacciones
# Para lograr al menos 250 interacciones lógicas, haremos que cada usuario interactúe con 
# una selección de productos (entre 7 y 10 productos cada uno).
# Para que sea real, un usuario interactúa con más frecuencia con productos afines a su perfil, 
# pero también puede interactuar con algunos aleatorios (ruido).

interacciones = []
for index, cliente in df_clientes.iterrows():
    u_id = cliente["id_usuario"]
    perf_name = cliente["perfil"]
    perf_config = perfiles[perf_name]
    
    # Decidir con cuántos productos interactúa este usuario (entre 8 y 10)
    n_interacciones = random.randint(8, 10)
    
    # Ponderar la probabilidad de elegir productos según afinidad de categoría del perfil
    pesos_productos = []
    for prod in productos_data:
        cat = prod["categoria"]
        afin = perf_config["afinidad_categoria"].get(cat, 0.0)
        # Convertir la afinidad en un peso no negativo
        peso = max(0.1, 1.0 + afin)
        pesos_productos.append(peso)
        
    # Seleccionar productos únicos basados en las ponderaciones
    indices_elegidos = np.random.choice(len(productos_data), size=n_interacciones, replace=False, p=np.array(pesos_productos)/sum(pesos_productos))
    
    for idx in indices_elegidos:
        prod = productos_data[idx]
        p_id = prod["id_producto"]
        cat = prod["categoria"]
        marca = prod["marca"]
        precio = prod["precio"]
        
        # Regla sugerida para rating:
        # rating = base + afinidad categoria + afinidad marca - penalizacion precio + ruido
        
        base = 3.0
        af_cat = perf_config["afinidad_categoria"].get(cat, 0.0)
        af_marca = perf_config["afinidad_marca"].get(marca, 0.0)
        
        # Penalización precio: si el precio es mayor al presupuesto, penalizar según la sensibilidad
        presupuesto = perf_config["presupuesto"]
        sensibilidad = perf_config["sensibilidad_precio"]
        
        penalizacion_precio = 0.0
        if precio > presupuesto:
            # Penalización proporcional a cuánto se excede del presupuesto
            exceso = precio - presupuesto
            penalizacion_precio = exceso * 0.002 * sensibilidad
            
        # Ruido controlado: distribución normal con media 0 y desviación estándar 0.25
        ruido = np.random.normal(0, 0.25)
        
        # Rating final
        rating = base + af_cat + af_marca - penalizacion_precio + ruido
        
        # Limitar estrictamente entre 1 y 5
        rating = round(max(1.0, min(5.0, rating)), 2)
        
        interacciones.append({
            "id_usuario": u_id,
            "id_producto": p_id,
            "rating": rating
        })

df_interacciones = pd.DataFrame(interacciones)

# Guardar los archivos CSV en el workspace
df_productos.to_csv("productos.csv", index=False)
df_interacciones.to_csv("calificaciones.csv", index=False)
# También guardamos una tabla descriptiva de clientes para referencia
df_clientes.to_csv("clientes.csv", index=False)

print(f"Generación completa:")
print(f"- {len(df_productos)} productos guardados en 'productos.csv'")
print(f"- {len(df_clientes)} clientes guardados en 'clientes.csv'")
print(f"- {len(df_interacciones)} calificaciones (interacciones) guardadas en 'calificaciones.csv'")
print("Primeras 5 calificaciones generadas:")
print(df_interacciones.head())
