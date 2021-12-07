suma=0
x=[]
l=[]
lista2=[]
lista1=[]
with open("Lista_clasei_11D.txt","r")as f:
    for i in f:
        x=i.split()
        l.append(x)
        if l[0][3]=='2':
            lista2.append(i.strip())
        elif l[0][3]=='1':
            lista1.append(i.strip())
        l.clear()
        suma+=int(x[2])
with open("Media_Clasei.txt","w")as m:
    m.write(f"Media clasei: {suma/30}")
with open("Grupa1.txt","w")as gr1:
    for elev1 in lista1:
        gr1.write(f"{elev1[0:-1]}\n")
with open("Grupa2.txt","w")as gr2:
    for elev2 in lista2:
        gr2.write(f"{elev2[0:-1]}\n")



    