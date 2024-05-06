# /*Write a program to implement towers of Hanoi.*/
hanoi(N) :-
 move(N, left, center, right ).

move(0, _, _, _) :- !.
move(N, Source, Target, Aux) :-
 M is N - 1,
 move(M, Source, Aux, Target),
 format("Move disk ~w from ~w to ~w~n", [N, Source, Target]),
 move(M, Aux, Target, Source).

# alt
hanoi(1, Source, Target, _) :-
write('Move disk from '),
write(Source),
write(' to '),
write(Target),
nl.
hanoi(N, Source, Target, Auxiliary) :-
N > 1,
M is N - 1,
hanoi(M, Source, Auxiliary, Target),
hanoi(1, Source, Target, _),
hanoi(M, Auxiliary, Target, Source).
% Example usage:
% hanoi(3, 'A', 'C', 'B')