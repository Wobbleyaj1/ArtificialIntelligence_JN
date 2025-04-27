animal(dog)  :- is_true('has fur'), is_true('says woof').
animal(cat)  :- is_true('has fur'), is_true('says meow').
animal(duck) :- is_true('has feathers'), is_true('says quack').
animal(mouse) :- is_true('is small'), is_true('says squeak').
animal(bear) :- is_true('is large'), is_true('has cubs').
animal(alligator) :- is_true('is green'), is_true('can swim').

is_true(Q) :-
        format("~w?\n", [Q]),
        read(yes).
