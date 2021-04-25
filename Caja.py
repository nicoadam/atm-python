import banco
from os import system, path
import time #tiempo del sistema


class Caja(object):
    
    rayas ="*"*100 #rayas
    ban = "" # inicializo la variable del objeto banco
    
  


    def __init__(self):
        try:
            self.historial = ["****ACCIONES EFECTUADAS****\n"] # titulo de la cabezera del archivo

            #path.expanduser me tra el home del usuario
            self.archivo = open(path.join(path.expanduser('~'),'Desktop/registro.txt'),'a')
            system("clear")
            print self.rayas # las rayas
            
    	    nombre = raw_input("Nombre: ")
            cuenta = raw_input("Cuenta: ")
            deposito = raw_input("Deposito: ")
            self.historial = ["****ACCIONES EFECTUADAS****\n"] # titulo de la cabezera del archivo
            self.historial.append("Cliente: " + nombre+'\n') # agregro el cliente la lista del historial
            self.historial.append("Cuenta: "+ cuenta+'\n') #agrego la cuenta en la lista
            self.historial.append("Deposito Inicial: "+ deposito+'\n\n') # agrego el deposito en la lista

            if str(nombre) != "" and str(cuenta) != "" and int(deposito) > 0: #aseguro que dijito datos
                           
                # construllo el objeto banco con los valores el cliente
                self.ban = banco.Banco(nombre,cuenta,deposito)
                #muesto el menu de opciones
                self.menu()
            else:
                print "datos incorrectos dijite datos"

        except ValueError:
            print "error en los datos \ndigite los datos corecctos" 
  



    def menu(self):
    	
        print "\n\n\n"
        print self.rayas
        print "****************Menu de opciones:*********************\n"

        try:
            opcion = raw_input("QUE DESEA Hacer:\n1-) Consultar Balance\n2-) Comprar Targeta\n3-) Hacer retiro\n4-) Depositar\n5-) Salir\n Elija un numero# ")
            if  int(opcion) == 1: #consulta de balance
                system("clear")
                self.Consultar_balance()
                self.transaccion('Consulta')
                self.menu()

            elif int(opcion) == 2: #compra de targeta
                system("clear")
                self.comprar_targeta(raw_input("cantida de recarga $..... ")) # metodo comprar_targeta
                self.transaccion('Compra')
                self.menu()

            elif int(opcion) == 3: #retiro
                system("clear")
                self.hacer_retiro(raw_input("**#Cantidad de retiro $..... ")) #metodo hacer retiro
                self.transaccion('Retiro')
                self.menu()

            elif int(opcion) == 4: #deposito
                system("clear")
                self.hacer_deposito(raw_input('$Cantidad a depositar\n.....')) #metodo hacer_reposito
                self.transaccion('Deposito')
                self.menu()

            elif int(opcion) == 5: #salir del programa
                
                for reg in self.historial:
                    self.archivo.writelines(reg) #recuperando el listado de la lista historial

                self.archivo.flush()
                self.archivo.close()
                print "bye"
                exit()    

            else:
            	system("clear")
            	print "ELIJA UNA DE LAS OPCIONES\n\n"
            	self.menu()
        except ValueError:
            print "Error Elija solo numeros"
            self.menu()



    def Consultar_balance(self):
        try:
            if self.ban.getMonto() > 0: # vefirica si el monto que 0 , si tiene balance
                print("**SU BALANCE ES DE $ " + str(self.ban.getMonto()) +" RD")
        except Exception, e:
            print ("error: " + str(e))
       
      

    def comprar_targeta(self,dinero):
        try:
            if int(dinero) > 0: # verifica que entras dinero
                self.ban.targeta(dinero) # el banco hace la transaccion
        except Exception, e:
            print ("error" + str(e))
                                 

    
    def hacer_retiro(self,dinero):
        try:
            self.ban.retiro(dinero) # llama funcion retiro de BANCO
        except Exception, e:
            print "error: " + str(e)
        
            
    def hacer_deposito(self,dinero):
        try:
            self.ban.depositar(dinero)
        except Exception, e:
            print "error: " + str(e)
   
    def transaccion(self,accion):
        try:
            self.historial.append(str(accion)+' a las '+str(time.ctime(time.time())) + "\n") # ctime convierte a string los segundo que viene de time()
        
        except Exception, e:
            print "error: " + str(e)
            self.archivo.close()
      
ca =Caja()
