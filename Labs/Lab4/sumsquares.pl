sumsquares(1,1).
sumsquares(N,NSS) :-
	N>1,
	NMinus1 is N - 1,
	sumsquares(NMinus1,SSMinus1),
	NSS is N * N + SSMinus1.
