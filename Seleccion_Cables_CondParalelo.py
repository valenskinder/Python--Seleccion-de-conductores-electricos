from tkinter import *
from tkinter import messagebox #importo de tkinter para poder hacer una ventana emergente.
from tkinter import ttk #Importo de tkinter para la creacion del scrollbar

root=Tk() #Creacion raiz


root.title("Seleccion de cables de Baja Tensión")


#******************************************Creación de funciones***********************************************

def Seleccion (form,Iadm,resisCable,reacCable):

    try:

    #En la funcion se ingresan las listas correspondientes a los distintos valores de parámetros de los diferentes cables.
    
    #Calculo la caida de tension tanto en circuito monofásico como trifásico

        Iproy=float(cuadroCorriente.get())

        Uproy=float(cuadroTension.get())

        longi=float (cuadroLongitud.get())

        i=0

        resultadoCable=form[i]

        resultadoR=float(resisCable[i])

        resultadoRe=float(reacCable[i])

        deltaUM=(2)*(Iproy)*(longi)*((resultadoR*0.85)+(resultadoRe*0.53)) #Caida de tension circuito monofásico

        deltaUT=(1.73)*(Iproy)*(longi)*((resultadoR*0.85)+(resultadoRe*0.53)) #Caida de tension circuito trifásico
        
        if OpcionIlumoFM.get()==0: #Iluminacion: la caida de tension debera ser menor al 3 %

            porcentajeAdm=Uproy*(0.03) #Esto se empleara en la condicion de evaluacion del bucle while

            leyendaPorc="3 %" #Esto se concatena con el label warning 2

        else: #Fuerza motriz: la caida de tension debera ser menor al 5 %

            porcentajeAdm=Uproy*(0.05) #Esto se empleara en la condicion de evaluacion del bucle while

            leyendaPorc="5 %" #Esto se concatena con el label warning 2

        #A continuación, obtengo el valor máximo de la lista, para evaluar si la corriente será contenida
        #por un conductor, o por dos o más.

        maximaCorriente=max (Iadm) #Obtengo el mayor numero de la lista.

        if maximaCorriente > Iproy:

            cantConduc="(Un conductor)"

            while ((Iproy > Iadm[i]) or ( (deltaUM > porcentajeAdm)and (deltaUT > porcentajeAdm))): 
#Dentro del while evaluo para que se cumplan las dos condiciones
            

                i=i+1

                resultadoCable=form[i]

                resultadoIadm=Iadm[i]

                resultadoR=resisCable[i]

                resultadoRe=reacCable[i]

                deltaUM=(2)*(Iproy)*(longi)*((resultadoR*0.85)+(resultadoRe*0.53)) #Caida de tension circuito monofásico

                deltaUT=(1.73)*(Iproy)*(longi)*((resultadoR*0.85)+(resultadoRe*0.53)) #Caida de tension circuito trifásico
            
            leyendaCorrienteRes.config (text=str(Iproy))
            cableResultado.config (text=str(resultadoCable))
            iadmResultado.config (text=str(resultadoIadm))
            resistenciaResultado.config (text=str(resultadoR))
            reactanciaResultado.config (text=str(resultadoRe))

        else: #En el caso que la corriente admisible del cable sea menor que la del proyecto, se deberá colocar dos conductores por fase
        
            if maximaCorriente > (Iproy/2):

                cantConduc="(Dos conductores)"

                while (((Iproy/2) > Iadm[i]) or ( (deltaUM > porcentajeAdm)and (deltaUT > porcentajeAdm))): 
#Dentro del while evaluo para que se cumplan las dos condiciones
            
                    i=i+1

                    resultadoCable=form[i]

                    resultadoIadm=Iadm[i]

                    resultadoR=(resisCable[i])/2

                    resultadoRe=(reacCable[i])/2

                    deltaUM=(2)*(Iproy)*(longi)*((resultadoR*0.85)+(resultadoRe*0.53)) #Caida de tension circuito monofásico

                    deltaUT=(1.73)*(Iproy)*(longi)*((resultadoR*0.85)+(resultadoRe*0.53)) #Caida de tension circuito trifásico
            
                leyendaCorrienteRes.config (text=str(round ((Iproy/2),4)))
                cableResultado.config (text=str(resultadoCable))
                iadmResultado.config (text=str(resultadoIadm))
                resistenciaResultado.config (text=str(round (resultadoR,4)))
                reactanciaResultado.config (text=str(round (resultadoRe,4)))

            else: #Comienza el calculo para tres conductores en paralelo.

                cantConduc="(Tres conductores)"

                while (((Iproy/3) > Iadm[i]) or ( (deltaUM > porcentajeAdm)and (deltaUT > porcentajeAdm))): 
#Dentro del while evaluo para que se cumplan las dos condiciones
            
                    i=i+1

                    resultadoCable=form[i]

                    resultadoIadm=Iadm[i]

                    resultadoR=(resisCable[i])/3

                    resultadoRe=(reacCable[i])/3

                    deltaUM=(2)*(Iproy)*(longi)*((resultadoR*0.85)+(resultadoRe*0.53)) #Caida de tension circuito monofásico

                    deltaUT=(1.73)*(Iproy)*(longi)*((resultadoR*0.85)+(resultadoRe*0.53)) #Caida de tension circuito trifásico
            
                leyendaCorrienteRes.config (text=str(round ((Iproy/3),4)))
                cableResultado.config (text=str(resultadoCable))
                iadmResultado.config (text=str(resultadoIadm))
                resistenciaResultado.config (text=str(round (resultadoR,4)))
                reactanciaResultado.config (text=str(round (resultadoRe,4)))

        if OpcionCircuitos.get()==0: #La opcion elegida es calculo de caida de tensión monofásica

            deltaUResultado.config(text=str(round(deltaUM,4))) #con round corto la variable deltaUM en 4 digitos
            warning1.config (text="El conductor verifica por criterio térmico",bg="green",fg="black")
            warning2.config (text="El conductor verifica por caida de tensión. Caida de tension menor al: "+leyendaPorc ,bg="green",fg="black")

        else: #La opcion elegida es calculo de caida de tensión trifásica

            deltaUResultado.config(text=str(round(deltaUT,4))) #con round corto la variable deltaUM en 4 digitos
            warning1.config  (text="El conductor verifica por criterio térmico",bg="green",fg="black")
            warning2.config (text="El conductor verifica por caida de tensión. Caida de tension menor al: "+leyendaPorc ,bg="green",fg="black")

    # Parte del programa para escribir los labels que indicaran los resultados

        leyendaResultado.config(text="El cable seleccionado es: ",fg="gray10")
        leyendaCorriente.config (text="La corriente del proyecto es:"+ cantConduc)
        leyendaIadm.config (text="La corriente admisible del conductor es:",fg="gray10")
        leyendaResistencia.config (text="La resistencia del cable seleccionado es [Ω/km] :",fg="gray10")
        leyendaReactancia.config (text="La reactancia del cable seleccionado es: [Ω/km] :",fg="gray10")
        leyendaDeltaU.config (text="La caida de tensión es: ",fg="gray10")


    except:
        warning1.config (fg="black",bg="red",text="La intensidad ingresada es mayor a la maxima admisible del tipo de conductor y a su forma de instalacion seleccionado.Intente con otro. ")
        leyendaIadm.config(text="")
        iadmResultado.config(text="")
        leyendaResultado.config(text="")
        leyendaResistencia.config (text="")
        leyendaReactancia.config (text="")
        leyendaDeltaU.config (text="")
        deltaUResultado.config (text="")
        cableResultado.config (text="")
        resistenciaResultado.config (text="")
        reactanciaResultado.config (text="")
        warning2.config (text="",bg="gray20")
        leyendaCorriente.config (text="")
        leyendaCorrienteRes.config (text="")
        
#******************************************************Creacion de funcion CALCULAR*********************************************************
def Calcular():

#A continuación, evaluo, si lo ingresado a los entry, corresponde a un numero. Si es asi, continuo con las operaciones, sino marca un error
# en un label.


    uno=cuadroCorriente.get().replace(".","1").isdigit() #En el caso que exista un ".", lo reemplazo con un "1". "isdigit" da TRUE si es todo numero 
    dos=cuadroTension.get().replace(".","1").isdigit()
    tres=cuadroLongitud.get().replace(".","1").isdigit()

    if (uno and dos and tres==True): #Si todo lo ingresado es numero, continuo con la operacion

#A continuacion, dependiendo de el tipo de cable, y forma de instalacion, se realiza el calculo llamando a la funcion selección    

#Para todas las opciones de cable unipolar

        if ((OpcionCables.get()==1) and opcionMetodos.get()==0):

            Seleccion(unipolar,dosUnip,resisUnipolar,reactUnipolar)

        elif ((OpcionCables.get()==1) and opcionMetodos.get()==1):

            Seleccion(unipolar,tresbolilloUnip,resisUnipolar,reactUnipolar)

        elif ((OpcionCables.get()==1) and opcionMetodos.get()==2):

            Seleccion(unipolar,iadmTresUnCont,resisUnipolar,reactUnipolar)

        elif ((OpcionCables.get()==1) and opcionMetodos.get()==3):

            Seleccion(unipolar,iadTresUnipSepH,resisUnipolar,reactUnipolar)

        elif ((OpcionCables.get()==1) and opcionMetodos.get()==4):

            Seleccion(unipolar,iadTresUnipSepV,resisUnipolar,reactUnipolar)

        elif ((OpcionCables.get()==1) and opcionMetodos.get()==5):

            Seleccion(unipolar,iadTresUnipEnt,resisUnipolar,reactUnipolar)

#Para todas las opciones de cable bipolar

        if ((OpcionCables.get()==2) and opcionMetodos.get()==0):

            Seleccion(formBipolar,iadmParedBipo,resisBipolar,reacBipoar)

        elif ((OpcionCables.get()==2) and opcionMetodos.get()==1):

            Seleccion(formBipolar,iadmBanNoPerfBipo,resisBipolar,reacBipoar)
    
        elif ((OpcionCables.get()==2) and opcionMetodos.get()==2):

            Seleccion(formBipolar,iadmBanPerfBipo,resisBipolar,reacBipoar)

        elif ((OpcionCables.get()==2) and opcionMetodos.get()==3):

            Seleccion(formBipolar,iadmCaEntBipo,resisBipolar,reacBipoar)
    
        elif ((OpcionCables.get()==2) and opcionMetodos.get()==4):

            Seleccion(formBipolar,iadmCondEntBipo,resisBipolar,reacBipoar)

#Para todas las opciones de cable tripolar

        if ((OpcionCables.get()==3) and opcionMetodos.get()==0):

            Seleccion(formTripolar,iadmParedTripolar,resisTripolar,reacTripolar)

        elif ((OpcionCables.get()==3) and opcionMetodos.get()==1):

            Seleccion(formTripolar,iadmBanNoPerfTripolar,resisTripolar,reacTripolar)

        elif ((OpcionCables.get()==3) and opcionMetodos.get()==2):

            Seleccion(formTripolar,iadmBanPerfTripolar,resisTripolar,reacTripolar)

        elif ((OpcionCables.get()==3) and opcionMetodos.get()==3):

            Seleccion(formTripolar,iadmCaEntTripolar,resisTripolar,reacTripolar)

        elif ((OpcionCables.get()==3) and opcionMetodos.get()==4):

            Seleccion(formTripolar,iadmCondEntTripolar,resisTripolar,reacTripolar)

#Para todas las opciones de los cables tetrapolares

        if ((OpcionCables.get()==4) and opcionMetodos.get()==0):

            Seleccion(formTretrapolar,iadmParedTripolar,resisTripolar,reacTripolar)

        elif ((OpcionCables.get()==4) and opcionMetodos.get()==1):

            Seleccion(formTretrapolar,iadmBanNoPerfTripolar,resisTripolar,reacTripolar)

        elif ((OpcionCables.get()==4) and opcionMetodos.get()==2):

            Seleccion(formTretrapolar,iadmBanPerfTripolar,resisTripolar,reacTripolar)

        elif ((OpcionCables.get()==4) and opcionMetodos.get()==3):

            Seleccion(formTretrapolar,iadmCaEntTripolar,resisTripolar,reacTripolar)

        elif ((OpcionCables.get()==4) and opcionMetodos.get()==4):

            Seleccion(formTretrapolar,iadmCondEntTripolar,resisTripolar,reacTripolar)
    
    else: #En el caso que se ingrese una letra u otro simbolo, escribe un mensaje de error en un label.

        warning1.config (fg="black",bg="red",text="Ha ingresado un valor incorrecto en alguno de los cuadros de CORRIENTE,TENSION u LONGITUD.VERIFIQUE")
        
#******************************************************Creacion de funcion BORRAR**********************************************************

def Borrar():
    cuadroCorriente.delete(0,END)
    cuadroLongitud.delete(0,END)
    cuadroTension.delete(0,END)
    leyendaIadm.config(text="")
    iadmResultado.config(text="")
    leyendaResultado.config(text="")
    leyendaResistencia.config (text="")
    leyendaReactancia.config (text="")
    leyendaDeltaU.config (text="")
    deltaUResultado.config (text="")
    cableResultado.config (text="")
    resistenciaResultado.config (text="")
    reactanciaResultado.config (text="")
    warning1.config (text="",bg="gray20")
    warning2.config (text="",bg="gray20")
    leyendaCorriente.config (text="")
    leyendaCorrienteRes.config (text="")
    
def SalirAplicacion (): #Funcion para que pregunta si se desea salir o no de la aplicacion.

    valor=messagebox.askquestion("Salir","Desea salir de la aplicacion?")

#Si el elijo si, la variable valor tiene el valor de "yes"

    if valor=="yes": 
        root.destroy() #Para  el programa.

def InfoAdicional(): #Funcion para mostrar aviso en una ventana emergente. Tengo que llamar con un command desde el subelemento
    #de AYUDA, Acerca de...
    
    messagebox.showinfo("Cálculo de cables eléctricos de Cobre- Ing. Valentin Skinder","Datos utilizados del catálogo de cables PRYSMIAN-SINTENAX.")



#****************************************************************Creación del menu**********************************************************
#Creacion del menu.

barraMenu=Menu (root) #Creacion de variable, y le decimos a donde va a pertenecer (root).

root.config (menu=barraMenu, width=300,height=300,bg="gray70")

#Establecemos cuantos elementos va a contener el menu.

#Elemento ARCHIVO

archivoMenu=Menu (barraMenu,tearoff=0) #Con tearoff es para eliminar una linea dentro del submenu.

archivoMenu.add_command(label="Calcular",command=Calcular) #Para agregar un subelemento al elemento ARCHIVO. A continuacion agregamos otros subelementos:
archivoMenu.add_command(label="Borrar",command=Borrar)# Con command llamo a la funcion que quiero que ejecute

archivoMenu.add_separator() #Esto es para hacer una linea que separa los elementos del submenu. Tenemos que colocarla en la parte del codigo
#que querramos separar.
archivoMenu.add_command(label="Salir",command=SalirAplicacion)

#Elemento AYUDA

archivoAyuda=Menu (barraMenu,tearoff=0)

#Creamos subelementos para AYUDA

archivoAyuda.add_command(label="Acerca de...",command=InfoAdicional)#Con command llamo a la funcion para mostrar la ventana emergente.

#Especificamos los nombres de cada elemento del menu de la siguiente manera:

barraMenu.add_cascade (label="Archivo",menu=archivoMenu) #El elemento archivo menu, perteneciente a la barra menu, tendra el nombre de archivo.

barraMenu.add_cascade (label="Ayuda",menu=archivoAyuda)

#************************************************************Creación del primer frame******************************************************
miFrame1=Frame(root,bg="gray70") #Creacion frame

miFrame1.pack() #Empaquetamiento frame

#******************************************************Lista de parámetros de cable unipolar************************************************

unipolar=["0","4 mm2","6 mm2","10 mm2","16 mm2","25 mm2","35 mm2","50 mm2","70 mm2","95 mm2","120 mm2","150 mm2","185 mm2","240 mm2","300 mm2","400 mm2","500 mm2","630 mm2"]
resisUnipolar=[1,5.92,3.95,2.29,1.45,0.933,0.663,0.462,0.326,0.248,0.194,0.156,0.129,0.0987,0.0754,0.0606,0.0493,0.0407] #Resistencia.Esto es en  [Ω/km]
reactUnipolar=[1,0.189,0.180,0.170,0.162,0.154,0.150,0.147,0.143,0.142,0.139,0.139,0.139,0.137,0.140,0.140,0.138,0.138] #Reactancia. Esto es en  [Ω/km]
dosUnip=[1,36,46,64,86,114,141,171,218,264,306,353,403,475,547,656] #Dos cables unipolares en contacto [A]
tresbolilloUnip=[1,29,37,52,71,96,119,145,199,230,268,310,356,422,488,571] #Tres Cables unipolares en tresbolillo [A]
iadmTresUnCont=[1,30,39,55,74,99,124,151,196,239,279,324,371,441,511,599] #Tres cables unipolares en contacto [A]
iadTresUnipSepH=[1,39,51,70,96,127,157,191,244,297,345,397,453,535,617,741] #Tres cables unipolares separados en forma horizontal [A]
iadTresUnipSepV=[1,34,44,62,84,113,141,171,221,271,315,365,418,495,573,692] #Tres cables unipolares separados en forma vertical [A]
iadTresUnipEnt=[1,28,37,47,59,80,104,134,162,198,240,280,324,363,405,475,533] #Tres cables unipolares directamente enterrado [A]

#******************************************************Lista de parámetros de cable bipolar*************************************************

formBipolar=["0","1.5 mm2","2.5 mm2","4 mm2","6 mm2","10 mm2","16 mm2","25 mm2","35 mm2"] #Esto es en mm2.
resisBipolar=[1,15.9,9.55,5.92,3.95,2.29,1.45,0.933,0.663] #Resistencia.Esto es en  [Ω/km]
reacBipoar=[1,0.108,0.0995,0.0991,0.0901,0.0860,0.0813,0.0780,0.0760] #Reactancia. Esto es en  [Ω/km]
iadmParedBipo=[1,14,20,26,33,45,60,78,97] #Corriente admisible de conductor en caño embutido en pared [A]
iadmBanNoPerfBipo=[1,17,23,31,40,55,74,97,120] #Corriente admisible en bandeja no perforada o solida [A]
iadmBanPerfBipo=[1,19,26,35,44,61,82,104,129] #Corriente admisible en bandeja perforada [A]
iadmCaEntBipo=[1,25,33,43,53,71,91,117,140] #Corriente admisible en conductor en caño enterrado [A]
iadmCondEntBipo=[1,29,39,51,65,88,112,137,164] #Corriente admisible de un conductor directamente enterrado [A]

#************************************Lista de parámetros de cabletripolar*************************************************
formTripolar=["0","1.5 mm2","2.5 mm2","4 mm2","6 mm2","10 mm2","16 mm2","25 mm2","35 mm2","50 mm2","70 mm2","95 mm2","120 mm2","150 mm2","185 mm2","240 mm2","300 mm2"]
resisTripolar=[1,15.9,9.55,5.92,3.95,2.29,1.45,0.933,0.663,0.464,0.321,0.232,0.184,0.150,0.121,0.0911,0.0730] #Resistencia.Esto es en  [Ω/km]
reacTripolar=[1,0.108,0.09995,0.0991,0.0901,0.0860,0.0813,0.0780,0.0760,0.0777,0.0736,0.0733,0.0729,0.0720,0.0720,0.0716,0.0714] #Reactancia.Esto es en  [Ω/km]
iadmParedTripolar=[1,13,17,23,30,40,54,70,86,103,130,156,179] #Corriente admisible del conductor en caño embutido en pared [A]
iadmBanNoPerfTripolar=[1,15,21,28,36,50,66,84,104,125,160,194,225,260,297,350,403] #Corriente admisible del conductor en bandeja no perforada o solida [A]
iadmBanPerfTripolar=[1,16,22,30,37,52,70,88,110,133,170,207,240,278,317,374,432] #Corriente admisible en bandeja perforada [A]
iadmCaEntTripolar=[1,20,27,35,44,58,75,96,115,137,169,201,228,258,289,333,377] #Corriente admisible en conductor en caño enterrado [A]
iadmCondEntTripolar=[1,25,34,44,55,74,95,117,140,173,211,254,290,325,369,428,484] #Corriente admisible de un conductor directamente enterrado [A]

#*****************************************************Lista de parámetros de cable tetrapolar************************************************

formTretrapolar=["0","1.5 mm2","2.5 mm2","4 mm2","6 mm2","10 mm2","16 mm2","25-16 mm2","35-16 mm2","50-25 mm2","70-35 mm2","95-50 mm2","120-70 mm2","150-70 mm2","185-95 mm2","240-120 mm2","300-150 mm2"]
 # El resto de los valores de resistencias,reactancias y corrientes admisibles son iguales que los tripolares.

#****************************************************************Titulo********************************************************************

titulo=Label(miFrame1,text="Selección de cables eléctricos de Baja Tensión de cobre",justify="right")
titulo.grid(row=0,column=0)
titulo.config(fg="gray10",bg="gray70")
titulo.config(font=("verdana",20))

#**************************Creación del segundo frame que contendrá los radio button de los tipos de circuito**************************

miFrame2=Frame (root,bg="gray70") #Creacion del segundo frame.

miFrame2.pack() #Empaquetamiento del segundo frame.

#****************************************************Creacion de los radio button******************************************************

OpcionCircuitos=IntVar() #Variable para los radio button de seleccion del tipo de circuito

OpcionIlumoFM=IntVar() #Variable para los radio button de seleccion de circuito de fuerza motriz o iluminación

circMono=Radiobutton (miFrame2, text="Circuito monofásico", variable=OpcionCircuitos,value=0,bg="gray70",fg="gray10",activebackground="gray20") #Radio button para seleccion circ. monofásico.
circMono.grid(row=0,column=0) #Con esto hago que aparezcan todos los radio button alineados.

circTrif=Radiobutton (miFrame2, text="Circuito trifásico", variable=OpcionCircuitos,value=1,bg="gray70",fg="gray10",activebackground="gray20") #Radio button para seleccion circ. trifásico.
circTrif.grid(row=0,column=1)

iluminacion=Radiobutton (miFrame2, text="Iluminación", variable=OpcionIlumoFM,value=0,bg="gray70",fg="gray10",activebackground="gray20") #Radio button para seleccion circ. monofásico.
iluminacion.grid(row=1,column=0) #Con esto hago que aparezcan todos los radio button alineados.

FM=Radiobutton (miFrame2, text="Fuerza Motriz", variable=OpcionIlumoFM,value=1,bg="gray70",fg="gray10",activebackground="gray20") #Radio button para seleccion circ. trifásico.
FM.grid(row=1,column=1)

#**************************************Creación del tercer frame que contendrá los labels y entry*****************************************
miFrame3=Frame (root,bg="gray70") #Creacion del tercer frame.

miFrame3.pack() #Empaquetamiento del tercer frame.

#*********************************************************Creacion de los labels**********************************************************

corriente= Label(miFrame3, text="Corriente nominal [A]: ",bg="gray70",fg="gray10") #Label de corriente nominal.
corriente.grid(row=0, column=1, padx=10, pady=10)

tension= Label(miFrame3, text="Tension nominal [V]: ",bg="gray70",fg="gray10") #Label de tension nominal.
tension.grid(row=1, column=1, padx=10, pady=10)

longitud= Label(miFrame3, text="Longitud [km]: ",bg="gray70",fg="gray10") #Label de longitud.
longitud.grid(row=2, column=1, padx=10, pady=10)

#********************************************************Creacion de los entry**********************************************************

cuadroCorriente=Entry (miFrame3,bg="ivory2") #Entry para la corriente nominal.
cuadroCorriente.grid (row=0,column=2,padx=10,pady=10)
cuadroCorriente.config(justify="right",fg="black")


cuadroTension=Entry (miFrame3,bg="ivory2") #Entry para la tension nominal.
cuadroTension.grid (row=1,column=2,padx=10,pady=10)
cuadroTension.config(justify="right",fg="black")

cuadroLongitud=Entry (miFrame3,bg="ivory2") #Entry para la longitud.
cuadroLongitud.grid (row=2,column=2,padx=10,pady=10)
cuadroLongitud.config(justify="right",fg="black")

#*************************Creación del cuarto frame que contendrá los radio button de seleccion del tipo de cables********************

miFrame4=Frame (root,bg="gray70") #Creacion del cuarto frame.

miFrame4.pack() #Empaquetamiento del cuarto frame.

#************************************* Creacion de los radio button de seleccion del tipo de cables***********************************

def Etiqueta(): #En funcion de la seleccion de tipo de cable, los radio button del quinto frame cambiaran su forma de instalacion.

    if (OpcionCables.get()==1):

        metodo1.config (text="Dos cables unipolares en contacto",bg="gray70",fg="gray10")
        metodo2.config (text="Tres cables unipolares en tresbolillo",bg="gray70",fg="gray10")
        metodo3.config (text="Tres cables unipolares en contacto",bg="gray70",fg="gray10")
        metodo4.config (text="Tres cables unipolares separados horizontalmente",bg="gray70",fg="gray10")
        metodo5.config (text="Tres cables unipolares separados verticalmente",bg="gray70",fg="gray10")
        metodo6.config (text="Tres cables unipolares directamente enterrados",bg="gray70",fg="gray10")
        
    elif (OpcionCables.get()==2 or OpcionCables.get()==3 or OpcionCables.get()==4 ):

        metodo1.config (text="Cables en caños embutidos en pared",bg="gray70",fg="gray10")
        metodo2.config (text="Cables en bandeja no perforada",bg="gray70",fg="gray10")
        metodo3.config (text="Cables en bandeja perforada",bg="gray70",fg="gray10")
        metodo4.config (text="Cables en caño y enterrados",bg="gray70",fg="gray10")
        metodo5.config (text="Cables directamente enterrados",bg="gray70",fg="gray10")
        metodo6.config (text="")
     
OpcionCables=IntVar()

cUnip=Radiobutton (miFrame4, text="Cable unipolar", variable=OpcionCables,value=1,command=Etiqueta,bg="gray70",fg="gray10",activebackground="gray20") #Radio button para seleccion del tipo de cable unipolar
cUnip.grid(row=1,column=0)

cBipolar=Radiobutton (miFrame4, text="Cable bipolar", variable=OpcionCables,value=2,command=Etiqueta,bg="gray70",fg="gray10",activebackground="gray20") #Radio button para seleccion del tipo de cable bipolar
cBipolar.grid(row=1,column=1)

cTripolar=Radiobutton (miFrame4, text="Cable tripolar", variable=OpcionCables,value=3,command=Etiqueta,bg="gray70",fg="gray10",activebackground="gray20") #Radio button para seleccion del tipo de cable tripolar
cTripolar.grid(row=1,column=2)

cTetrapolar=Radiobutton (miFrame4, text="Cable tetrapolar", variable=OpcionCables,value=4,command=Etiqueta,bg="gray70",fg="gray10",activebackground="gray20") #Radio button para seleccion del tipo de cable tetrapolar
cTetrapolar.grid(row=1,column=3)


#**************************************Creación del quinto frame que contendrá los radio button**************************************
miFrame5=Frame (root,bg="gray70") #Creacion del quinto frame.

miFrame5.pack() #Empaquetamiento del quinto frame.

opcionMetodos=IntVar() #Variable para los radio button de seleccion del tipo de montaje de los conductores

# A continuación se crean los radio button para los diferentes metodos de instalacion del conductor, dependiendo si son unipolares,
# bipolares,tripolares o tetrapolares

metodo1=Radiobutton (miFrame5,variable=opcionMetodos,value=0,bg="gray70",activebackground="gray20")
metodo1.pack(anchor="w")

metodo2=Radiobutton (miFrame5,variable=opcionMetodos,value=1,bg="gray70",activebackground="gray20")
metodo2.pack(anchor="w")

metodo3=Radiobutton (miFrame5,variable=opcionMetodos,value=2,bg="gray70",activebackground="gray20")
metodo3.pack(anchor="w")

metodo4=Radiobutton (miFrame5,variable=opcionMetodos,value=3,bg="gray70",activebackground="gray20")
metodo4.pack(anchor="w")

metodo5=Radiobutton (miFrame5,variable=opcionMetodos,value=4,bg="gray70",activebackground="gray20")
metodo5.pack(anchor="w")

metodo6=Radiobutton (miFrame5,variable=opcionMetodos,value=5,bg="gray70",activebackground="gray20")
metodo6.pack(anchor="w")

#**************************************Creacion del sexto frame que contendra los botones**********************************

miFrame6=Frame (root,bg="gray70") #Creacion del sexto frame.

miFrame6.pack() #Empaquetamiento del sexto frame.

#****************************************************Creacion de los botones************************************************

calcular=Button (miFrame6,text="Calcular",activebackground="green",relief=RAISED, borderwidth=5,command=Calcular,bg="royalblue1") #con activebackground cuando aprieto el boton, cambia el color.
calcular.config(width=35,height=2)
calcular.grid (row=0,column=0,padx=10,pady=10)

borrar=Button (miFrame6,text="Borrar",activebackground="red",relief=RAISED, borderwidth=5,command=Borrar,bg="royalblue1")
borrar.config(width=35,height=2)
borrar.grid (row=0,column=1,padx=10,pady=10)

#**************************************Creacion del scrollbar para el septimo frame*********************************************

#**************************************Creacion del septimo frame que contendra los resultados**********************************
#Primero creamos un frame que contenga todo.
miFrame7=Frame (root,bg="gray70") #Creacion del septimo frame.
miFrame7.pack(fill=BOTH,expand=1) #Empaquetamiento del septimo frame.

#Luego creamos un canvas (liezo)
miCanvas=Canvas (miFrame7,bg="gray70")
miCanvas.pack (side=LEFT,fill=BOTH, expand=1)

#Agregamos el scrollbar al canvas
miBarra=ttk.Scrollbar (miFrame7,orient=VERTICAL, command=miCanvas.yview)
miBarra.pack(side=RIGHT, fill=Y)

#Configuramos el canvas
miCanvas.configure (yscrollcommand=miBarra.set)
miCanvas.bind ("<Configure>", lambda e: miCanvas.configure(scrollregion=miCanvas.bbox ("all")))

#Creamos otro frame dentro del canvas
miFrame8= Frame (miCanvas,bg="gray70")

#Agregamos el ultimo frame dentro del canvas
miCanvas.create_window((0,0),window=miFrame8,anchor="nw")


#**************************************Creacion de los labels de resultados*****************************************************
warning1=Label(miFrame8,bg="gray70",fg="gray10") #Contendra la leyenda para indicar que cumple por criterio termico
warning1.grid (row=0,column=0,padx=10,pady=10)

warning2=Label(miFrame8,bg="gray70",fg="gray10") #Contendra la leyenda para indicar que cumple por caida de tension
warning2.grid (row=1,column=0,padx=10,pady=10)

leyendaCorriente=Label(miFrame8,bg="gray70",fg="gray10") #Label= "La corriente en el conductor es: "
leyendaCorriente.grid (row=3,column=0,padx=10,pady=10)

leyendaCorrienteRes=Label(miFrame8,bg="gray70",fg="gray10") #Label= Contendra el valor de la corriente en el conductor
leyendaCorrienteRes.grid (row=3,column=1,padx=10,pady=10)


leyendaResultado=Label(miFrame8,bg="gray70",fg="gray10") #Label= "El cable seleccionado es: "
leyendaResultado.grid (row=4,column=0,padx=10,pady=10)

cableResultado=Label(miFrame8,bg="gray70",fg="gray10") #Contendra el resultado del cable seleccionado
cableResultado.grid (row=4,column=1,padx=10,pady=10)

leyendaIadm=Label(miFrame8,bg="gray70",fg="gray10") #Label= "La corriente admisible del cable es: "
leyendaIadm.grid (row=5,column=0,padx=10,pady=10)

iadmResultado=Label(miFrame8,bg="gray70",fg="gray10") #Contendra el resultado de la corriente admisible
iadmResultado.grid (row=5,column=1,padx=10,pady=10)

leyendaResistencia=Label(miFrame8,bg="gray70",fg="gray10") #Label= "La resistencia del cable seleccionado es:  "
leyendaResistencia.grid(row=6,column=0,padx=10,pady=10)

resistenciaResultado=Label(miFrame8,bg="gray70",fg="gray10") #Contendra el resultado de la resistencia del cable seleccionado
resistenciaResultado.grid (row=6,column=1,padx=10,pady=10)

leyendaReactancia=Label(miFrame8,bg="gray70",fg="gray10") #Label= "La reactancia del cable seleccionado es:  "
leyendaReactancia.grid (row=7,column=0,padx=10,pady=10)

reactanciaResultado=Label(miFrame8,bg="gray70",fg="gray10") #Contendra el resultado de la reactancia del cable seleccionado
reactanciaResultado.grid (row=7,column=1,padx=10,pady=10)

leyendaDeltaU=Label(miFrame8,bg="gray70",fg="gray10") #Label= "La caida de tension del cable seleccionado es:  "
leyendaDeltaU.grid (row=8,column=0,padx=10,pady=10)

deltaUResultado=Label(miFrame8,bg="gray70",fg="gray10") #Contendra el resultado de la caida de tension
deltaUResultado.grid (row=8,column=1,padx=10,pady=10)




root.mainloop()