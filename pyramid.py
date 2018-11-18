'''
Draw pyramid using recursive function.
'''
def pyramid(N, i=0):
    if N > 0:
        print((N - 1) * ' ' + '*' * (i * 2 + 1))
        pyramid(N - 1, i + 1)

'''
Draw pyramid using string
'''
def pyramid_in_string(base):
    for i in range(1, base+1, 2):
        print('{:^{}}'.format('*' * i, base))


if __name__ == '__main__':
    pyramid(5)
    pyramid_in_string(10)
