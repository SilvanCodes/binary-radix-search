
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

if __name__ == '__main__':
    import timeit
    import math
    import json
    from random import shuffle

    NUM_RUNS = 100
    SAMPLE_STEP_SIZE = int(1e5)
    MAX_SAMPLE_COUNT = int(1e6*5)
    GROUPS = 8

    results = {
        'binary-radix-sort': [],
        'time-sort': [],
        'sample_size': [],
        'sample_step': str(SAMPLE_STEP_SIZE),
        'max_sample_count': str(MAX_SAMPLE_COUNT),
        'number_of_runs': str(NUM_RUNS),
        'number_of_groups' : str(GROUPS)
    }

    print('expected sample sets: ' + str(int(MAX_SAMPLE_COUNT/SAMPLE_STEP_SIZE)))

    for sample_set, sample_size in enumerate(xrange(SAMPLE_STEP_SIZE, MAX_SAMPLE_COUNT + 1, SAMPLE_STEP_SIZE)):

        # see script working
        print('timing sample set no ' + str(sample_set))

        # generate samples
        samples = []

        if GROUPS:
            for group in xrange(GROUPS):
                # uniform distribution over groups
                samples += [group] * int(sample_size/GROUPS)
        else:
            # each sample will be unique
            samples = [i for i in xrange(sample_size)]

        # shuffle to sort afterwards
        shuffle(samples)

        # store normalized sample count
        results['sample_size'].append((sample_size/SAMPLE_STEP_SIZE))
        results['binary-radix-sort'].append(0)
        results['time-sort'].append(0)

        for runs in xrange(NUM_RUNS):
            # measure binary radix sort
            binary_radix_sort_samples = samples[:]
            t1 = timeit.default_timer()
            binary_radix_sort(binary_radix_sort_samples)
            t2 = timeit.default_timer()
            # store resulting time difference
            results['binary-radix-sort'][sample_set] += (t2-t1)

            # measure time sort
            time_sort_samples = samples[:]
            t1 = timeit.default_timer()
            sorted(time_sort_samples)
            t2 = timeit.default_timer()
            # store resulting time difference
            results['time-sort'][sample_set] += (t2-t1)

        # normalize collected times
        results['binary-radix-sort'][sample_set] /= NUM_RUNS
        results['time-sort'][sample_set] /= NUM_RUNS

    with open('results.json', 'w') as file:
        file.write(json.dumps(results))

    print('done')