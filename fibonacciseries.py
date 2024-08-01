def fibo(n):
    f1=-1
    f2=1
    for i in range(n):
        f3=f1+f2
        print(f3)
        f1=f2
        f2=f3
    
fibo(int(input("How many numbers is the Fibonacci series do you want to print?")))  #print the first 10 numbers in fibonacci series