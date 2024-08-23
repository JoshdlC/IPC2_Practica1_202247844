from datetime import date

listaAutos = []
listaClientes = []
listaCompras = []
#carritoCompras = []
idCompraGlobal = 1
totalGeneral = 0
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
            mostrarCompras()
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
    if placa in [auto.getPlaca() for auto in listaAutos]: #* validacion de placa unica
        print ("")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print ("   La placa ya existe, ingrese otra placa")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        return
    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    descripcion = input("Ingrese la descripcion del auto: ")
    anio = input("Ingrese el anio del auto: ")
    if not anio.isdigit(): #* validacion de anio
        print("El año debe ser un numero")
        return
    if anio < "1985" or anio > "2025":
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("El año debe estar entre 1985 y 2025")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
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
    if nit in [cliente.getNit() for cliente in listaClientes]:
        print ("")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print ("   El nit ya existe, ingrese otro nit")
        print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    #* creacion de objeto cliente
    cliente = Cliente(nombre, correo, nit)
    listaClientes.append(cliente)
    print("")
    print("Cliente registrado con exito!")
    print("")



def realizarCompra():

    global idCompraGlobal
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
        clienteSeleccionado = None
        print ("")
        #! ver logica para filtrar nits
        existeCliente = False
        for cliente in listaClientes:
            if nitCliente == cliente.getNit():
                clienteSeleccionado = cliente
                break
        if clienteSeleccionado:  
            print ("")
            print ("Compra para el cliente: "+cliente.getNombre())
            print ("")
            while True:
                
                print ("***************************")
                print ("     Menu de Compra    ")
                print ("***************************")
                print ("")
                print ("1. Agregar auto al carrito")
                print ("2. Terminar compra y facturar")
                opcionCompra = input("Seleccione una opcion:")
                #* si se agrega un auto al carrito
                if opcionCompra == "1":
                    autoSeleccionado = mostrarAutos()

                    if autoSeleccionado: #* si se selecciono un auto
                        #* agregando auto al carrito
                        clienteSeleccionado.agregarAlCarrito(autoSeleccionado)
                        listaAutos.remove(autoSeleccionado)

                        #* mostrando auto seleccionado
                        print(f"Auto {autoSeleccionado.getMarca()} {autoSeleccionado.getModelo()} agregado al carrito.") 
                        print ("")                      
                        # print ("")
                        # print ("Desea agregar mas autos al carrito?")
                        # print ("1. Si")
                        # print ("2. No")
                        # print ("")
                        # opcionCarrito = input("Seleccione una opcion:")

                elif opcionCompra == "2":

                    if clienteSeleccionado.carritoCompras:
                        #idCompra = len(listaCompras) + 1 #* id de compra
                        # seguroFlag = False
                        print ("")
                        print ("Desea agregar un seguro a su(s) auto(s)?  (S/N)")
                        print ("")
                        opcionSeguro = input("Ingrese una letra:").strip().lower() == 's'
                        compra = Compras(idCompraGlobal, clienteSeleccionado, clienteSeleccionado.carritoCompras, opcionSeguro)

                        # if opcionSeguro == "1":
                        #     seguroFlag = True
                        # elif opcionSeguro == "2":
                        #     print ("")
                        #     print ("*********************************")
                        #     print ("Compra realizada con exito")
                        #     print ("*********************************")
                        #     print ("")      
                        # else:
                        #     print ("")
                        #     print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                        #     print ("Opcion no valida")
                        #     print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                        #     print ("")

                        #nuevaCompra = Compras(id=idCompra, cliente=clienteSeleccionado, autos=clienteSeleccionado.carritoCompras, seguro=seguroFlag)
                        idCompraGlobal += 1

                        listaCompras.append(compra)
                        print ("********************")
                        print ("Autos en el carrito: ")
                        print ("********************")

                        clienteSeleccionado.mostrarCarrito()
  
                        print ("")
                        print ("********************")
                        print ("Terminando compra..")
                        print ("********************")
                    else:
                        print ("")
                        print ("*********************************")
                        print ("No hay autos en el carrito")
                        print ("*********************************")
                    break
                
                else :
                    print ("")
                    print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    print ("Opcion no valida")
                    print ("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    print ("")
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



def mostrarCompras():
    hoy = date.today()
    dia = hoy.strftime("%d/%m/%Y")
    print ("***************************")	
    print ("     Reporte de Compras    ")
    print ("***************************")
    print ("")

    if not listaCompras:
        print ("*********************************")
        print ("No hay compras registradas")
        print ("*********************************")
        print ("")
        return
    else: 
        print ("===================================================================")
        print ("                        Super Autos GT")
        print ("===================================================================")
        print ("")
        print ("Fecha: ", dia)
        print ("Ciudad de Guatemala, Guatemala")	

        for compra in listaCompras:
            compra.mostrarCompra()
            print ("")
            print ("===================================================================== ")
            print ("")

        #print ("===========================================================")
        print ("")
        print ("Total general de ventas: Q", totalGeneral)



def datosEstudiante():
    print("")
    print("***************************")
    print("     Datos Estudiante    ")
    print("***************************")
    print("Nombres: Josue Samuel")
    print("Apellidos: de la Cruz Medina")
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
    print("")
    print("Seleccione un auto")
    print ("Ingrese 0 para regresar al menu principal:")
    print ("")
    #print("Id \t Placa \t\t Marca \t Modelo \t Descrip. \t Precio")
    print("------------------------------------------------------------------------------")

    for i, auto in enumerate(listaAutos, start=1):
        #print("#"+i) 
        print(f"{i}. \n Placa: {auto.getPlaca()} \n Marca: {auto.getMarca()} \n Modelo: {auto.getModelo()} \n Descripción: {auto.getDescripcion()} \t Precio: Q{auto.getPrecioUnit()}")
        #i+=1
    
    print("------------------------------------------------------------------------------")
    print ("")

    opcionAuto = input("Seleccione un auto: ")

    #* validacion de opcion
    if not opcionAuto.isdigit() or int(opcionAuto) <= 0 or int(opcionAuto) > len(listaAutos):
        print("La opcion debe ser un numero")
        return
    if opcionAuto == "0":
        print("No se selecciono ningun auto, regresando al menu principal")
        return
    
    opcionAuto = int(opcionAuto)

    autoSeleccionado = listaAutos[opcionAuto - 1]
    return autoSeleccionado




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
        self.carritoCompras = []
    #! getters
    def getNombre(self):
        return self.nombre
    
    def getCorreo(self):
        return self.correo
    
    def getNit(self):
        return self.nit
    
    def agregarAlCarrito(self, auto):
        self.carritoCompras.append(auto)

    def mostrarCarrito(self):
        for auto in self.carritoCompras:
            print(f"Placa: {auto.getPlaca()}, Marca: {auto.getMarca()}, Modelo: {auto.getModelo()}, Descripcion: {auto.getDescripcion()}, Precio: Q{auto.getPrecioUnit()}")
    


class Compras():
    def __init__(self, id, cliente, autos, seguro=None):
        self.id = id
        self.cliente = cliente
        self.autos = autos
        self.seguro = seguro
        self.costoTotal = self.calcularCostoTotal() #* calculando costo total

    def calcularCostoTotal(self):
        total = 0
        for auto in self.autos:
            precio = auto.getPrecioUnit()
            if self.seguro:
                precio *= 1.15
            total += precio
        return total

    def mostrarCompra(self):
        global totalGeneral 
        print("---------------------------------------------------------------------")
        print(f"Compra ID: {self.id}")
        print(f"Cliente: {self.cliente.getNombre()}")
        print(f"Correo cliente: {self.cliente.getCorreo()}")
        print("")
        print(f"Seguro aplicado: {'Sí' if self.seguro else 'No'}")
        print("")
        print("Auto(s) comprado(s):")
        print("Placa \t\t Marca \t Modelo \t Descrip. \t Precio")
        print("---------------------------------------------------------------------")
        for auto in self.autos:
            print(f"{auto.getPlaca()} \t {auto.getMarca()} \t {auto.getModelo()} \t {auto.getDescripcion()} \t Q{auto.getPrecioUnit()}")
            totalGeneral = auto.getPrecioUnit() + totalGeneral
        print("---------------------------------------------------------------------")
        print(f"\t \t \t \t \t  Costo total: Q{self.costoTotal:.2f}")


        

    

#* ejecucion del programa
class Main():
    menuPrincipal()