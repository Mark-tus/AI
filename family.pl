//Program to demonstrate family relationship.

parent( pam, bob).
parent( tom, bob).
parent( tom, liz).
parent( bob, ann).
parent( bob, pat).
parent( pat, jim).
female( pam).
male(tom).
male(bob).
female(liz).
female(ann).
female(pat).
male(jim).
offspring( Y, X) :-
 parent( X, Y).
mother( X, Y) :-
 parent( X, Y),
 female( X).
father( X, Y) :-
 parent( X, Y),
 male( X).
grandparent(X, Z) :-
 parent( X, Y),
 parent( Y, Z).
grandmother(X, Z) :-
 parent( X, Y),
 parent( Y, Z),
 female(X).
grandfather(X, Z) :-
 parent( X, Y),
 parent( Y, Z),
 male(X).
grandchild(X,Y):-
 parent(Z,X),
 parent(Y,Z).
sister( X, Y) :-
 parent( Z, X),
 parent( Z, Y),
 female( X),
 different( X, Y).
brother( X, Y) :-
 parent( Z, X),
 parent( Z, Y),
 male( X),
 different( X, Y).
different(X, Y) :-
 X \= Y.
predecessor(X, Z) :-
 parent( X, Z).
predecessor( X, Z) :-
 parent( X, Y),
 predecessor(Y,Z).
hasachild(X):-
 parent(X,Y).
