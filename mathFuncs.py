def gcd(a, b):
    if(b==0) :
        return (a,1,0)
    (g,x,y) = gcd(b,a%b);
    q = a//b;
    return (g, y, x-q*y)


def generatePrime():
    import secrets
    bigNum = secrets.randbits(45) 
    bigNum = bigNum if bigNum % 2 != 0 else bigNum + 1
    if isPrime(bigNum):
        return bigNum
    return generatePrime()



def isPrime(bigNum):
    sqrtNum = int(bigNum**(1/2)) + 1
    isCompound = False
    div = 3
    
    if bigNum % 2 == 0 and bigNum > 2:
        return False

    while div < sqrtNum and not isCompound:
        isCompound = bigNum % div == 0
        div += 1

    return not isCompound

def getRelativePrime(num):
    e = 3
    p = gcd(e, num)
    while p[0] != 1:
        e += 2
        p = gcd(e, num)
    return e, p[1]