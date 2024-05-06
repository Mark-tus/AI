/*WAP to implement factorial, Fibonacci of a given number using
PROLOG.*/

%Factorial
factorial(0,1).
factorial(N,Result):-
 N>0,
 N1 is N-1,
 factorial(N1,Result1),
 Result is N*Result1.

%Fibonacci
fibo(0,0).
fibo(1,1).
fibo(N,Result):-
 N>1,
 N1 is N-1,
 N2 is N-2,
 fibo(N1,Result1),
 fibo(N2,Result2),
 Result is Result1+Result2.
