class Cliente:
    def __init__(self, nombre=str):
        self.nombre = nombre

    #
    def hacerPedido(self, pedidoTotal=list, domicilio=False):
        print(f"Señor {self.nombre}, acaba de ordenar lo siguiente:")
        # Si son mas de dos pedidos, se mostrara primero el primero y asi sucesivamente
        for pedidos_individuales in pedidoTotal:

            texto = f"""
            Galleta: {pedidos_individuales[0]}
            Aderezo: {pedidos_individuales[1]}
            Topping: {pedidos_individuales[2]}
            Precio: {pedidos_individuales[3]}
            """
            print(texto)

        print("Pedido realizado con éxito.")
        # Se observa si es a domicilio o no, si es a domicilio, se imprime con atributos de direccion y telefono, caso contrario, solo con mesa
        if domicilio:
            print(
                f'El pedido será enviado a la dirección {self.direccion}, llamando al numero {self.telefono}')
        else:
            print(
                f'El pedido estará disponible para ser recogido en la mesa {self.numeroMesa}.')
        return True

# Clase mesa heredando el nombre del cliente


class Mesa(Cliente):
    def __init__(self, nombre=str, numeroMesa=int):
        super().__init__(nombre)
        self.numeroMesa = numeroMesa

# Clase domicilio heredando el nombre del cliente


class Domicilio(Cliente):
    def __init__(self, nombre=str, direccion=str, telefono=int):
        super().__init__(nombre)
        self.direccion = direccion
        self.telefono = telefono

# Se retorna el costo total de la compra


class OrdenDeCompra:
    def __init__(self, pedido=list):
        self.pedido = pedido
        self.precio = 0
        self.costoDomicilio = 1000  # Precio de domicilio por defecto

    def calcularPrecio(self, domicilio=False):
        total = 0
        # Averiguando el precio de cada pedido
        for precio_pedido in self.pedido:
            total += precio_pedido[3]
        # Si es a domicilio, se cobra el valor extra
        if domicilio:
            self.precio = total + self.costoDomicilio
        else:
            self.precio = total
        return self.precio

# Imprimiendo el recibo de pago


class ReciboDePago:
    def __init__(self, cliente=str, orden=list, costoTotal=float):
        self.cliente = cliente
        self.orden = orden
        self.costoTotal = costoTotal

    def imprimirRecibo(self):

        recibo = f"""
        ******************************
            Señor {self.cliente}
            Su orden es: {self.orden}
            El costo total es: ${self.costoTotal}
            ¡Gracias por su compra!
        ******************************
        """
        print(recibo)


# Ejemplo de uso del sistema:

nombre_cliente = input("Ingrese su nombre: ")
es_Domicilio = input("¿Es domicilio?  (s/n): ").lower() == "s"

if es_Domicilio:
    direccion_cliente = input("Ingrese su direccion: ")
    telefono_cliente = input("Ingrese su telefono: ")
    cliente1 = Domicilio(nombre_cliente, direccion_cliente, telefono_cliente)
else:
    numero_mesa = int(input("Ingresa el nomero de mesa: "))
    cliente1 = Mesa(nombre_cliente, numero_mesa)


total_pedido = []

while True:
    galleta_a_ordenar = input(
        "Ingrese el nombre de la galleta (o 'fin' para finalizar): ")

    if galleta_a_ordenar.lower() == "fin":
        break

        # Solicitar detalles del producto
    aderezo_galleta = input("Ingrese el aderezo del producto: ")
    topping_galleta = input("Ingrese el topping del producto: ")
    precio_galleta = float(input("Ingrese el precio del producto: "))

    # Crear un objeto Galletas con los detalles del producto

    pedido_actual = (galleta_a_ordenar, aderezo_galleta,
                     topping_galleta, precio_galleta)
    total_pedido.append(pedido_actual)


cliente1.hacerPedido(total_pedido, es_Domicilio)
orden = OrdenDeCompra(total_pedido)

costo_final = orden.calcularPrecio(es_Domicilio)

recibo = ReciboDePago(nombre_cliente, total_pedido, costo_final)
recibo.imprimirRecibo()
