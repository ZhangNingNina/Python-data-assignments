P=10**7
r=5/100/12
A=41680
month=0
outstanding=P
def print_one_month(month,outstanding):
    month=month+1
    interest=outstanding*r
    principal=A-interest
    outstanding=outstanding-principal
    print('{0:03d}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}'.format(month, A, interest, principal, outstanding))
    return month,outstanding
    
#for i in range(999999):
   # month,outstanding=print_one_month(month,outstanding)
    #if outstanding <= 0:
   #     break

#i=0
#while i < 999999:
#   i=i+1

while True:#want to do this forever
    month,outstanding=print_one_month(month,outstanding)
    #if outstanding<=0 then stop the loop
    if outstanding <= 0:
        break

headers = ['Month', 'Instalment', 'Interest', 'Principal', 'Outstanding']
for i in range(5):
    #print(i, 'th', 'header')
    print(headers[i],'\t',end='')
