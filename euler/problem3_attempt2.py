

def largest_prime_factor( n ):
    f = 2
    while f * f <= n:
        if n % f == 0:
            n = n // f
        else:
            f = f + 1

    return n

def is_prime( number ):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True


if __name__  == "__main__":
    # number = input( "Enter number: ",  )
    # number = int( number )

    for number in [1,2,3,4,5,6,7,8,9,10,27,81,19,51,600851475143]:
        largest_prime = largest_prime_factor( number )
        print( number, largest_prime, is_prime( largest_prime ))