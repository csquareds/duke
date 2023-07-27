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