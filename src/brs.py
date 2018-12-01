# args = ['j','i','o','b','y']

# bits = int(math.ceil(math.log(len(args),2))) # best-case, min bit size
# for b in range(0, 64): # worst-case, max bit size

def binary_radix_sort(args):
    pos = 0x01
    cont = 1
    bit_pos = 0

    while cont:
        one = []
        zero = []
        cont = 0
        pos = 1 << bit_pos
        bit_pos += 1
        
        for n in args:
            cont = cont | (n >> bit_pos)
            if n & pos:
                one.append(n)
            else:
                zero.append(n)
        args = zero + one

    return args

def hex_radix_sort(args):

    max_key_length = int(math.ceil(math.log(len(args),16)))

    form = '%0' + str(max_key_length) + 'x'

    for pos in range(0, max_key_length):
        buckets = { '0': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], 'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [] }
        for n in args:
            buckets[list(form % n)[::-1][pos]].append(n)
        args = buckets['0'] + buckets['1'] + buckets['2'] + buckets['3'] + buckets['4'] + buckets['5'] + buckets['6'] + buckets['7'] + buckets['8'] + buckets['9'] + buckets['a'] + buckets['b'] + buckets['c'] + buckets['d'] + buckets['e'] + buckets['f']
    return args


if __name__ == '__main__':
    import timeit
    import math
    from random import shuffle

    items = int(1e6)
    # args = [i for i in range(items)]

    args = []
    groups = 8
    for i in xrange(groups):
        args += [i] * int(items/groups)

    # args = ( [1] * (items/2) ) + ( [2] * (items/2) )

    print('sorting ' + str(items) + ' items')
    t1 = timeit.default_timer()
    shuffle(args)
    t2 = timeit.default_timer()
    print('shuffled [ms]: ' + str(t2-t1))

    t1 = timeit.default_timer()
    res2 = sorted(args[:])
    t2 = timeit.default_timer()
    # print(res2)
    print('sort [ms]: ' + str(t2-t1))

    # print(args)
    t1 = timeit.default_timer()
    res1 = binary_radix_sort(args[:])
    t2 = timeit.default_timer()
    # print(res1)
    print('brs [ms]: ' + str(t2-t1))

    # print(args)
    # t1 = timeit.default_timer()
    # res3 = hex_radix_sort(args[:])
    # t2 = timeit.default_timer()
    # print(res3)
    # print('hrs [ms]: ' + str(t2-t1))

    
