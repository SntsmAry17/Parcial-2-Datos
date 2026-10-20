from collections import deque

# A. Gestión de solicitudes mediante FIFO
# Una deque permite agregar al final y atender desde el inicio de manera eficiente.
solicitudes = deque()


# B. Registro de despachos mediante LIFO
# Una lista funciona como pila: append agrega arriba y pop retira el último.
despachos = []


def cargar_datos_iniciales():
    solicitudes.extend([
        {"codigo": "P001", "cliente": "Nicole Estefania"},
        {"codigo": "P002", "cliente": "María José"},
        {"codigo": "P003", "cliente": "Estudiante 3"},
    ])

    despachos.extend([
        {"operacion": "D001", "producto": "PROD001"},
        {"operacion": "D002", "producto": "PROD002"},
        {"operacion": "D003", "producto": "PROD003"},
    ])


def registrar_solicitud():
    # 1. Registrar solicitud con código y nombre del cliente/estudiante.
    codigo = input("Código de solicitud: ").strip()
    cliente = input("Nombre del cliente/estudiante: ").strip()
    if not codigo or not cliente:
        print("El código y el nombre son obligatorios.")
        return

    # 2. Agregar cada solicitud al final de la cola FIFO.
    solicitudes.append({"codigo": codigo, "cliente": cliente})
    print("Solicitud agregada a la cola.")


def atender_solicitud():
    # 3 y 5. Atender la solicitud más antigua; controlar cola vacía.
    if not solicitudes:
        print("No hay solicitudes pendientes para atender.")
        return
    solicitud = solicitudes.popleft()
    print(f"Solicitud atendida: {solicitud['codigo']} - {solicitud['cliente']}")


def mostrar_solicitudes():
    # 4. Mostrar pendientes en el orden en que serán atendidas.
    if not solicitudes:
        print("No hay solicitudes pendientes.")
        return
    print("\nSolicitudes pendientes (primero en atenderse):")
    for numero, solicitud in enumerate(solicitudes, start=1):
        print(f"{numero}. {solicitud['codigo']} - {solicitud['cliente']}")


def registrar_despacho():
    # 6. Registrar despacho con código de operación y código de producto.
    operacion = input("Código de operación: ").strip()
    producto = input("Código de producto: ").strip()
    if not operacion or not producto:
        print("El código de operación y el de producto son obligatorios.")
        return

    # 7. Agregar el despacho a la cima de la pila LIFO.
    despachos.append({"operacion": operacion, "producto": producto})
    print("Despacho registrado en la pila.")


def mostrar_despachos():
    # 8. Consultar despachos sin retirarlos; se muestra primero el más reciente.
    if not despachos:
        print("No hay despachos registrados.")
        return
    print("\nDespachos registrados (más reciente primero):")
    for numero, despacho in enumerate(reversed(despachos), start=1):
        print(f"{numero}. {despacho['operacion']} - Producto: {despacho['producto']}")


def retirar_despacho():
    # 9 y 10. Retirar el último registro; si no hay elementos, informar.
    if not despachos:
        print("No se puede retirar: la pila de despachos está vacía.")
        return
    despacho = despachos.pop()
    print(
        f"Registro retirado: {despacho['operacion']} - "
        f"Producto: {despacho['producto']}"
    )
    print("Esta corrección del registro no devuelve físicamente el producto al almacén.")

