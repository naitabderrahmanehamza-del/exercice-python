f= open("table_de_multiplication.txt","w+")
c=1
while c!= 10:
    f.write("table de multiplication de"+" "+str(c)+" "+"est"+"\n")
    for i in range(0,11):
       
        f.write(str(c)+"*"+str(i)+"="+str(c*i)+"\n")
    c+=1

    

