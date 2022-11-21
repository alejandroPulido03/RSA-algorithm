def generateKeys(p, q):
    n = p*q
    m = (p-1)*(q-1)
    e, d = math.getRelativePrime(m)
    return (e, n), (d, n), m



def getNums():
    p, q = 0, 0
    times = [0,0]
    p = int(input('type a prime number or -1 if you want a random generation: '))
    if p == -1:
        times[0] = getTime()
        p = math.generatePrime()
        q = math.generatePrime()
        times[1] = getTime()
        print('Prime numbers were generated')
        print(p, f' ({len(str(p))})', q, f' ({len(str(q))})')
    else:
        q = int(input('type another number: '))
        times[0] = getTime()
        if not(math.isPrime(p) and math.isPrime(q)):
            print('P or Q are not primes, please try again')
            return getNums()
        times[1] = getTime()

    return p, q, times

def getTime():
    return float(time.perf_counter()*1000)

import sys
import mathFuncs as math
import time

sys.setrecursionlimit(10**5)

if __name__ == '__main__':
    print('RSA KEYS GENERATOR')

    
    p, q, times = getNums()
    print(f'Time obtained primes {round(times[1] - times [0], 2)}')
    start_keys_time = getTime()
    publicKey, privateKey, m = generateKeys(p, q)
    end_keys_time = getTime()
    print(f'Time obtained keys {round(end_keys_time - start_keys_time, 2)}')
    print('Public key: ', publicKey,'Private key: ', privateKey)
        


