from struct import *

#stores as bytes data

packed_data=pack('iif',6,9,12.75)         #two integers and a float
print(packed_data)          #this is how you transfer data over network

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#to get byte date back to normal

orig=unpack('iif',packed_data)
print(orig)

