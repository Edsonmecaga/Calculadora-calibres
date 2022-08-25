# =======================================E============================================ #
# ==================================================================================== #
#=====  Software que calcula el calibre necesario en una instalación electria   ====== #
# ==================================================================================== #
# =====================================*___*========================================== #




# Comenzamos con el menu de tipo de red

option = 0 
print("""

Selecciona el numero de acuerdo al tu circuito

    1.-Monofásica
    2.-Bifasica
    3.-Trifásica 3H
    4.-Trifásica 4H

""")
option =int (input ( "  "))





# =========================================D========================================== #
# ==================================================================================== #
# ============ EMPEZAMOS A HACER LAS OPERACIONES SI LA RED ES MONOFÁSICA  ============ #
# ==================================================================================== #
# ========================================:v========================================== #



if option== 1:
    w = float(input("Introduce el dato de Potencia en Watts:        "))
    fd = .85
    fp = .90
    l = float (input("Introduce la distancia en metros:             "))


    print("     ")
    ipc = ((w * fd) / (110 * fp)) 
    In = 1.25 * ipc




    # Se hace la busqueda de calibres con respecto a los parametros de la norma, se eligira el calibre mas alto
    if (In<20):
        calibre1 = 14
        
    elif ( 20>= In <25):
        calibre1 = 12
    elif ( 25>= In < 35 ):
        calibre1 = 10
    elif ( 35 >= In < 50):
        calibre1= 8
    elif ( 50>= In < 65 ):
        calibre1 = 6
    elif ( 65>= In < 85 ):
        calibre1 = 4
    elif ( 85>= In < 100 ):
        calibre1 = 3
    elif ( 100>= In < 115 ):
        calibre1 = 2
    elif ( 115>= In < 130 ):
        calibre1 = 1
    else:
        print("""
        
        Lamentablemente la calculadora malota de calibres detecto datos erroneos 
        
        Intentalo de nuevo
        
        """)
    # Se hace la correccion por caida de tension
    e=2
    s = ((4 * l * In)/(110*e))
    s=round(s,1)
    
    #Se hace la busqueda por parametros de acuerdo a la nom, se hace la comparación del resultado de los dos calibres y se emite la respuesta en 
    #favor del numero mas bajo.
    
    if( s < 0.8235):
        calibre2=18
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(.8235<= s) and (s < 1.307):  
        calibre2=16
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(1.307<= s)  and (s < 2.08):
        calibre2=14
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(2.08<= s) and (s < 3.307):
        calibre2=12
        if(calibre1>=calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(3.307<= s) and (s < 5.26):
        calibre2=10
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(5.26<= s) and (s < 8.367):
        calibre2=8
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(8.367<= s) and (s < 13.3):
        calibre2=6
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(13.3<= s) and (s < 21.15):
        calibre2=4
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    elif(21.15<= s) and (s < 26.67):
        calibre2=3
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(26.67<= s) and (s < 33.62):
        calibre2=2
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    elif(33.62<= s) and (s < 44.41):
        calibre2=1
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1    
    else:
        print("Calibre no enocntrado, Intenta de nuevo ")
    
    my_Id= 1.4* ipc
    if(my_Id<15):
        tmagnetico=15
        mess=1
    elif(15<=my_Id) and (my_Id<20):
        tmagnetico=20
        mess=1
    elif(20<=my_Id) and (my_Id<30):
        tmagnetico=30
        mess=1
    elif(30<=my_Id) and (my_Id<50):
        tmagnetico=50
        mess=1
    elif(50<=my_Id) and (my_Id<60):
        tmagnetico=60
    if(mess==1):
        print("Para esta instalacion se requiere un Interruptor Termodinámico de ", tmagnetico, " Amp")
    else:
        print("No se encontro un interruptor termomagnetico adecuado, intenta de nuevo")
    
#Se imprime el ticket
    my_ticket = int(input("Presione 1 para imprimir ticket ..."))
    if(my_ticket==1):
      print("""

    ======================================================================================================================================    
    ======================================================================================================================================
    ======================================================================================================================================



    El departamento de mantenimiento de la Empresa X solicita al departamento de compras lo siguiente:
    
    Cable calibre #""",calibrefinal, """THW Ang 75° Marca ACME
    
    Interruptor termodinámico de """, tmagnetico,""" Amp. Marca ACME
    
    Todo esto con el propósito de finalizar nuestras funciones como departamento. 
    
    Esperamos la pronta respuesta del departamento de compras a fin de no retrasar las tareas ya agendadas para este bimestre
    
    Att. Lic. Patito Diaz. 
    Director de mantenimiento
    
    ======================================================================================================================================    
    ======================================================================================================================================
    ======================================================================================================================================"""
    )




    # ================================================================================== #
    # ================================================================================== #
    # ============ EMPEZAMOS A HACER LAS OPERACIONES SI LA RED ES BIFASICA  ============ #
    # ================================================================================== #
    # ======================================0-0========================================= #


elif option== 2:
    

    w = float(input("Introduce el dato de Potencia en Watts:        "))
    fd = .85
    fp = .90
    l = float (input("Introduce la distancia en metros:             "))


    
    ipc = ((w * fd) / (2 * 220 * fp) ) 
    In = (1.25 * ipc)

    

    #Comenzamos la busqueda con respecto a los parametros establecidos en la NOM


    if (In<20):
        calibre1 = 14
        
    elif ( 20>= In <25):
        calibre1 = 12
    elif ( 25>= In < 35 ):
        calibre1 = 10
    elif ( 35 >= In < 50):
        calibre1= 8
    elif ( 50>= In < 65 ):
        calibre1 = 6
    elif ( 65>= In < 85 ):
        calibre1 = 4
    elif ( 85>= In < 100 ):
        calibre1 = 3
    elif ( 100>= In < 115 ):
        calibre1 = 2
    elif ( 115>= In < 130 ):
        calibre1 = 1

    else:
        print("""
        
        Lamentablemente la calculadora malota de calibres detecto datos erroneos 
        
        Intentalo de nuevo
        
        """)
    

    s=((4*l*In)/(110* 2))


    if( s < 0.8235):
        calibre2=18
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(.8235<= s) and (s < 1.307):
        calibre2=16
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(1.307<= s)  and (s < 2.08):
        calibre2=14
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(2.08<= s) and (s < 3.307):
        calibre2=12
        if(calibre1>=calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(3.307<= s) and (s < 5.26):
        calibre2=10
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(5.26<= s) and (s < 8.367):
        calibre2=8
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(8.367<= s) and (s < 13.3):
        calibre2=6
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(13.3<= s) and (s < 21.15):
        calibre2=4
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    elif(21.15<= s) and (s < 26.67):
        calibre2=3
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(26.67<= s) and (s < 33.62):
        calibre2=2
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
        
    else:
        print("Calibre no enocntrado, Intenta de nuevo ")
    
    my_Id= 1.4* ipc
    if(my_Id<15):
        tmagnetico=15
        mess=1
    elif(15<=my_Id) and (my_Id<20):
        tmagnetico=20
        mess=1
    elif(20<=my_Id) and (my_Id<30):
        tmagnetico=30
        mess=1
    elif(30<=my_Id) and (my_Id<50):
        tmagnetico=50
        mess=1
    elif(50<=my_Id) and (my_Id<60):
        tmagnetico=60
    if(mess==1):
        print("Para esta instalacion se requiere un Interruptor Termodinámico de ", tmagnetico, " Amp")
    else:
        print("No se encontro un interruptor termomagnetico adecuado, intenta de nuevo")
    
#Se imprime el ticket
    my_ticket = int(input("Presione 1 para imprimir ticket ..."))
    if(my_ticket==1):
     print("""

    ======================================================================================================================================    
    ======================================================================================================================================
    ======================================================================================================================================



    El departamento de mantenimiento de la Empresa X solicita al departamento de compras lo siguiente:
    
    Cable calibre #""",calibrefinal, """THW Ang 75° Marca ACME
    
    Interruptor termodinámico de """, tmagnetico,""" Amp. Marca ACME
    
    Todo esto con el propósito de finalizar nuestras funciones como departamento. 
    
    Esperamos la pronta respuesta del departamento de compras a fin de no retrasar las tareas ya agendadas para este bimestre
    
    Att. Lic. Patito Diaz. 
    Director de mantenimiento
    
    ======================================================================================================================================    
    ======================================================================================================================================
    ======================================================================================================================================"""
    )







    # ================================================================================== #
    # ================================================================================== #
    # ========== EMPEZAMOS A HACER LAS OPERACIONES SI LA RED ES TRIFASICA 3H  ========== #
    # ================================================================================== #
    # ====================================C____Ↄ======================================== #

    
elif option== 3:
    print("Entro a la opcion TRIFASICA")

    hp = float(input("Introduce los caballos de fueza:        "))
    efic = float(input("Introduce la eficiencia         "))
    fp = .90
    l = float (input("Introduce la distancia en metros:             "))


    
    ipc = ((hp * 746) / (efic * 220 * fp) ) 
    In = (1.25 * ipc)

    if (In<20):
        calibre1 = 14
        
    elif ( 20>= In <25):
        calibre1 = 12
    elif ( 25>= In < 35 ):
        calibre1 = 10
    elif ( 35 >= In < 50):
        calibre1= 8
    elif ( 50>= In < 65 ):
        calibre1 = 6
    elif ( 65>= In < 85 ):
        calibre1 = 4
    elif ( 85>= In < 100 ):
        calibre1 = 3
    elif ( 100>= In < 115 ):
        calibre1 = 2
    elif ( 115>= In < 130 ):
        calibre1 = 1

    else:
        print("""
        
        Lamentablemente la calculadora malota de calibres detecto datos erroneos 
        
        Intentalo de nuevo
        
        """)
    e=1
    s=((2*l*In)/(220* e))

    if( s < 0.8235):
        calibre2=18
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(.8235<= s) and (s < 1.307):
        calibre2=16
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(1.307<= s)  and (s < 2.08):
        calibre2=14
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(2.08<= s) and (s < 3.307):
        calibre2=12
        if(calibre1>=calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(3.307<= s) and (s < 5.26):
        calibre2=10
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(5.26<= s) and (s < 8.367):
        calibre2=8
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(8.367<= s) and (s < 13.3):
        calibre2=6
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(13.3<= s) and (s < 21.15):
        calibre2=4
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    elif(21.15<= s) and (s < 26.67):
        calibre2=3
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(26.67<= s) and (s < 33.62):
        calibre2=2
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
        
    else:
        print("Calibre no enocntrado, Intenta de nuevo ")
    #Se empiezan a hacer los calculos para el Id y obtener el interruptor termodinamico correcto 

    my_Id= 1.4* ipc
    print("Id= ",my_Id)
    if(my_Id<15):
        tmagnetico=15
        mess=1
    elif(15<=my_Id) and (my_Id<20):
        tmagnetico=20
        mess=1
    elif(20<=my_Id) and (my_Id<30):
        tmagnetico=30
        mess=1
    elif(30<=my_Id) and (my_Id<40):
        tmagnetico=40
        mess=1
    elif(40<=my_Id) and (my_Id<50):
        tmagnetico=50
        mess=1
    elif(50<=my_Id) and (my_Id<60):
        tmagnetico=60
        mess=1
    elif(60<=my_Id) and (my_Id<100):
        tmagnetico=100
        mess=1
    elif(100<=my_Id) and (my_Id<125):
        tmagnetico=125
        mess=1
    elif(125<=my_Id) and (my_Id<150):
        tmagnetico=150
        mess=1
    elif(200<=my_Id) and (my_Id<225):
        tmagnetico=225
        mess=1
    elif(300<=my_Id) and (my_Id<400):
        tmagnetico=400
        mess=1
    elif(400<=my_Id) and (my_Id<500):
        tmagnetico=500
        mess=1
    elif(500<=my_Id) and (my_Id<750):
        tmagnetico=750
        mess=1
    elif(750<=my_Id) and (my_Id<800):
        tmagnetico=800
        mess=1
    elif(1000<=my_Id) and (my_Id<1250):
        tmagnetico=1250
        mess=1
    elif(1250<=my_Id) and (my_Id<1500):
        tmagnetico=1500
        mess=1
    elif(1500<=my_Id) and (my_Id<2000):
        tmagnetico=2000
        mess=1
    else:
        if(my_Id>=2000):
            print("Para esta instalación se requiere de un Interruptor Termódinamico Especial")
            mess=0
        else:
            print("No se encontro un interruptor termodinamico adecuado, por favor intenta de nuevo")

        
    if(mess==1):
        print("Para esta instalacion se requiere un Interruptor Termodinámico de ", tmagnetico, " Amp")
    

#Se imprime el ticket
    my_ticket = int(input("Presione 1 para imprimir ticket ..."))
    if(my_ticket==1):
      print("""

    ======================================================================================================================================    
    ======================================================================================================================================
    ======================================================================================================================================



    El departamento de mantenimiento de la Empresa X solicita al departamento de compras lo siguiente:
    
    Cable calibre #""",calibrefinal, """THW Ang 75° Marca ACME
    
    Interruptor termodinámico de """, tmagnetico,""" Amp. Marca ACME
    
    Todo esto con el propósito de finalizar nuestras funciones como departamento. 
    
    Esperamos la pronta respuesta del departamento de compras a fin de no retrasar las tareas ya agendadas para este bimestre
    
    Att. Lic. Patito Diaz. 
    Director de mantenimiento
    
    ======================================================================================================================================    
    ======================================================================================================================================
    ======================================================================================================================================"""
    )


    # ================================================================================== #
    # ================================================================================== #
    # ========== EMPEZAMOS A HACER LAS OPERACIONES SI LA RED ES TRIFASICA 4H  ========== #
    # ================================================================================== #
    # ====================================*____*======================================== #




elif option == 4:
    

    w = float(input("Introduce el dato de potencia en watts:        "))
    fd = .85
    fp = .90
    l = float (input("Introduce la distancia en metros:             "))

    ipc=((w*fd)/(1.73 * 220 * fp))
    In= 1.25 * ipc
    if (In<20):
        calibre1 = 14
        
    elif ( 20>= In <25):
        calibre1 = 12
    elif ( 25>= In < 35 ):
        calibre1 = 10
    elif ( 35 >= In < 50):
        calibre1= 8
    elif ( 50>= In < 65 ):
        calibre1 = 6
    elif ( 65>= In < 85 ):
        calibre1 = 4
    elif ( 85>= In < 100 ):
        calibre1 = 3
    elif ( 100>= In < 115 ):
        calibre1 = 2
    elif ( 115>= In < 130 ):
        calibre1 = 1

    else:
        print("""
        
        Lamentablemente la calculadora malota de calibres detecto datos erroneos 
        
        Intentalo de nuevo
        
        """)
    e=1
    s=((2 * 1.73 * l * In )/(220*e))

    print("S=", s)

    if( s < 0.8235):
        calibre2=18
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(.8235<= s) and (s < 1.307):
        calibre2=16
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(1.307<= s)  and (s < 2.08):
        calibre2=14
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(2.08<= s) and (s < 3.307):
        calibre2=12
        if(calibre1>=calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(3.307<= s) and (s < 5.26):
        calibre2=10
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(5.26<= s) and (s < 8.367):
        calibre2=8
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    
    elif(8.367<= s) and (s < 13.3):
        calibre2=6
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(13.3<= s) and (s < 21.15):
        calibre2=4
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1
    elif(21.15<= s) and (s < 26.67):
        calibre2=3
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
            calibrefinal=calibre1

    elif(26.67<= s) and (s < 33.62):
        calibre2=2
        if(calibre1>= calibre2):
            print("El calibre que necesitas es: #", calibre2, "THW Ang 75°")
            calibrefinal=calibre2
        else:
            print("El calibre que necesitas es: #", calibre1, "THW Ang 75°")
        
    else:
        print("Calibre no enocntrado, Intenta de nuevo ")



#Se empiezan a hacer los calculos para el Id y obtener el interruptor termodinamico correcto 

    my_Id= 1.4* ipc
    print("Id= ",my_Id)
    if(my_Id<15):
        tmagnetico=15
        mess=1
    elif(15<=my_Id) and (my_Id<20):
        tmagnetico=20
        mess=1
    elif(20<=my_Id) and (my_Id<30):
        tmagnetico=30
        mess=1
    elif(30<=my_Id) and (my_Id<40):
        tmagnetico=40
        mess=1
    elif(40<=my_Id) and (my_Id<50):
        tmagnetico=50
        mess=1
    elif(50<=my_Id) and (my_Id<60):
        tmagnetico=60
        mess=1
    elif(60<=my_Id) and (my_Id<100):
        tmagnetico=100
        mess=1
    elif(100<=my_Id) and (my_Id<125):
        tmagnetico=125
        mess=1
    elif(125<=my_Id) and (my_Id<150):
        tmagnetico=150
        mess=1
    elif(200<=my_Id) and (my_Id<225):
        tmagnetico=225
        mess=1
    elif(300<=my_Id) and (my_Id<400):
        tmagnetico=400
        mess=1
    elif(400<=my_Id) and (my_Id<500):
        tmagnetico=500
        mess=1
    elif(500<=my_Id) and (my_Id<750):
        tmagnetico=750
        mess=1
    elif(750<=my_Id) and (my_Id<800):
        tmagnetico=800
        mess=1
    elif(1000<=my_Id) and (my_Id<1250):
        tmagnetico=1250
        mess=1
    elif(1250<=my_Id) and (my_Id<1500):
        tmagnetico=1500
        mess=1
    elif(1500<=my_Id) and (my_Id<2000):
        tmagnetico=2000
        mess=1
    else:
        if(my_Id>=2000):
            print("Para esta instalación se requiere de un Interruptor Termódinamico Especial")
            mess=0
        else:
            print("No se encontro un interruptor termodinamico adecuado, por favor intenta de nuevo")

        
    if(mess==1):
        print("Para esta instalacion se requiere un Interruptor Termodinámico de ", tmagnetico, " Amp")


    
    my_ticket = int(input("Presione 1 para imprimir ticket ..."))
    if(my_ticket==1):
     print("""

    ======================================================================================================================================    
    ======================================================================================================================================
    ======================================================================================================================================



    El departamento de mantenimiento de la Empresa X solicita al departamento de compras lo siguiente:
    
    Cable calibre #""",calibrefinal, """THW Ang 75° Marca ACME
    
    Interruptor termodinámico de """, tmagnetico,""" Amp. Marca ACME

    
    Todo esto con el propósito de finalizar nuestras funciones como departamento. 
    
    Esperamos la pronta respuesta del departamento de compras a fin de no retrasar las tareas ya agendadas para este bimestre
    
    Att. Lic. Patito Diaz. 
    Director de mantenimiento
    
    ======================================================================================================================================    
    ======================================================================================================================================
    ======================================================================================================================================"""
    )

else:
    print("Opcion Inválida")



