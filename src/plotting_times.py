if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import json

    with open('results_10k_upto_5m_unique_cleaned.json') as f:
        results = json.load(f)

    fig = plt.figure()

    fig.suptitle('samples averaged over ' + results['number_of_runs'] + ' runs', fontsize=14)

    fig.subplots_adjust(hspace=0.5)
    
    ax1 = fig.add_subplot(111)
    ax1.set_title('binary-radix-sort (red), time-sort (blue), each key unique')
    ax1.set_ylabel('time (s)')
    ax1.set_xlabel('samples in ' + results['sample_step'])
    ax1.plot(results['sample_size'], results['binary-radix-sort'], 'ro', results['sample_size'], results['time-sort'], 'bo')

    """
    with open('results_10k_uptp_1m_8groups.json') as f:
        results = json.load(f)

    ax2 = fig.add_subplot(212)
    ax2.set_title('binary-radix-sort (red), time-sort (blue), 8 key groups')
    ax2.set_ylabel('time (s)')
    ax2.set_xlabel('samples in ' + results['sample_step'])
    ax2.plot(results['sample_size'], results['binary-radix-sort'], 'ro', results['sample_size'], results['time-sort'], 'bo')
    """

    plt.show()