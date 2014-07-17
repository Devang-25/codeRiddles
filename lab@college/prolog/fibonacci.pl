% -*- Prolog -*-

%%%%%%%%%%%%%%%%%%%%%%%%%
%% Test case for IDEA 2
%% ?- fib(1,1,5).
%% 1
%% 1
%% 2
%% 3
%% 5
%%%%%%%%%%%%%%%%%%%%%%%%%
%% Test case for IDEA 3
%% ?- fib(1,5).
%% 1
%% 1
%% 2
%% 3
%% 5
%%%%%%%%%%%%%%%%%%%%%%%%%

%% IDEA 2 
fib(M,I,N):-
    M-1 > -2,
    print(M),
    print('\n'),
    N1 is N-1,
    L is M+I,
    print(L),
    print('\n'),
    fib2(M,L,N1).

%% %% IDEA 3
%% fib(M,N):-
%%     M-1 > -1,
%%     I is M-1,
%%     print(M),
%%     print('\n'),
%%     N1 is N-1,
%%     fib2(I,M,N1).

fib2(M,I,N):-
    L is M+I,
    print(L),
    N1 is N-1,
    N1>0,
    print('\n'),
    fib2(I,L,N1).

%% IDEA 1

%% fib(M,I,N):-
%%     M<2,
%%     M-1 > -2,
%%     write('....fib()....\n'),
%%     print('1\n'),
%%     fib2(M,I,N-1).

%% fib(M,I,N):-
%%     M>1,
%%     write('....fib2()....\n'),
%%     write(M),
%%     print('\n'),
%%     fib2(M,I,N-1).

