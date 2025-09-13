'''def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
 
func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)'''

'''t=(1,)
t+=(3,4)
print("Tuple:" ,t)
print("Max value:",max(t))'''

'''
a=(1,2,3)
b=('A','B','C')
c=zip(a,b)
print(tuple(c))'''


s = {i+j for i in range(3) for j in range(3) if i*j ==0}
print(s)