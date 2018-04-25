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
for i in range(-1,len(tmb)+1):
    if i < 0:
        for i in range(0,szelesseg+4):
            print("*", end="")


    elif i > len(tmb)-1:
        for i in range(0,szelesseg+4):
            print("*", end="")
        break
    else:
        print("* {} *".format(tmb[i]))



