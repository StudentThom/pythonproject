'''
Created on 24 jan. 2017
Assigment Introduction to binary numbers
@author: Thom
'''

def to_binary(getal):
    if getal == 0:
        return ''
    else:
        return to_binary(getal/2) + str(getal%2)

getal = to_binary(0)
print getal

def to_decimal(bin):
    lijst = map(int, str(bin))
    print lijst
    som = int(0)
    teller = 0
    for element in lijst:
        som += element * 2**(int(len(lijst))-teller-1)
        teller += 1
    return som                    
    print som
    
to_decimal(101010)

lijst = [
"1101000",
"1100101",
"1101100",
"1101100",
"1101111"
]
# By using your function to decimal you can now decode the message.
def binary_to_ascii(lst):
    msg = ""
    for b in lst:
        decimal_value = int(to_decimal(b))
        msg += chr(decimal_value)
    print(msg)

binary_to_ascii(lijst)