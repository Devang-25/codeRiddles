% -*- Prolog -*-

table(N,M):- L is 1, 
	     loop(N,L,M).
loop(A,L,M):- X is A*L,
	      L<M,
	      L1 is L+1,
	      write(A),
	      write('x'),
	      write(L),
	      write('='),
	      write(X),
	      write('\n'),
	      loop(A,L1,M).
