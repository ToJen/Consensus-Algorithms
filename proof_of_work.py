# simple implementation of the Proof of Work consensus algorithm

import sys
import time
import hashlib
from struct import unpack, pack

#information on a block
timestamp = str(time.time())
message = "demo"
payload = timestamp + message

#perform and keep track of work done
nonce = 0
guess = 9999999999999
throttle = 1000000
target = 2**64 / throttle

payload_hash = hashlib.sha512(str(payload).encode('utf-8')).digest()

start = time.time()

while guess > target:
    nonce+1       #increment before attempting to solve in order to prove work done
    guess, = unpack('>Q', hashlib.sha512(hashlib.sha512(pack('>Q', nonce) + payload_hash).digest()).digest()[0:8])


end = time.time()

print("%s\t:\t%s\t:\t%s\t:\t%s\t:\t%s\t:\t%s\t:\t%s" % (timestamp, message, nonce, guess, payload, target, end-start))
