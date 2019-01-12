from rsa import *

# Testing rsa.py

# Generating random primes
p = random_prime(2048)
q = random_prime(2048)
n = p*q
# calculates "e" and "d"
e = find_e(p,q)
d = find_d(e,p,q)


print("Prime p:" + str(p)+"\n\n")
print("Prime q:" + str(q)+"\n\n")
print("n = p*q:"+str(n)+"\n\n")
print("Key e: "+str(e)+"\n\n")
print("Key d: "+str(d)+"\n\n")

message = str(input('Input message to be encrypted: \n'))

print("Pre-coded message: "+str(message)+"\n\n")

M = encodes(message)
print('Encoded message: ' + str(M)+"\n\n")

encrypted_message = encrypt(M,n,e)
print("Encrypted message: " + str(encrypted_message)+"\n\n")

decrypted_message = decrypt(encrypted_message,n,d)
print("Decrypted message: "+ str(decrypted_message)+"\n\n")

decoded_message = decodes(decrypted_message)
print("Decoded message: "+str(decoded_message)+"\n\n")
