def generateKeys(p, q):
    n = p*q
    m = (p-1)*(q-1)
    e, d = math.getRelativePrime(m)
    return (e, n), (d, n), m



def getNums():
    p, q = 0, 0
    p = int(input('type a prime number or -1 if you want a random generation: '))
    if p == -1:
        p = math.generatePrime()
        q = math.generatePrime()
        print('Prime numbers were generated')
        print(p, q)
    else:
        q = int(input('type another number: '))
        if not(math.isPrime(p) and math.isPrime(q)):
            print('P or Q are not prime, please try again')
            return getNums()


    return p, q

    
import sys
import mathFuncs as math

sys.setrecursionlimit(10**5)

if __name__ == '__main__':
    print('RSA KEYS GENERATOR')
    p, q = getNums()
    publicKey, privateKey, m = generateKeys(p, q)
    print(publicKey, privateKey)
        


