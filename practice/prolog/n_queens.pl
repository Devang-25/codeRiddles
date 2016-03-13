% -*- Prolog -*-

%% https://www.csupomona.edu/~jrfisher/www/prolog_tutorial/2_11.html
%% Refer to practice/8_queens_map_sample.py for sample solution array interpretation

/* prolog tutorial 2.11 Chess queens challenge puzzle */

perm([X|Y],Z) :- perm(Y,W), delete(X,Z,W).   
perm([],[]).

delete(X, [X|T], T).
delete(X, [H|T], [H|NT]) :-
    delete(X, T, NT).

solve(P) :-
     perm([1,2,3,4,5,6,7,8],P), 
     combine([1,2,3,4,5,6,7,8],P,S,D),
     all_diff(S),
     all_diff(D).

combine([X1|X],[Y1|Y],[S1|S],[D1|D]) :-
     S1 is X1 +Y1,
     D1 is X1 - Y1,
     combine(X,Y,S,D).
combine([],[],[],[]).

all_diff([X|Y]) :-  \+member(X,Y), all_diff(Y).
all_diff([X]).

%% %% Example:
%% ?- solve(P).
%% P = [5, 2, 6, 1, 7, 4, 8, 3] ;
%% P = [6, 3, 5, 7, 1, 4, 2, 8] ;
%% P = [6, 4, 7, 1, 3, 5, 2, 8] .

%% ?- setof(P,solve(P),Set), length(Set,L).
%% Set = [[1, 5, 8, 6, 3, 7, 2, 4], [1, 6, 8, 3, 7, 4, 2|...], [1, 7, 4, 6, 8, 2|...], [1, 7, 5, 8, 2|...], [2, 4, 6, 8|...], [2, 5, 7|...], [2, 5|...], [2|...], [...|...]|...],
%% L = 92.
