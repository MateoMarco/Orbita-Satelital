import math

import matplotlib.pyplot as plt

def mov_circular (R, w, h, fi_cero):
    
    ds = w * R * h
            
    dfi = ds/R
    
    fi_uno = fi_cero + dfi
    
    x_uno = R * math.cos(fi_uno)
    
    y_uno = R * math.sin(fi_uno)
    
    return (x_uno, y_uno, fi_uno)
    

def principal():

    metodo = input ("1. Euler explicito \n2. RK 2 \n3. RK 4 \nElegir el metodo: ")

    G = 0.00000000006674

    Mp = 1.303e22

    Mc = 1.586e21

    Rp = 1.188e6

    Rc = 0.606e6

    hcero = 7.87e6

    paso = float( input ("Definir paso: "))

    it = int ( input ("Definir iteraciones: "))

    caronte = input ("Considerar Caronte? Si / No: ")

    if caronte in ["No","no","NO"]:

        Mc = 0

    xp = -2410000

    yp = 0
    
    fi_p = math.pi

    xc = 17181000

    yc = 0
    
    fi_c = 0

    xs = xp - hcero - Rp

    ys = 0

    vx = 0

    vy = float ( input ("Defina una velocidad de lanzamiento del satelite: "))

    posx = [xs]

    posy = [ys]

    Em = []

    Ec = []

    Ep = []
    
    rot = input ("Considerar rotacion entre Pluton y Caronte? Si / No: ")
    
    if rot in ["SI", "Si" ,"si"]:
        
        w = float ( input ("Defina velocidad de rotacion: "))
        
        posfi_p = [math.pi]
        
        posx_p = [xp]
        
        posy_p = [yp]
        
        posfi_c = [0]
        
        posx_c = [xc]
        
        posy_c = [yc]
        
    else:
        
        w = 0

    for i in range (it):

        aP = math.atan(abs( (yp - posy[i])/(xp - posx[i]) ) )

        aC = math.atan(abs( (yc - posy[i])/(xc - posx[i]) ) )
        
        aS = math.atan(abs (posy[i]/posx[i]) )

        dP = math.sqrt ( ((posx[i] - xp)**2) + ((posy[i] - yp)**2) )

        dC = math.sqrt ( ((posx[i] - xc)**2) + ((posy[i] - yc)**2) )
        
        dS = math.sqrt ( (posx[i]**2) + (posy[i]**2) )

        fxP = G*Mp*math.cos(aP)/(dP**2)

        fxC = G*Mc*math.cos(aC)/(dC**2)
        
        fxCent = (w**2) * dS * math.cos(aS)

        fyP = G*Mp*math.sin(aP)/(dP**2)

        fyC = G*Mc*math.sin(aC)/(dC**2)
        
        fyCent = (w**2) * dS * math.sin(aS)

        if xp < posx[i]:

            fxP = -fxP

        if yp < posy[i]:

            fyP = -fyP

        if xc < posx[i]:

            fxC = - fxC

        if yc < posy[i]:

            fyC = - fyC
        
        if posx[i] < 0:

            fxCent = -fxCent

        if posy[i] < 0:

            fyCent = -fyCent
        
        
        if metodo == '1':

            vx_uno = vx + paso*( fxP + fxC + fxCent )

            vy_uno = vy + paso*( fyP + fyC + fyCent )

            x_uno = posx[i] + paso*vx

            y_uno = posy[i] + paso*vy

            posx.append(x_uno)

            posy.append(y_uno)

            vx = vx_uno

            vy = vy_uno
            

        if metodo == '2':           

            dP_n = math.sqrt ( ((xp - (posx[i] + paso*vx))**2) + ((yp - (posy[i] + paso*vy))**2) )

            dC_n = math.sqrt ( ((xc - (posx[i] + paso*vx))**2) + ((yc - (posy[i] + paso*vy))**2) )

            dS_n = math.sqrt ( ((posx[i] + paso*vx)**2) + ((posy[i] + paso*vy)**2) )

            aP_n = math.atan(abs( (yp - (posy[i] + paso*vy))/(xp - (posx[i] + paso*vx)) ) )

            aC_n = math.atan(abs( (yc - (posy[i] + paso*vy))/(xc - (posx[i] + paso*vx)) ) )

            aS_n = math.atan(abs ((posy[i] + paso*vy)/(posx[i] + paso*vx)) )

            fxP_n = G*Mp*math.cos(aP_n)/(dP_n**2)

            fxC_n = G*Mc*math.cos(aC_n)/(dC_n**2)
            
            fxCent_n = (w**2) * dS_n * math.cos(aS_n)

            fyP_n = G*Mp*math.sin(aP_n)/(dP_n**2)

            fyC_n = G*Mc*math.sin(aC_n)/(dC_n**2)
            
            fyCent_n = (w**2) * dS_n * math.sin(aS_n)

            if xp < posx[i]:

                fxP_n = -fxP_n

            if yp < posy[i]:

                fyP_n = -fyP_n

            if xc < posx[i]:

                fxC_n = - fxC_n

            if yc < posy[i]:

                fyC_n = - fyC_n
            
            if posx[i] < 0:

                fxCent_n = -fxCent_n

            if posy[i] < 0:

                fyCent_n = -fyCent_n            

            q1_vx = paso*(fxC + fxP + fxCent)

            q2_vx = paso*(fxC_n + fxP_n + fxCent_n )

            q2_x = paso*(vx + q1_vx)

            vx_uno = vx + 0.5*(q1_vx + q2_vx)

            q1_vy = paso*(fyC + fyP + fyCent)

            q2_vy = paso*(fyC_n + fyP_n + fyCent_n)

            q2_y = paso*(vy + q1_vy)
                
            vy_uno = vy + 0.5*(q1_vy + q2_vy)

            x_uno = posx[i] + 0.5*(paso*vx + q2_x)

            y_uno = posy[i] + 0.5*(paso*vy + q2_y)

            posx.append(x_uno)

            posy.append(y_uno)

            vx = vx_uno

            vy = vy_uno
            

        if metodo == '3':

            z = 0

            q_x = []

            q_vx = []

            q_y = []

            q_vy = []

            qn_x = 1

            qn_vx = 1

            qn_y = 1

            qn_vy = 1 

            for n in range (1,5):

                dP_n = math.sqrt ( ((xp - (posx[i] + z*qn_x))**2) + ((yp - (posy[i] + z*qn_y))**2) )

                dC_n = math.sqrt ( ((xc - (posx[i] + z*qn_x))**2) + ((yc - (posy[i] + z*qn_y))**2) )

                dS_n = math.sqrt ( ((posx[i] + z*qn_x)**2) + ((posy[i] + z*qn_y)**2) )

                aP_n = math.atan(abs( (yp - (posy[i] + z*qn_y))/(xp - (posx[i] + z*qn_x)) ) )

                aC_n = math.atan(abs( (yc - (posy[i] + z*qn_y))/(xc - (posx[i] + z*qn_x)) ) )

                aS_n = math.atan(abs ((posy[i] + z*qn_y)/(posx[i] + 0.5*qn_x)) )

                fxP_n = G*Mp*math.cos(aP_n)/(dP_n**2)

                fxC_n = G*Mc*math.cos(aC_n)/(dC_n**2)
                
                fxCent_n = (w**2) * dS_n * math.cos(aS_n)

                fyP_n = G*Mp*math.sin(aP_n)/(dP_n**2)

                fyC_n = G*Mc*math.sin(aC_n)/(dC_n**2)
                
                fyCent_n = (w**2) * dS_n * math.sin(aS_n)

                if xp < posx[i]:

                    fxP_n = -fxP_n

                if yp < posy[i]:

                    fyP_n = -fyP_n

                if xc < posx[i]:

                    fxC_n = - fxC_n

                if yc < posy[i]:

                    fyC_n = - fyC_n
                
                if posx[i] < 0:

                    fxCent_n = -fxCent_n

                if posy[i] < 0:

                    fyCent_n = -fyCent_n

                if n==1:

                    q_vx.append( paso*(fxC_n + fxP_n + fxCent_n) )

                    q_x.append( paso*vx )

                    q_vy.append( paso*(fyC_n + fyP_n + fyCent_n))

                    q_y.append( paso*vy )                   

                    qn_x = q_x[n-1]

                    qn_vx = q_vx[n-1]

                    qn_y = q_y[n-1]

                    qn_vy = q_vy[n-1]

                    z == 0.5

                if n==2:

                    q_vx.append( paso*(fxC_n + fxP_n + fxCent_n) )

                    q_x.append( paso*vx + z*q_vx[n-1])

                    q_vy.append( paso*(fyC_n + fyP_n + fyCent_n))

                    q_y.append( paso*vy + z*q_vy[n-1])
 
                    z = 0.5

                    qn_x = q_x[n-1]

                    qn_vx = q_vx[n-1]

                    qn_y = q_y[n-1]

                    qn_vy = q_vy[n-1]                    

                if n==3:

                    q_vx.append( paso*(fxC_n + fxP_n + fxCent_n) )

                    q_x.append( paso*vx + z*q_vx[n-1])

                    q_vy.append( paso*(fyC_n + fyP_n + fyCent_n))

                    q_y.append( paso*vy + z*q_vy[n-1])

                    z = 1

                    qn_x = q_x[n-1]

                    qn_vx = q_vx[n-1]

                    qn_y = q_y[n-1]

                    qn_vy = q_vy[n-1]

                if n==4:

                    q_vx.append( paso*(fxC_n + fxP_n + fxCent_n) )

                    q_x.append( paso*vx + z*q_vx[n-1])

                    q_vy.append( paso*(fyC_n + fyP_n + fyCent_n))

                    q_y.append( paso*vy + z*q_vy[n-1])                                  

            vx_uno = vx + 1/6*(q_vx[0] + 2*q_vx[1] + 2*q_vx[2] + q_vx[3])            

            vy_uno = vy + 1/6*(q_vy[0] + 2*q_vy[1] + 2*q_vy[2] + q_vy[3])

            x_uno = posx[i] + 1/6*(q_x[0] + 2*q_x[1] + 2*q_x[2] + q_x[3])

            y_uno = posy[i] + 1/6*(q_y[0] + 2*q_y[1] + 2*q_y[2] + q_y[3])

            posx.append(x_uno)

            posy.append(y_uno)

            vx = vx_uno

            vy = vy_uno        
            
        
        if w != 0:
            
            xp , yp , fi_p_uno = mov_circular ( 2410000 , w , paso , fi_p )
            
            posx_p.append(xp)
            
            posy_p.append(yp)
            
            posfi_p.append(fi_p_uno)
            
            xc , yc , fi_c_uno = mov_circular ( 17181000 , w , paso , fi_c )
            
            posx_c.append(xc)
            
            posy_c.append(yc)
            
            posfi_c.append(fi_c_uno)
            
            fi_p = fi_p_uno
            
            fi_c = fi_c_uno

            
##Esto lo utilizabamos para encontrar los errores de la trayectoria de la Parte 1.
            
        if i>0 and posx[i] < 0: 
            
            if paso < 50 and (-10000) < posy[i] < 10000:
                
                dAprox = abs( posx[i] - posx[0] )
                
                print (f"El satelite pasó por el punto ( {posx[i]} ; {posy[i]} ) en la iteracion {i}, y la distancia al punto inicial es {dAprox} ")
                
            if 49 < paso < 100 and (-50000) < posy[i] < 50000:
                
                dAprox = abs( posx[i] - posx[0] )
                
                print (f"El satelite pasó por el punto ( {posx[i]} ; {posy[i]} ) en la iteracion {i}, y la distancia al punto inicial es {dAprox} ")
                
            if paso > 99 and (-100000) < posy[i] < 100000:
                
                dAprox = abs( posx[i] - posx[0] )
                
                print (f"El satelite pasó por el punto ( {posx[i]} ; {posy[i]} ) en la iteracion {i}, y la distancia al punto inicial es {dAprox} ")

##Cálculo de las energías y su error
                
        if caronte in ["No", "no","NO"]:

            Ep.append(G*Mp/dP)

        if caronte in ["Si", "si", "SI"]:

            Ep.append(G*Mp/dP + G*Mc/dC)

        Ec.append(0.5*math.sqrt( (vx**2) + (vy**2) ))        
                    
        Em.append (Ec[i] + Ep[i])

    Em_in = Em [0]
    
    Em_min = min(Em)
        
    Em_max = max(Em)
        
    dEm = 100*(Em_max - Em_min)/( 0.5* (Em_max + Em_min)) 

    print (f"Tomando como referencia los puntos con máxima {Em_max}(iteración 0) y el de mínima {Em_min} energía mecánica, la diferencia porcentual o energía que se disipa entre estos es del {dEm}%. \n \n") 

    lista_it = []
    
    for i in range (it):

        lista_it.append(i)
                      
    plt.plot(lista_it,Ec, color='r')

    plt.plot(lista_it,Ep, color='b')

    plt.plot(lista_it,Em, color='g')

    plt.xlabel('Iteraciones')

    plt.ylabel('Energía')
    
    plt.show()

## Gráfico de la trayectoria
    
    plt.plot(posx,posy) 

    circle1=plt.Circle((xp,yp),1.188e6,color='r')

    fig = plt.gcf()
    
    fig.gca().add_artist(circle1)

    if caronte in ["Si","si","SI"]:

        circle2=plt.Circle((xc,yc),0.606e6,color='b')

        fig.gca().add_artist(circle2)

    fig.savefig('plotcircles.png')
       
    plt.xlabel('x')

    plt.ylabel('y')

    plt.title('Posición')

    plt.show()
                                               

principal()
  

intento = input( "Desea probar otra configuración?: " )

while intento in ["Si", "si", "SI"]:

    principal()
 
    intento = input("Desea probar otra configuración?: ")

    


