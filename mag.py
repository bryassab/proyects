import serial
import numpy
import matplotlib.pyplot as plt
import numpy.matlib as npm
from copy import copy, deepcopy


SENSITIVITY_MAG = (10.0*4800.0)/32768.0


data = serial.Serial('/dev/ttyACM0',9600,timeout=10)
print(data)

datos=numpy.zeros((100,5)) #bits
datos1=numpy.zeros((100,5)) #no calibrados
datos2=numpy.zeros((100,5)) # calibrados

value = input("\nQuiere adquirir los datos? S/N \n\n")

if value == 'S' or value == 's':
    print("\nCapturando datos\n")
    data.write(b'H')
    for i in range(100):
        rec=data.readline() #byte
        print(rec)
        rec=rec.decode("utf-8") #string
        print(rec)
        rec=rec.split() #lista
        datos[i][:]=rec
    print("\nTermina\n")
    print(datos,"\n")
    print(type(datos))
    print(type(datos[0,1]),type(datos[0][1]))

    offsets = [numpy.mean(datos[:,2]), numpy.mean(datos[:,3]),numpy.mean(datos[:,4])]
    print(offsets)
    datos1 = deepcopy(datos)
    #print("datos1",datos1)
    datos2 = deepcopy(datos)
    #print("datos2",datos2)

    for i in range(0,3):
        for j in range(0,100):
            datos2[j][i+2] = ((datos2[j,i+2])-offsets[i])*SENSITIVITY_MAG
           # datos2[j][i+5] = ((datos2[j,i+5])-offsets[i+3])*SENSITIVITY_GYRO
    #print("...datos2 \n",datos2)

    h=plt.figure(2)
    ax3 = h.subplots(2,2)
    h.suptitle('Magnetometro calibrado MPU9250')
    ax3[0,0].plot(datos2[:,0], datos2[:,2])
    ax3[0,0].set_title('mx')
    ax3[0,1].plot(datos2[:,0], datos2[:,3])
    ax3[0,1].set_title('my')
    ax3[1,0].plot(datos2[:,0], datos2[:,4])
    ax3[1,0].set_title('mz')
    ax3[1,1].plot(datos2[:,0], datos2[:,(2,3,4)])
    ax3[1,1].set_title('mx, my y mz')
    h.show()

   

    for i in range(0,3):
        for j in range(0,100):
            datos1[j][i+2] = ((datos2[j,i+2]))*SENSITIVITY_MAG
           # datos1[j][i+5] = ((datos2[j,i+5]))*SENSITIVITY_GYRO
    #print("...datos1 \n",datos1)

    f=plt.figure(1)
    ax1 = f.subplots(2,2)
    f.suptitle('Magnetometro no calibrado MPU9250')
    ax1[0,0].plot(datos1[:,0], datos1[:,2])
    ax1[0,0].set_title('mx')
    ax1[0,1].plot(datos1[:,0], datos1[:,3])
    ax1[0,1].set_title('ma')
    ax1[1,0].plot(datos1[:,0], datos1[:,4])
    ax1[1,0].set_title('mz')
    ax1[1,1].plot(datos1[:,0], datos1[:,(2,3,4)])
    ax1[1,1].set_title('mx, my y mz')
    f.show()


else:
    print("\nAdios\n")

