import math
    
def principal():

    G = 0.00000000006674

    Mp = 1.303e22

    Mc = 1.586e21

    xp = -2410000

    yp = 0

    xc = 17181000

    yc = 0
    
    xs = float(input("xs= "))
    
    ys = 0
    
    w = 0.00001139
    
    fxs = 100000
    
    while abs(fxs) > 1e-9:

        aP = 0

        aC = 0
        
        aS = 0

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
        
        xs = xs + 1
        
        
    print (f"Posicion: {xs} , Fx: {fxs}")
        
        
principal()
  

intento = input( "Desea probar otra configuración?: " )

while intento in ["Si", "si", "SI"]:

    principal()
 
    intento = input("Desea probar otra configuración?: ")

