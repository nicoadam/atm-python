class Banco:

    
    monto = 0 #variable que almacena el dinero el usuario
    

    def __init__(self,nombre,cuenta,deposito):
        self.monto = self.monto + int(deposito)
                

        

    def setMonto(self,dinero):
        self.monto = dinero + getMonto()

    def getMonto(self):
        return int(self.monto) #devuelve el monto total del usuario

    
    def targeta(self,dinero):
        try:
            if int(self.getMonto()) >= int(dinero): # vefirica si el balance es mayor o igual a la compra
                compra = self.getMonto() - int(dinero) # Resta lo que tiene lo qut tiene con la compra
                self.monto = compra                
                print ("*********COMPRA REALIZADA CON EXITO**********\n")           
            else:
                print ("*****NO TIENES DINERO SUFICIENTE*****")
        except Exception, e:
            print e
        else:
            print("PROCESO DE COMPRA FINALIZADO")
     
        
  

    def retiro(self,dinero):
        try:
            if self.getMonto() >= int(dinero): #vefirica si tiene dinero suficiente para retirar

                retiro = self.getMonto() - int(dinero) # disminuye el monto que tenia
                self.monto = retiro 
                print ("******RETIRO REALIZADO CON EXITO********\n")
            else:
                print ("NO TIENES DINERO SUFICIENTE PARA RETIRAR")
        except Exception, e:
            print e
        else:
            print "PROCESO DE RETIRO FINALIZADO..."
            

    def  depositar(self,dinero):
         try:
             self.monto = self.monto + int(dinero)
             print "DEPOSTIDO REALIZADO"
         except Exception , e:
             print e
         else:
             print "****PROCESO DEPOSTIDO REALIZADO*****"
       
      
  
