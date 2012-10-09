import random
from sys import argv
from numpy import*
from random import uniform
from random import randint
import os

class neurona(object):

  def __init__(self,cantidadEntradas=0): 
    self.cantidadEntradas=cantidadEntradas
    #tamano del vector de pesos	
    self.num=3
         
  def inicializaPesos(self):

    #inicializo los pesos	
    pesos=zeros(self.num)
    for i in range(self.num):
	pesos[i]=(random.uniform(-1,1))
    print "PESOS INICIALES: \n",pesos ,"\n"       
    return pesos
   
  def obtenerEntradas(self,pesos):
    #vector de entradas	
    entrada=zeros(2)
    vectorEntradas=zeros([self.cantidadEntradas,self.num],float)
    #vector de salidas deseadas
    salidaDeseada=zeros(self.cantidadEntradas)
	
    #abro los archivos
    puntosx=open("puntosx.txt","w")     
    puntosy=open("puntosy.txt","w")     
    salidaObtenida=open("salidasObtenidas.txt","w")
    puntos=open("puntos.txt","w")
    salida_deseada=open("salidasDeseadas.txt","w")      
 
    for x in range(self.cantidadEntradas):
      for j in range(2):
        entrada[j]=(random.uniform(-1,1))
	vectorEntradas[x][j]=entrada[j]
      entraday=append(entrada,-1)
      vectorEntradas[x][2]=-1
      #calculo la salida mediante la funcion :funcionActivacion
      salida=self.funcionActivacion(entraday,pesos)
      salidaDeseada=self.calcularSalidaDeseada(entraday,pesos)
      salida_deseada.write(str(salidaDeseada)+"\n")
      puntos.write(str(entrada[0])+" "+str(entrada[1])+" "+str(salida)+"\n")
      puntosx.write(str(entrada[0])+"\n")
      puntosy.write(str(entrada[1])+"\n")
      salidaObtenida.write(str(salida)+"\n")
	
    #cierro los archivos
    puntos.close
    puntosx.close
    puntosy.close
    salidaObtenida.close
    salida_deseada.close
    return vectorEntradas
		      	       
  def comparar(self,entradas,pesos,factorAprendizaje):
    
    #guardo en un vector las salidas obtenidas
    archivoSalidaObtenida=open('salidasObtenidas.txt','r')	
    salidaObtenida=zeros(self.cantidadEntradas)
    for contador,li in enumerate(archivoSalidaObtenida):
        salidaObtenida[contador]=li   
    archivoSalidaObtenida.close()

    #guardo en un vector las salidas deseadas
    archivoSalidaDeseada=open('salidasDeseadas.txt','r')	
    salidaDeseada=zeros(self.cantidadEntradas)
    for contador,li in enumerate(archivoSalidaDeseada):
        salidaDeseada[contador]=li   
    archivoSalidaDeseada.close()
 
    unoCorrecto=open("unoCorrecto.txt","w")
    unoIncorrecto=open("unoIncorrecto.txt","w")
    ceroCorrecto=open("ceroCorrecto.txt","w")
    ceroIncorrecto=open("ceroIncorrecto.txt","w")
    aux=2.0

    for i in range(self.cantidadEntradas):
	if(salidaObtenida[i] == salidaDeseada[i]):
		if salidaObtenida[i]==1:
			for k in range (self.num-1):
				unoCorrecto.write(str(entradas[i][k])+" ")    			
			unoCorrecto.write("\n")
		else:
			for k in range (self.num-1):
				ceroCorrecto.write(str(entradas[i][k])+" ")
			ceroCorrecto.write("\n")
	else:		
		for m in range(self.num):
			print pesos[m]
                	pesos[m]=pesos[m]+(factorAprendizaje*(salidaDeseada[i]-salidaObtenida[i])*entradas[i][m])

			#pesos[m]=pesos[m]+(factorAprendizaje*aux)*(salidaDeseada[i]*entradas[i][m])
		print "PESOS ACTUALIZADOS: \n",pesos
		salida=self.funcionActivacion(entradas[i],pesos)		
		if(salida == salidaDeseada[i]):
			if salida==1:		
				for k in range (self.num-1):
					unoCorrecto.write(str(entradas[i][k])+" ")
				unoCorrecto.write("\n")								
			else:
				for k in range (self.num-1):
					ceroCorrecto.write(str(entradas[i][k])+" ")
				ceroCorrecto.write("\n")
		else:
			if salida==1:		
				for k in range (self.num-1):					
					unoIncorrecto.write(str(entradas[i][k])+" ")
				unoIncorrecto.write("\n")
			else:
				for k in range (self.num-1):
					ceroIncorrecto.write(str(entradas[i][k])+" ")
				ceroIncorrecto.write("\n")
    unoCorrecto.close
    unoIncorrecto.close
    ceroCorrecto.close
    ceroIncorrecto.close

  def funcionActivacion(self,entradas,pesos):
    sumatoria=sum(entradas*pesos)
    c=.5
    if sumatoria>=c:
    	salida=1
    elif sumatoria<c:
    	salida=0
    return salida

  def calcularSalidaDeseada(self,entradas,pesos):
    sumatoria=sum(entradas*pesos)
    if sumatoria>=0:
    	salida=1
    elif sumatoria<0:
    	salida=0
    return salida
	
def main():	
        cantidadEntradas=(argv[1])
	factorAprendizaje=(argv[2])
        neurona1=neurona(int(cantidadEntradas))
        pesos=neurona1.inicializaPesos()
	entradas=neurona1.obtenerEntradas(pesos)
	neurona1.comparar(entradas,pesos,float(factorAprendizaje))
      
main()
