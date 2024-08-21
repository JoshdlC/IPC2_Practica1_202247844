listaAutos = []
listaClientes = []

def menuPrincipal():
    opcion = 0
    while opcion != 6:
        print("")
        print("************************")
        print("     Menu Principal      ")
        print("     Super Autos GT")
        print("************************")
        print("")
        print("************************")
        print("1. Registrar auto")
        print("2. Registrar clientes")
        print("3. Realizar compra")
        print("4. Reporte de compra")
        print("5. Datos del estudiante")
        print("6. Salir")
        print("*************************")
        print("")
        opcion = input("Seleccione una opcion:")

        #* switch(opcion) con if
        if opcion == "1":
            print("Registrar auto")
            registrarAuto()
        elif opcion == "2":
            print("Registrar clientes")
            registrarCliente()
        elif opcion == "3":
            print("")
            realizarCompra()
        elif opcion == "4":
            print("Reporte de compras")
        elif opcion == "5":
            datosEstudiante()
        elif opcion == "6":
            print("Saliendo del sistema...")
            print("")
            exit()
        elif opcion == "7":
            mostrarAutos()
        else:
            print("XXXXXXXXXXXXXXXX")
            print("Opcion no valida")
            print("XXXXXXXXXXXXXXXX")
            print("")
            
   
def registrarAuto():
    print("************************")
    print("     Registrar Auto      ")
    print("************************")
    #* ingreso de datos del auto
    placa = input("Ingrese la placa del auto: ")
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    descripcion = input("Ingrese la descripcion del auto: ")
    anio = input("Ingrese el anio del auto: ")
    if not anio.isdigit(): #* validacion de anio
        print("El año debe ser un numero")
        return
            
     #* validacion de precio unitario
    try:
        precioUnit = float(input("Ingrese el precio unitario del auto: "))
    except ValueError:
        print("El precio unitario debe ser un numero")
        return
    
    #* creacion de objeto auto
    auto = Auto(placa, marca, modelo, descripcion, anio, precioUnit)
    #* agregando auto a la lista de autos
    listaAutos.append(auto)
    print("")
    print("Auto registrado con exito!")
    print("")


def registrarCliente():
    print("")
    print("************************")
    print("     Registrar Cliente      ")
    print("************************")
    print("")
    #* ingreso de datos del cliente
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    nit = input("Ingrese el nit del cliente: ")
    if not nit.isdigit():
        print("El nit debe ser un numero")
        return
    #* creacion de objeto cliente
    cliente = Cliente(nombre, correo, nit)
    listaClientes.append(cliente)
    print("")
    print("Cliente registrado con exito!")
    print("")


def realizarCompra():
    print("")
    print("************************")
    print("     Realizar Compra      ")
    print("************************")
    print("")

    if not listaAutos or not listaClientes:

        print("")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Registre de primero aunque sea un cliente y un auto")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("")

    else:
        print ("****************************************")
        print (" ")
        nitCliente = input("Ingrese el nit del cliente: ")
        print ("")
        #! ver logica para filtrar nits
        existeCliente = False
        for cliente in listaClientes:
            if nitCliente == cliente.getNit():
                existeCliente = True
                break
        if existeCliente:  
            print ("")
            print ("Compra para el cliente: "+cliente.getNombre())
            print ("")
            print ("************* Menu Compra **************")
            print ("")
            print ("1. Agregar auto al carrito")
            print ("2. Terminar compra y facturar")
            opcionCompra = input("Seleccione una opcion:")
            if opcionCompra == "1":
                mostrarAutos()
            
            if opcionCompra == "2":
                print ("********************")
                print ("Terninando compra..")
                print ("********************")
                
                
        # print("Seleccione un auto: ")
        # #* mostrando autos
        # for auto in listaAutos:
        #     print("Placa: "+ auto.getPlaca() + ", Marca: " + auto.getMarca() + ", Modelo: " + auto.getModelo() + ", Precio: " + auto.getPrecioUnit())
        # print("")
        # print("Seleccione un cliente: ")
        # #* mostrando clientes
        # for cliente in listaClientes:
        #     print("Nombre: " + cliente.getNombre() + ", Correo: " + cliente.getCorreo() + ", Nit: " + cliente.getNit())
        # print("")
        # #* seleccion de auto y cliente

def datosEstudiante():
    print("")
    print("***************************")
    print("     Datos Estudiante    ")
    print("***************************")
    print("Nombre: Josue Samuel")
    print("Apellido: de la Cruz Medina")
    print("Carnet: 202247844")
    print("Curso: IPC2")
    print("****************************")
    print("")
    print("")
    menuPrincipal()


def mostrarAutos():
    print("")
    print("************************")
    print("     Autos Registrados      ")
    print("************************")
    
    for i, auto in enumerate(listaAutos, start=1):
        #print("#"+i) 
        print(f"{i}. Placa: {auto.getPlaca()}, Marca: {auto.getMarca()}, Modelo: {auto.getModelo()}, Descripcion: {auto.getDescripcion()}, Precio: Q{auto.getPrecioUnit()}")
        #i+=1
    print("")
    print("************************")


class Auto():
    #! clase para autos
    def __init__(self, placa, marca, modelo, descripcion, anio, precioUnit):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.anio = anio
        self.precioUnit = precioUnit

    #! getters 
    def getPlaca(self):
        return self.placa
    
    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo
    
    def getDescripcion(self):
        return self.descripcion
    
    def getAnio(self):
        return self.anio
    
    def getPrecioUnit(self):
        return self.precioUnit
    


class Cliente():
    #! clase para clientes
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit
    #! getters
    def getNombre(self):
        return self.nombre
    
    def getCorreo(self):
        return self.correo
    
    def getNit(self):
        return self.nit
    
class Compras(Cliente):
    def __init__(self, nombre, correo, nit, id, seguro):
        super().__init__(nombre, correo, nit)
        self.id = id
        self.seguro = seguro


class Main():
    menuPrincipal()