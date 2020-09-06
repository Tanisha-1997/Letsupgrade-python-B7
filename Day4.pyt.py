'''Armstrong Number between any two number'''


for num in range(1,200):
    n=num
    sum=0
    while n!=0:
        sum=sum+(n%10)**3
        n=n//10
    if num == sum:
        print('The Armstrong Number is:',num)
        break
else:
    print('No Armstrong Number Found')
    


