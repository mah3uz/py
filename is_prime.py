def is_prime(n):
    '''Check if the number is Prime'''
    # make sure n is a positive integer.
    n = abs(int(n))

    # 0 and 1 is not prime.
    if n < 2:
        return False

    # 2 is the only even prime.
    if n == 2:
        return True

    # all other even numbers are not primes.
    if not n & 1:
        return False

    # range starts with 3 and only needs to go up
    # the square root of n for all odd numbers.
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

def whois_prime(n):
    '''Check if the number which number is Prime in range'''
    for i in range(n):
        # make sure n is a positive integer.
        i = abs(int(i))

        # 0 and 1 is not prime.
        if i < 2:
            return

        # 2 is the only even prime.
        if i == 2:
            return '{} is Prime.'.format(i)

        # all other even numbers are not primes.
        if not i & 1:
            return

        # range starts with 3 and only needs to go up
        # the square root of n for all odd numbers.
        for x in range(3, int(i**0.5) + 1, 2):
            if i % x == 0:
                return

        return '{} is Prime.'.format(i)


if __name__ == '__main__':
    is_prime(121)
    whois_prime(121)
