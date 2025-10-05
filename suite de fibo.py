def fibo (n):
    if n==0 or n==1:
        return n
    else :
        k= fibo(n-1)+fibo(n-2)
        return k
    
k= fibo (10)  
print("la valeur est ",k)       
     
     