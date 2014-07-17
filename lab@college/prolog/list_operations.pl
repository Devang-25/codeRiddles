% -*- Prolog -*-

size([],0).

size([_|T],R):-
    size(T, R1),
    R is R1+1.

delete(X, [X|T], T).
delete(X, [H|T], [H|NT]) :- 
    delete(X, T, NT).
