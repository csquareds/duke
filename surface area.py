def conc(C1,u1,C2,u2,V2):
    c1 = 1
    c2 = 1

    if u1 == 'ug' and u2 == 'mg':
        c1 = C1
        c2 = C2 * 1000
    elif u1 == 'mg' and u2 == 'ug':
        c1 = C1 * 1000
        c2 = C2
    else:
        c1 = C1
        c2 = C2

    V1 = c2 * V2 / c1
    return V1*1000 # volume in µL

def surfaceArea(value,d,stock,c): # value - conc (mg), d - diameter (nm), stock conc, final conc; for 1000 µL / 1 mL
    volume = conc(stock,'mg',c,'mg',1)
    total = 1000
    dilute = volume / total
    particles = value * dilute # from sheets
    diameter = d / 1e+6 # mm
    SA = 4 * π * (diameter/2)**2 # 4πr^2
    return particles*SA

def SA250(value,d,stock,c): # value mg, d in nm; for 250 µL
    volume = conc(stock,'mg',c,'mg',0.25)
    total = 250
    dilute = volume / total
    particles = value * dilute # from sheets
    diameter = d / 1e+6 # mm
    SA = 4 * π * (diameter/2)**2 # 4πr^2
    return particles*SA