from sympy.ntheory.residue_ntheory import discrete_log

card_pub = 10212254
door_pub = 12577395
modulus = 20201227 

print(pow(door_pub, discrete_log(modulus, card_pub, 7), modulus))