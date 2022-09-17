from re import S
from typing import get_origin


class Package():
    def __init__(self, id, origin, destination, weight):
        self.__Id = id 
        self.__Origin = origin
        self.__Destination = destination
        self.__Weight = weight

    #Getters
    def get_Id(self):
        return self.__Id
        
    def get_Origin(self):
        return self.__Origin

    def get_Destination(self):
        return self.__Destination

    def get_Weight(self):
        return self.__Weight
        
    #Setters 
    def set_Id(self, myId):
            self.__Id = myId
        
    def set_Origin(self, myO):
        self.__Origin = myO

    def set_Destination(self, myDes):
        self.__Destination = myDes

    def set_Weight(self, myW):
        self.__Weight = myW
    #Impresion en pantalla del objeto
    def __str__(self):
        return( f"******************************\n" +
                f"Id------: {self.__Id}\n" +
                f"Origen--: {self.__Origin}\n" +
                f"Destino-: {self.__Destination}\n" +
                f"Peso(Kg): {self.__Weight}\n")
    