n=int(input("what number do you want to calculate the power of? "))
x=int(input("What power do you want it to? "))
m=n
for i in range (0,x-1):
    m=m*n
print(m)