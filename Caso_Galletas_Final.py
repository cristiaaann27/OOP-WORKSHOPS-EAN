
# """
# El programa es un software de gestión para una panadería llamada SoftCookie,
# que permite a los usuarios agregar panaderos y productos, enviar pedidos para hornear
# y eliminar productos y panaderos existentes. El programa utiliza
# la programación orientada a objetos y utiliza la biblioteca threading para manejar
# múltiples procesos en paralelo.

# Este es un programa de simulación de una panadería, que permite agregar productos y contratar
# panaderos para prepararlos. Los clientes pueden hacer un pedido de un producto y el sistema
# selecciona el panadero disponible que haya trabajado menos recientemente para hacerlo.

# El código contiene tres clases principales: Panaderia, Pedido y Panadero, además de una clase
# para los productos. La clase Panaderia tiene métodos para agregar y quitar panaderos y productos,
# hacer pedidos, y manejar la terminación del trabajo de los panaderos. La clase Pedido almacena
# la lista de productos que componen el pedido y asigna el pedido al panadero disponible que haya
# trabajado menos recientemente. La clase Panadero tiene métodos para preparar un producto,
# iniciar y terminar el trabajo y una variable que indica su disponibilidad.

# La clase Main se encarga de ejecutar el programa.
# Permite crear una nueva panadería y ofrece varias opciones de gestión,
# como agregar un panadero o un producto, enviar un producto a la preparación,
# despedir un panadero o quitar un producto.

# El programa utiliza la biblioteca threading para permitir la ejecución simultánea de
# múltiples hilos de trabajo, en este caso los panaderos preparando los productos.

# En general, el código está bien estructurado y los métodos tienen nombres descriptivos,
# lo que hace que sea fácil de entender.

# Los usuarios pueden interactuar con el programa
# a través de un menú de opciones que se muestra en la consola y seleccionando la opción
# deseada mediante el ingreso de números.

# @author: David
# """


""" Se importan los módulos timeel cual nos proporciona funciones para trabajar co el tiempo y threading que nos permite ejecutar varias tareas
a la vez en un programa. """

import time
import threading

# Se define la clase Panaderia que contiene el nombre de la panadería, una lista de productos y una lista de panaderos en vacío.


class Panaderia:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos = []
        self.panaderos = []
    """
    La función hacer_pedido(pedido) de la clase Panaderia simula el proceso de hacer un pedido. La función verifica si hay panaderos disponibles,
    si no hay ninguno disponible, pregunta al usuario si quiere esperar o volver al menú principal. Si el usuario decide esperar,
    se espera un minuto y se vuelve a verificar si hay panaderos disponibles. Si hay un panadero disponible, 
    se asigna el pedido al panadero.
    """

    def hacerPedido(self, pedido: str):
        panaderos_disponibles = [
            panadero for panadero in self.panaderos if panadero.disponible]
        while not panaderos_disponibles:
            print("Todos los panaderos están ocupados. ¿Qué desea hacer?\n")
            try:
                respuesta = int(input(
                    "1. Esperar a que se desocupe un panadero\n2. Volver al menu principal?: "))

            except ValueError:
                print("Opcion no valida, ingrese correctamente la opcion.")
            else:
                if respuesta == 1:
                    print("Esperando 1 minuto...")
                    time.sleep(60)
                    panaderos_disponibles = [
                        panadero for panadero in self.panaderos if panadero.disponible]
                elif respuesta == 2:
                    return
                else:
                    print("Opcion no valida")
        pedido.asignarPedido(panaderos_disponibles)

    # La función terminar_pedidos() de la clase Panaderia termina todos los pedidos para cada panadero.

    def terminarPedidos(self):
        for panadero in self.panaderos:
            panadero.terminarTrabajo()

    # La función contratar_panadero(nombre) de la clase Panaderia crea un nuevo panadero con el nombre dado
    # y lo agrega a la lista de panaderos.

    def contratarPanadero(self, nombre: str):
        nuevo_panadero = Panadero(nombre)
        self.panaderos.append(nuevo_panadero)
        print(f"El panadero {nombre} ha sido agregado con éxito")
    # El metodo mostrarPanaderos, sirve para imprimir todos los panaderos actuales.

    def mostrarPanaderos(self):
        print(f"Esta es la lista con los nombres de los panaderos: ")
        for panaderos_actuales in self.panaderos:
            print(panaderos_actuales.__str__())
        return len(self.panaderos)

    # La función despedir_panadero(nombre_panadero) de la clase Panaderia busca el panadero con el nombre dado y
    # lo elimina de la lista de panaderos.

    def despedirPanadero(self, nombre_panadero: str):
        for panadero in self.panaderos:
            if panadero.nombre == nombre_panadero:
                self.panaderos.remove(panadero)
                print(f"El panadero {nombre_panadero} ha sido removido")
                return
        print(f"No se encontró al panadero {nombre_panadero}")

    # Recibe el nombre y el tiempo de preparación de un producto y crea una nueva instancia de la clase Producto con esos valores.
    # Agrega el nuevo producto a la lista de productos de la panadería.
    def añadirProducto(self, nombre: str, tiempo_preparacion: float):
        nuevo_producto = Producto(nombre, tiempo_preparacion)
        self.productos.append(nuevo_producto)
        print(
            f"El producto {nombre} se ha añadido a la lista con un tiempo de preparacion medio de {tiempo_preparacion} Minutos.")

    # Metodo que imprime cada producto con su tiempo de preparación y retorna la cantidad de productos que hay actualmente.
    def productosActuales(self):
        print(f"Esta es la lista con los nombres de los Productos: ")
        for productos_actuales in self.productos:
            print(productos_actuales.__str__())
        return len(self.productos)

    # Recibe el nombre de un producto y busca en la lista de productos de la panadería el producto con ese nombre.
    # Si lo encuentra, lo elimina de la lista. Si no lo encuentra, muestra un mensaje de error.
    def quitarProducto(self, nombre_producto: str):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                self.productos.remove(producto)
                print(
                    f"El producto {nombre_producto} se ha removido de la lista")
                return
        print(f"No se encontró en la lista al producto: {nombre_producto}")

# Se crea la clase pedido la cual establece la lista de productos en vacío y el panadero asignado como None


class Pedido:
    def __init__(self):
        self.productos = []
        self.panadero_asignado = None

    # Recibe una lista de panaderos disponibles y asigna el pedido al panadero que haya trabajado menos recientemente.
    # Llama al método comenzar_trabajo del panadero asignado con el primer producto de la lista de productos del pedido.

    def asignarPedido(self, panaderos_disponibles: list):
        panadero_elegido = min(panaderos_disponibles,
                               key=lambda panadero: panadero.trabajoReciente)
        if panadero_elegido.disponible:
            self.panadero_asignado = panadero_elegido
            panadero_elegido.comenzarTrabajo(self.productos[0])

    # Recibe un producto y lo agrega a la lista de productos del pedido.

    def agregarProducto(self, producto: str):
        self.productos.append(producto)

# Inicializa una nueva instancia de la clase Panadero. Recibe el nombre del panadero y establece su disponibilidad
# como True, su tiempo de trabajo reciente en 0 y su hilo como None


class Panadero:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.disponible = True
        self.trabajoReciente = 0
        self.thread = None

    def __str__(self):
        return f"Nombre: {self.nombre}"

    # Recibe un producto y lo prepara durante un tiempo determinado. Establece la disponibilidad del panadero como
    # False mientras trabaja en el producto. Cuando termina, actualiza el tiempo de trabajo reciente del panadero
    # y llama al método terminar_trabajo.

    def prepararProducto(self, producto: str):
        self.disponible = False
        tiempo_preparacion = producto.tiempo_preparacion
        print(f"{self.nombre} está preparando un {producto.nombre} y tardará {tiempo_preparacion} minutos.\n")
        # Esta multiplicacion es para simplificar el tiempo de ejecucion, la espera puede ser de horas.
        time.sleep(tiempo_preparacion*0.1)
        print("\n// Su pedido está listo.//")
        self.trabajoReciente += tiempo_preparacion
        self.terminarTrabajo()

    # Recibe un producto y crea un nuevo hilo para prepararlo. Llama al método preparar_producto del panadero en ese hilo.

    def comenzarTrabajo(self, producto: str):
        self.thread = threading.Thread(
            target=self.prepararProducto, args=(producto,))
        self.thread.start()

    # Termina el trabajo y establece como True la disponibilidad del panadero.

    def terminarTrabajo(self):
        self.disponible = True

# Se define la clase producto que contiene el nombre del producto y su tiempo de preparacion.


class Producto:
    def __init__(self, nombre: str, tiempo_preparacion: float):
        self.nombre = nombre
        self.tiempo_preparacion = tiempo_preparacion

    # Este metodo se usa para retornar un string, para cuando se vaya a imprimir la lista de productos, no se imprima la direccion en memoria.
    def __str__(self):
        return f"Nombre del producto: {self.nombre}  Tiempo de preparación: {self.tiempo_preparacion} Minutos."

# Se crea la clase Main la cual muestra en pantalla un mensaje de bienvenida y contiene un metodo llamado run.


class Main:
    def __init__(self):
        print("Bienvenido al Software de gestion de panaderia SoftCookie")
        self.run()

    """
    Muestra al usuario un menú con opciones para agregar panaderos, agregar productos, hacer pedidos,
    despedir panaderos, quitar productos y salir del programa. Dependiendo de la opción que el usuario seleccione,
    se llamará al método correspondiente de la clase Panaderia.
    """

    def run(self):
        if 'panaderia' in locals():
            print("La panadería ya existe.")
        else:
            print(
                "Para iniciar el software de gestion de tu panaderia, primero debes crear una panaderia")
            nombre_panaderia = input(
                "¿Qué nombre tiene tu panadería?\nEscribe aqui: ").capitalize()
            panaderia = Panaderia(nombre_panaderia)

        while True:
            print(f"""
                    ¡Bienvenido panaderia: {nombre_panaderia}!
            A continuación, presentamos lo que puedes hacer con SoftCookie

            1. Agregar un panadero.
            2. Agregar un producto.
            3. Mandar hornear un producto.
            4. Despedir un panadero.
            5. Quitar un producto.
            6. Salir del programa 

            """)
            # Excepcion para manejar los errores de ValueError
            try:
                opcion = int(input("Por favor, ingrese la opción deseada: "))

                # Opción 1, agregar panadero.
                if opcion == 1:
                    nombre_panadero = input(
                        "Por favor, ingrese el nombre del panadero: ").capitalize()
                    panaderia.contratarPanadero(nombre_panadero)

                # Opción 2, agregar producto, con una excepción para manejar errores de digitación.
                elif opcion == 2:
                    nombre_producto = input(
                        "Por favor, ingrese el nombre del producto: ").capitalize()

                    while True:
                        try:
                            tiempo_producto = float(
                                input("Por favor, ingrese el tiempo medio de preparación del producto, en minutos: "))
                            if tiempo_producto <= 0:
                                print(
                                    "Numero incorrecto, ingresa valor nuevamente.")
                            else:
                                panaderia.añadirProducto(
                                    nombre_producto, tiempo_producto)
                                break
                        except ValueError:
                            print(
                                "Valor incorrecto del tiempo, ingreselo nuevamente.")

                # Opción 3, ordenar un producto, con la limitante de que al principio nos pide un minimo de 3 productos agregados, para ordenar.
                elif opcion == 3:
                    if panaderia.productosActuales() <= 3:
                        print("Agrega mas productos para tener un menú.")
                    else:
                        nuevo_pedido = Pedido()

                        while True:
                            nombre_producto = input(
                                "Por favor, ingrese el nombre del producto que se mandará a hornear: ").capitalize()

                            producto = next(
                                (p for p in panaderia.productos if p.nombre == nombre_producto), None)
                            if producto is None:
                                print(
                                    f"El producto {nombre_producto} no existe en la lista de productos.")
                            else:
                                nuevo_pedido.agregarProducto(producto)
                                break
                        panaderia.hacerPedido(nuevo_pedido)

                # Opción 4, despedir panaderos, con la limitante de tener algun panadero trabajando.
                elif opcion == 4:
                    if panaderia.mostrarPanaderos() == 0:
                        print("No hay panaderos para despedir.")
                    else:
                        nombre_panadero = input(
                            "Por favor, ingrese el nombre del panadero a despedir: ").capitalize()
                        panaderia.despedirPanadero(nombre_panadero)

                # Opción 5, quitar productos, con la limitante de tener algun producto en la lista.
                elif opcion == 5:
                    if panaderia.productosActuales() == 0:
                        print("No hay productos para quitar.")
                    else:
                        nombre_producto = input(
                            "Por favor, ingrese el nombre del producto a quitar: ").capitalize()
                        panaderia.quitarProducto(nombre_producto)
                # Opción 6, fin del programa.
                elif opcion == 6:
                    print("Gracias por utilizar SoftCookie. ¡Hasta la próxima!")
                    break
                else:
                    print("Opcion no disponible.")
            except ValueError:
                print("Valor no valido, ingrese los datos correctamente.")


# """
#  +----------------------------------+                   +--------------------------------------+
# |            Panaderia             |                   |             Panadero                |
# +-----------------------+----------+                   +--------------------------------------+
# | - productos           |          |                   | - nombre                             |
# | - panaderos           |          |                   | - disponible                        |
# |                                  |+----------------->| - trabajo_reciente                  |
# | + hacer_pedido()      |          |                   | + preparar_producto()                |
# | + terminar_pedidos()  |          |                   | + comenzar_trabajo()                 |
# |                        |          |                   | + terminar_trabajo()                 |
# +----------------------------------+                   +-------------------/---*--------------+
#                         |                                                  /   /
#                         | <------------------------------------------------/   /
#                         |                                                      /
#                 +-------*-------+                                   +----------/--+
#                 |    Producto   |<----------------------------------|   Pedido   |
#                 +---------------+                                   +------------+
#                 | - nombre      |                                   | - productos |
#                 | - tiempo_preparacion |                            | - panadero_asignado |
#                 +---------------+                                   | +asignar_pedido() |
#                 +------------+
"""
Correciones del codigo
1. Nombramos bien los metodos.
2. Agregamos excepciones cuando se tiene que ingresar un valor en numero, para que el programa no falle.
3. Agregamos un nuevo metodo para mostrar los panaderos.
4. Agregamos un nuevo metodo para mostrar los productos.
5. Agregamos un sistema de condiciones para manejar bien cuando no hay productos o panaderos.
6. Comentamos bien el código.
7. Especificar el tipo de dato en los atributos de los métodos.
"""

if __name__ == '__main__':
    Main()
