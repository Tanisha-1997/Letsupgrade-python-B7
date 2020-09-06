'''PILOT PROBLEM

A=float(input('enter the current altitude'))
if A<=1000:
    print('Land the plane')
elif 1000<A<5000:
    print('Come down to 1000')
else:
    print('Go round and try later')'''


'''Prime number between 1-200'''

for num in range(2,200):
    for i in range(2,(num//2)+1):
        if num%i==0:
            break
        else:
            print(num)
