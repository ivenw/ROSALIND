def mendels_first_law(K, M, N):
    '''Given: Three positive integers representing a population containing k+m+n organisms: k
    individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive

    Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.'''

    # define probablities for offspring having dominant allele of different matings
    K_K = 4/4
    M_M = 3/4
    N_N = 0/4
    K_M = 4/4
    K_N = 4/4
    M_N = 2/4

    offspring_prob = [K_K, M_M, N_N, K_M, K_N, M_N]
    mate_prob = []

    FIRST_POOL = K + M + N
    SECOND_POOL = FIRST_POOL - 1
    K_K_PROB = (K / FIRST_POOL) + (K-1)
    M_M_PROB = M / FIRST_POOL
    N_M_PROB = N / FIRST_POOL



    mate_prob.append()
    mate_prob.append(K * N)
    mate_prob.append(M * N)

    probability = 0
    for i in range(5) :
        probability += offspring_prob[i] * mate_prob[i]

    total_events = K * M * N

    return probability/total_events

if __name__ == '__main__' :
    print(mendels_first_law(2, 2, 2))
