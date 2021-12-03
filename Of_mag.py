import serial
import numpy
import matplotlib.pyplot as plt
import numpy.matlib as npm
from copy import copy, deepcopy
import array


SENSITIVITY_MAG = (10.0*4800.0)/32768.0


data = serial.Serial('/dev/ttyACM1',9600,timeout=10)
print(data)

datosx=numpy.zeros((120,5)) #bits
datosy=numpy.zeros((120,5)) #bits
datosz=numpy.zeros((120,5)) #bits

datos1x=numpy.zeros((120,5)) #no calibrados
datos1y=numpy.zeros((120,5)) #no calibrados
datos1z=numpy.zeros((120,5)) #no calibrados

datos2x=numpy.zeros((120,5)) # calibrados
datos2y=numpy.zeros((120,5)) # calibrados
datos2z=numpy.zeros((120,5)) # calibrados

#offsets = [6.50,413,18.50]
 
offsets = [98,605.5,18.81]

value = input("\nQuiere adquirir los datos? S/N \n\n")

if value == 'S' or value == 's':
    print("\ndefina cuales ejes va a girar x y z\n")
    print("\nrecuerde que los ejes sellecionados hay que girarlos\n")
    print("\npara saber los datos de los demas ejes y presione S cuando este listo o  N en caso contrario \n")
    values = input("\n recuerde los ejes z=xy y=xz \n\n")
    if values == 's' or values == 'S':
        data.write(b'H')
        for i in range(0,120):
            recx=data.readline() #byte
            print(recx)
            recx=recx.decode("utf-8") #string
            print(recx)
            recx=recx.split() #lista
            datosx[i][:]=recx
        print("\nTermina\n")
        #print(datosx,"\n")
        print(type(datosx))
        print(type(datosx[0,1]),type(datosx[0][1]))
    print("\nya se tomaron los datos del eje al cual usted giro")
    print("\npresione S cuando este listo o  N en caso contrario \n")
    valuess = input("\n recuerde los ejes x=yz y=xy z=xy\n\n")
    if valuess == 's' or valuess == 'S':
        data.write(b'H')
        for j in range(0,120):
            rec=data.readline() #byte
            print(rec)
            rec=rec.decode("utf-8") #string
            print(rec)
            rec=rec.split() #lista
            datosy[j][:]=rec
        print("\nTermina\n")
        #print(datosy,"\n")
        print(type(datosy))
        print(type(datosy[0,1]),type(datosy[0][1]))
        print("\nya se tomaron los datos del eje al cual usted giro")
    print("\npresione S cuando este listo o  N en caso contrario \n")
    valuesss = input("\n recuerde los ejes x=yz y=xy z=xy\n\n")
    if valuesss == 's' or valuess == 'S':
        data.write(b'H')
        for j in range(0,120):
            rec=data.readline() #byte
            print(rec)
            rec=rec.decode("utf-8") #string
            print(rec)
            rec=rec.split() #lista
            datosz[j][:]=rec
        print("\nTermina\n")
        #print(datosz,"\n")
        print(type(datosz))
        print(type(datosz[0,1]),type(datosz[0][1]))
    else:
        print("\ngenerando graficas correspondientes")
        
   
    datos1x = deepcopy(datosx)
    #print("datos1",datos1)
    datos2x = deepcopy(datosx)
    #print("datos2",datos2)
    
    datos1y = deepcopy(datosy)
    #print("datos1",datos1)
    datos2y = deepcopy(datosy)
    #print("datos2",datos2)
    
    datos1z = deepcopy(datosz)
    #print("datos1",datos1)
    datos2z = deepcopy(datosz)
    #print("datos2",datos2)
    


    for i in range(0,3):
        for j in range(0,120):
            datos2x[j][i+2] = ((datos2x[j,i+2]-offsets[i]))*SENSITIVITY_MAG
            datos2y[j][i+2] = ((datos2y[j,i+2]-offsets[i]))*SENSITIVITY_MAG
            datos2z[j][i+2] = ((datos2z[j,i+2]-offsets[i]))*SENSITIVITY_MAG
              
             # datos2[j][i+5] = ((datos2[j,i+5])-offsets[i+3])*SENSITIVITY_GYRO
    #print("...datos2 \n",datos2)

    
    l=plt.figure(2)
    l.suptitle(' calibrado ')
    plt.plot(datos2x[:,2],datos2x[:,3],'-')
    plt.plot(datos2y[:,3],datos2y[:,4],'-') 
    plt.plot(datos2z[:,2],datos2z[:,4],'-')
    
    l.show()
    
    

   

    for i in range(0,3):
        for j in range(0,120):
            datos1x[j][i+2] = ((datos1x[j,i+2]))*SENSITIVITY_MAG
            datos1y[j][i+2] = ((datos1y[j,i+2]))*SENSITIVITY_MAG
            datos1z[j][i+2] = ((datos1z[j,i+2]))*SENSITIVITY_MAG
             
             # datos1[j][i+5] = ((datos2[j,i+5]))*SENSITIVITY_GYRO
    #print("...datos1 \n",datos1)

    f=plt.figure(1)
    f.suptitle('no calibrado z ')
   
    plt.plot(datos1x[:,2],datos1x[:,3],'-')
    plt.plot(datos1y[:,3],datos1y[:,4],'-') 
    plt.plot(datos1z[:,2],datos1z[:,4],'-' )
    f.show()
    
    
     
    
else:
    print("\nAdios\n")
