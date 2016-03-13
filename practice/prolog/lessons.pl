% -*- Prolog -*-

%% http://www.anselm.edu/homepage/mmalita/culpro/index.html
%% http://www.cs.ccsu.edu/~markov/ccsu_courses/prolog.txt

has(jack,apples).
has(jack,car).
has(ann,plums).
has(dan,money).
fruit(apples).
fruit(plums).

%% load scripts like this [file_name]

%% if for example:
%% ?- has(X,Y).    
%% ..has multiple outputs, then use ; to proceed

%% has(jack,X).
%% has(jack,_).
%% has(X,apples),has(X,plums).
%% has(X,apples),has(Y,plums).
%% has(X,apples),has(X,plums).
%% has(X,plums).
%% fruit(Y).
%% listing(has).
%% has(X,Y),not(fruit(Y)).
