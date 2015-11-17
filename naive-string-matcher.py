def naive_string_matcher(T, P):
	n = len(T)
	m = len(P)
	for s in range(n-m+1):
		i = 0
		while i < m:
			if P[i] != T[s+i]:			
				break
			i = i + 1
		if i == m:
			print "pattern occurs with shift: %d" % s

if __name__ == "__main__":
	T = "aabaabaabaab"
	P = "aab"
	naive_string_matcher(T, P)