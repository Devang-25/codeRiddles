% -*- Prolog -*-

edible(chocolates).
edible(fruit).
edible(water).
edible(toffees).
edible(gourd).

tastes(chocolates, sweet).
tastes(fruit, sweet).
tastes(gourd, bitter).
tastes(toffees, sweet).

%% likes(prakash, X):- 
%%     %% print('\nin 1st likes.\n'),
%%     edible(X), 
%%     tastes(X, sweet).

likes(prakash, X):- 
    %% print('\nin 2nd likes.\n'),
    edible(X), 
    tastes(X, sweet),
    write(X),
    nl,
    fail.
