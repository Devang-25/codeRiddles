% -*- Prolog -*-

%% INPUT:
%% ?- radius(5,A,C).

%% OUTPUT:
%% Area is: 78.5
%% Circumference is: 31.400000000000002
%% A = 78.5,
%% C = 31.400000000000002.

radius(R,A,C):-
    A is (3.14 * R * R),
    C is (2 * 3.14 * R),
    write('\nArea is: '),
    print(A),
    write('\nCircumference is: '),
    print(C).
