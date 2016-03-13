% -*- Prolog -*-

arith(A,B,C):-
    C is A+B,
    write('Addition is: ').

arith(A,B,C):-
    C is A-B,
    write('Subtraction is: ').

arith(A,B,C):-
    C is A*B,
    write('Multiplication is: ').

arith(A,B,C):-
    C is A/B,
    write('Division is (Type: /): ').

arith(A,B,C):-
    C is A//B,
    write('Division is (Type: //): ').
