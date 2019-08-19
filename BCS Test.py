#!/usr/bin/python

#Given a positive integer _n_,
#print every number from n downwards to 1 and if the number is divisible by 4 print `(ノಠ益ಠ)ノ`
#and if the number is divisible by 6 print `彡┻━┻`.
#If the number is divisible by 4 and 6 print `(ノಠ益ಠ)ノ彡┻━┻`.

# Get an input number
N = int(input ('Please input a positive integer: '))

# Check if the input number can be divisible by 4 or 6 through loop
for i in range(N, 0, -1):
    # the number can be divisible by 4 not 6
    if i % 4 == 0 and i % 6 != 0:
        print (str(i) + ' ' + '(ノಠ益ಠ)ノ')
        
    # the number can be divisible by 6 not 4
    elif i % 4 != 0 and i % 6 == 0:
        print (str(i) + ' ' + '彡┻━┻')
        
    # the number can be divisible by 4 and 6
    elif i % 4 == 0 and i % 6 == 0:
        print (str(i) + ' ' + '(ノಠ益ಠ)ノ彡┻━┻')
        
    # the number can not be divisible by 4 or 6
    else:
        print (str(i))
    
