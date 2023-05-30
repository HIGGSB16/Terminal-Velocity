def v(t):
    from math import e
    g = 9.8
    c = 12.5
    vt = (((g*m)/c) * (1 - (e**(-1*(c/m)*t))))
    v = round(vt,2)
    return v

# Main Program

m = float(input("m = "))
t = 1
while t <= 2:
    print(v(t))
    t += 0.1
