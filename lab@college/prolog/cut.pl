% -*- Prolog -*-

do:-
    p(N),
    q(N),
    nl,
    write(N),
    !,
    r(N).

p(1).
p(2).
p(3).
p(4).

q(2).
q(3).
q(4).

r(3).

%% OUTPUT-1
%% ?- do.
%% 2
%% false.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% %% After adding this statement:
%% r(2).

%% OUTPUT-2
%% ?- do.
%% 2
%% true
