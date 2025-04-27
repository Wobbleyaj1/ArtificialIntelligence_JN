hassize(bluebird,small).

hascovering(bird,feathers).

hascolor(bluebird,blue).

hasproperty(bird,flies).

isa(bluebird,bird).
isa(bird,vertebrate).

isbird(Animal) :-
	hascovering(Animal,feathers),
	hasproperty(Animal,flies).
