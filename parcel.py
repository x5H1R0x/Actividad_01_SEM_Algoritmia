from email.policy import default
from os import system
import pickle
import package

class Node:             # Clase Nodo
    def __init__(self, myData, next):
        self.__Data = myData
        self.__Next = next

    def showNode(self):
        print(self.__Data)
    
    def getData(self):
        return self.__Data

    def setNext(self, Value):
        self.__Next = Value

    def getNext(self):
        return self.__Next
    
class Parcel:             # Clase paqueteria (Lista)
    def __init__(self):
        self.First = None
    
    def addItem(self, Value):
        myN = Node(Value, None)
        if self.First == None:
            self.First = myN

        else:
            myN.setNext(self.First)
            self.First = myN

    def saveList(self):    
        if ls.First != None: 
            file = open('Paquetes.txt', 'w')              
            aux = self.First
            while aux != None:
                file.write(aux.getData().get_Id())  
                file.write("\n")
                file.write(aux.getData().get_Origin())
                file.write("\n")
                file.write(aux.getData().get_Destination())
                file.write("\n")
                file.write(aux.getData().get_Weight())
                file.write("\n")  
                aux = aux.getNext()
            file.close()
            print("Archivo Guardado correctamente...")
        else:
            print("La lista esta vacia...")  
    
    def loadList(self):
        file = open("Paquetes.txt", "r")
        i = 0
        aux = package.Package(0, "","", 0)
        for line in file:
            if i == 0:
                myId = line.rstrip()
            if i == 1:
                myOri = line.rstrip()
            if i == 2:
                myDet = line.rstrip()
            if i == 3:
                 myW = line.rstrip()
            i += 1
            if i == 4:
                aux = package.Package(myId, myOri,myDet, myW)
                self.addItem(aux)
                i = 0

    def deleteItem(self):
        if self.First != None:    
            aux = self.First
            self.First = aux.getNext()
            aux.__Next = None
            aux = None            
            print("Eliminado con exito...\n")        
        else:
            print("La lista esta vacia...")        
    
    def showItems(self):
        print("----Lista de paquetes----")
        if self.First != None:    
            aux = self.First
            while aux != None:
                aux.showNode()
                aux = aux.getNext()       
        else:
            print("La lista esta vacia...")
        input("ENTER para continuar.")
        
def isNum(myNum):
    try:
        int(myNum)
        return True
    except ValueError:
        return False

def mainMenu():
        print("....MENU....")
        print("1.- Agregar al inicio.")
        print("2.- Eliminar al inicio.")
        print("3.- Mostrar.")
        print("4.- Guardar Registro.")
        print("5.- Cargar Registro")
        print("0.- Salir.")
        print("Ingrese una opcion... ")

if __name__ == "__main__":
    ls = Parcel()   
    while(True):
        system("cls")
        mainMenu()
        num = input("\tEleccion: ") 
        if num == "1":
            myPack = package.Package(0, "","", 0) 
            myNum = "s"
        
            while(isNum(myNum) == False):
                myNum = input("Ingrese el codigo del paquete: ")
                if(isNum(myNum)):
                    myPack.set_Id(myNum)
                else:
                    print("No se detecta numero valido...\n")
                    print("Intente de nuevo...\n")
                    input("Presione Enter para continuar...\n")
            
            myNum = input("Ingrese el origen del paquete: ")
            myPack.set_Origin(myNum)
            myNum = input("Ingrese el destino del paquete: ")
            myPack.set_Destination(myNum)
            
            myNum = "s"
            while(isNum(myNum) == False):
                myNum = input("Ingrese el peso del paquete (Kg): ")
                if(isNum(myNum)):
                    myPack.set_Weight(myNum)
                else:
                    print("No se detecta numero valido...\n")
                    print("Intente de nuevo...\n")
                    input("Presione Enter para continuar...\n")
            
            myNode = Node(myPack, None)
            ls.addItem(myPack)
            print(myPack)
            print("Ingresado con exito...\n")
            input("Presione Enter para continuar...\n")
            
        if num == "2":
            ls.deleteItem()
            input("ENTER para continuar...\n")

        if num == "3":
            system("cls")
            ls.showItems()
        
        if num == "4":
            ls.saveList()
            input("Presione Enter para continuar...\n")

        if num == "5":
            ls.loadList()
            print("Se cargo correctamente la lista\n")
        
        if num == "0":
            print("Saliendo del sistema...")
            print("Hasta la proxima. ")
            
            exit()
        
        
