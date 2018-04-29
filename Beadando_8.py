first = input("Adja meg az első szót! ")
second = input("Adja meg a második szót! ")
els=[]
mas=[]
for i in first:
    els.append(i)
for i in second:
    mas.append(i)

k=0
kozos=[]
for i in range(0,len(els)):
    for j in range(k,len(mas)):
        if els[i] == mas[j] :
            kozos.append(mas[j])
            k+=1
vegso=""
for i in kozos:
    if i not in vegso:
        vegso+=i
print(kozos)
print(vegso)


