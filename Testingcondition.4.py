a=1
b=3
print('variable a is:','one'if(a==1)else'not one')
print('variable a is:','odd'if(a%2!=0)else'even')
print('\nvariable b is:','one'if(b==1)else'not one')
print('variable b is:','odd'if(b%2!=0)else'even')
B=a if(b>a)else b
print(B)
