import math
    
def principal():

    G = 0.00000000006674

    Mp = 1.303e22

    Mc = 1.586e21

    Rp = 1.188e6

    Rc = 0.606e6

    hcero = 7.87e6

    xp = -2410000

    yp = 0

    xc = 17181000

    yc = 0
    
    R = float (input("R= "))
    
    aS = float (input("Angulo inicial= "))
    
    xs = R*math.cos(aS)
    ys = R*math.sin(aS)
    
    w = 0.00001139
    
    fxs = 100000 #los defino asi para entrar al ciclo while
    fys = 100000
    
    fs = math.sqrt( fxs**2 + fys**2 )
    
    while abs(fs) > 1e-5 and aS<(aS + math.pi*2):
            
        aP = 0

        aC = 0
        
        dP = math.sqrt ( ((xs - xp)**2) + ((ys - yp)**2) )

        dC = math.sqrt ( ((xs - xc)**2) + ((ys - yc)**2) )
        
        dS = math.sqrt ( (xs**2) + (ys**2) )

        fxP = G*Mp*math.cos(aP)/(dP**2)

        fxC = G*Mc*math.cos(aC)/(dC**2)
        
        fxCent = (w**2) * dS * math.cos(aS)

        fyP = G*Mp*math.sin(aP)/(dP**2)

        fyC = G*Mc*math.sin(aC)/(dC**2)
        
        fyCent = (w**2) * dS * math.sin(aS)

        if xp < xs:

            fxP = -fxP

        if yp < ys:

            fyP = -fyP

        if xc < xs:

            fxC = - fxC

        if yc < ys:

            fyC = - fyC
        
        if xs < 0:

            fxCent = -fxCent

        if ys < 0:

            fyCent = -fyCent
            
            
        fxs = fxP + fxC + fxCent
        fys = fyP + fyC + fyCent
        fs = math.sqrt( fxs**2 + fys**2 )
        
        
        aS = aS + 0.0000003
        xs = R*math.cos(aS)
        ys = R*math.sin(aS) 
        
        
    if aS < (math.pi*2):
    
        print (f"Posicion: R = {R} , Angulo = {aS} , Ft = {fs} , Fx: {fxs} , Fy: {fys}")
        
    else:
        
        print("Para el radio definido no hay ángulo que cumpla con las condiciones solicitadas\n")        
        
principal()
  

intento = input( "Desea probar otra configuración?: " )

while intento in ["Si", "si", "SI"]:

    principal()
 
    intento = input("Desea probar otra configuración?: ")

