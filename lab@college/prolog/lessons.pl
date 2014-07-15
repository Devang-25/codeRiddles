% -*- Prolog -*-

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
