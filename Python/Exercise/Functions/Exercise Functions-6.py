"""Implement Fibonacci sequence as recursive function and print first 5 elements."""

def Fibonacci(n):
    fibolist=[]
    for i in range(0,n):
        if i ==0:
            fibolist.append(0)
        elif i ==1:
            fibolist.append(1)
            
        else:  
            fibolist.append(fibolist[i-1]+fibolist[i-2])

           
    print(fibolist)        
              
           

    #print(fibolist[n-1])

 
 
Fibonacci(5)                   
           