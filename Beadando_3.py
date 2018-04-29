#a második feladat
be = input("Adjon meg egy mondatot!")
str = be.split(" ")
tmb=[]
for i in range(len(str)):
    tmb.append(str[i])
leg=0
for i in range(0,len(tmb)):
    if len(tmb[i]) > len(tmb[leg]):
        leg = i
szelesseg = len(tmb[leg])
print((szelesseg+4)*"*")
for i in range(0,len(tmb)):
    tmb[i]+= (szelesseg-len(tmb[i]))*' '
    print("* {} *".format(tmb[i]))
print((szelesseg+4)*"*")




