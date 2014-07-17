% -*- Prolog -*-

%% ?- size([a,b,c,d,e], R).
%% R = 5.

%% ?- delete(d, [a,b,c,d,e], R).
%% R = [a, b, c, e] 

%% ?- reverse([a,b,c,d,e], R).
%% R = [e, d, c, b, a].

%% ?- palindrome([1,2,3,2,1]).
%% true.

size([],0).

size([_|T],R):-
    size(T, R1),
    R is R1+1.

delete(X, [X|T], T).
delete(X, [H|T], [H|NT]) :- 
    delete(X, T, NT).

reverse([],[]).
reverse([H|T],L):-
    reverse(T,R),
    append(R,[H],L).

palindrome(L):-
    reverse(L,L).
