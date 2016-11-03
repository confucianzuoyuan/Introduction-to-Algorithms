def compute_prefix_function(P):
    m = len(P)
    pi = [0] * m
    pi[0] = 0
    k = 0
    for q in range(1, m):
        while k > 0 and P[k] != P[q]:
            k = pi[k]
        if P[k] == P[q]:
            k = k + 1
        pi[q] = k
    return pi

def kmp_matcher(T, P):
    n = len(T)
    m = len(P)
    pi = compute_prefix_function(P)
    q = 0
    for i in range(n):
        while q>0 and P[q]!=T[i]:
            q = pi[q]
        if P[q] == T[i]:
            q = q + 1
        if q == m:
            print "pattern occurs with shift: %d" % (i-m+1)
            q = pi[q-1]

if __name__ == "__main__":
    P = "abab"
    print compute_prefix_function(P)
    kmp_matcher('abcabcabc','abc')
