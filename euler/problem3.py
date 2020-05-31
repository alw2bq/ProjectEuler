# def get_max_factor(number)
#     max = 0
#
#     for n in range(1, (number // 2)):
#         if number % n == 0:
#             max = n
#     return max

def get_factors( number  ):
    factors = []
    for n in range(1, (number//2)):
        if number % n == 0:
            factors.append( n )
    return factors


def prime_factors( number ):
    prime_factors = []
    factors = get_factors( number )
    for n in factors:
        factors_of_factor = get_factors( n )
        if len( ( factors_of_factor ) ) <= 1:
            prime_factors.append( n )
    return prime_factors

def max_prime_factor( number ):
    prime_facts = prime_factors( number )
    maximum = max( prime_facts )

    return maximum




if __name__  == "__main__":
    number = input( "Enter number: ",  )
    number = int( number )

    print( max_prime_factor( number ))