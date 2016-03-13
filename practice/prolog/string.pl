% -*- Prolog -*-

%% ?- strprint('Hello',5).
%% Hello
%% Hello
%% Hello
%% Hello
%% Hello
%% false.

strprint(X,N):-
    print(X),
    print('\n'),
    N>1,
    N1 is N-1,
    strprint(X,N1).
