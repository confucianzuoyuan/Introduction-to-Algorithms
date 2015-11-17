def finite_automaton_matcher(T, theta, m):
	n = len(T)
	q = 0
	for i in range(n):
		q = theta[(q, T[i])]
		if q == m:
			print "pattern occurs with shift: %d" % (i-m)

def compute_transition_function(P, Sigma):
	theta = {}
	m = len(P)
	for q in range(0, m+1):
		for a in Sigma:
			k = min(m+1, q+2)
			k = k - 1
			for i in range(k,-1,-1):
				if post_fix(P[:k], P[:q]+a):
					break
			theta[(q, a)] = k
	return theta

def post_fix(P1, P2):
	lp1 = len(P1)
	lp2 = len(P2)
	for i in range(lp1-1, -1, -1):
		if P1[i] != P2[i+lp2-lp1]:
			return False
	return True

if __name__ == "__main__":
	print post_fix('aaa', 'bbbaaa')
	theta = compute_transition_function('ababaca', 'abc')
	print theta
	finite_automaton_matcher('ababababaca', theta, 7)