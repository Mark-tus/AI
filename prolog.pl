/*2) Write simple fact for the statements using PROLOG
•Ram likes mango.
•Seema is a girl.
•Bill likes Cindy.
•Rose is red.
•John owns
gold.*/

likes(ram, mango).
likes(bill, cindy).
is_a(seema, girl).
is_color(rose, red).
owns(john, gold).

/*Write predicates, one converts centigrade temperatures to Fahrenheit
using PROLOG.*/

celsius_to_fahrenheit(Celsius, Fahrenheit) :-
 Fahrenheit is (Celsius * 9/5) + 32.

//Write a program to solve the Monkey Banana problem using PROLOG.

move(state(middle, onbox, middle, hasnot),grasp,state(middle, onbox, middle, has)).
move(state(P, onfloor, P, H),climb,state(P, onbox, P, H)).
move(state(P1, onfloor, P1, H),drag(P1, P2),state(P2, onfloor, P2, H)).
move(state(P1, onfloor, B, H),walk(P1, P2),state(P2, onfloor, B, H)).
canget(state(_, _, _, has)).
canget(State1) :-
 move(State1, _, State2),
 canget(State2).
