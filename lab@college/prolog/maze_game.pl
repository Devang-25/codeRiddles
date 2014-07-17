% -*- Prolog -*-

%% Ref: http://cse3521.artifice.cc/prolog-examples.html#sec-3

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% %% OUTPUT
%% ?- play.
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): go west.
%% Garden
%% You are in the Garden. The trees and shrubs appear...
%% Type a command (or 'help'): go bizarre.
%% No exit that direction.
%% Garden
%% You are in the Garden. The trees and shrubs appear...
%% Type a command (or 'help'): go east.
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): go down.
%% Lair
%% You have found an apparently quite evil lair, of all things...
%% Type a command (or 'help'): quit.

%% true .
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

room(garden, 'Garden', 'You are in the Garden. The trees and shrubs appear...').
room(hallway, 'Hallway', 'You are in the Hallway. Dusty broken lamps and flower pots...').
room(kitchen, 'Kitchen', 'You are in the kitchen. Knives, pots, pans, ...').
room(library, 'Library', 'You are among many books in the Library...').
room(lair, 'Lair', 'You have found an apparently quite evil lair, of all things...').
connected(north, library, hallway).
connected(south, hallway, library).
%% connected(down, library, lair).
connected(down, library, lair) :- toggled(switch3).
connected(up, lair, library).
connected(west, library, garden).
connected(east, garden, library).
connected(west, hallway, kitchen).
connected(east, kitchen, hallway).


toggle(switch1) :- assertz(toggled(switch1)).

toggle(switch2) :- toggled(switch1), assertz(toggled(switch2)).

toggle(switch3) :- toggled(switch2), assertz(toggled(switch3)).

% this predicate has no inputs
print_location :-
    current_room(Current),
    room(Current, Name, Description),
    % nl means "newline"
    print(Name), nl, print(Description), nl.

:- dynamic current_room/1.

change_room(NewRoom) :-
    current_room(Current),
    retract(current_room(Current)),
    assertz(current_room(NewRoom)).

:- use_module(library(readln)).

:- prompt(_, 'Type a command (or ''help''): ').

strip_punctuation([], []).

strip_punctuation([Word|Tail], [Word|Result]) :-
    \+(member(Word, ['.', ',', '?', '!'])),
    strip_punctuation(Tail, Result).

strip_punctuation([_|Tail], Result) :-
    strip_punctuation(Tail, Result).

read_sentence(Input) :-
    % this is a special predicate from the readln library
    readln(Input1, _, ".!?", "_0123456789", lowercase),
    strip_punctuation(Input1, Input).

get_input :- read_sentence(Input), get_input(Input).
get_input([quit]).
get_input(Input) :-
    process_input(Input), print_location,
    read_sentence(Input1), get_input(Input1).

process_input([help]) :- print('Help...'), nl.

process_input([go, Direction]) :-
    current_room(Current),
    connected(Direction, Current, NewRoom),
    change_room(NewRoom).

process_input([go, _]) :-
    print('No exit that direction.'), nl.

process_input([_]) :-
    print('Huh?'), nl, nl.

:- dynamic toggled/1.

process_input([toggle, Switch]) :-
    toggle(Switch),
    % retrieve a set of switches that have been toggled
    setof(X, toggled(X), Switches),
    % print these
    print('Toggled switches: '), print(Switches), nl.

process_input([toggle, _]) :-
    print('Cannot toggle that switch.'), nl.


play :-
    retractall(current_room(_)), retractall(toggled(_)),
    assertz(current_room(library)),
    print_location,
    get_input.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% %% NEW OUTPUT

%% ?- play.
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): go down.
%% No exit that direction.
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): toggle switch3.
%% Cannot toggle that switch.
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): toggle switch2.
%% Cannot toggle that switch.
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): toggle switch1.
%% Toggled switches: [switch1]
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): toggle switch2.
%% Toggled switches: [switch1,switch2]
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): toggle switch3.
%% Toggled switches: [switch1,switch2,switch3]
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): go down.
%% Lair
%% You have found an apparently quite evil lair, of all things...
%% Type a command (or 'help'): go up.
%% Library
%% You are among many books in the Library...
%% Type a command (or 'help'): quit.

%% true .

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
