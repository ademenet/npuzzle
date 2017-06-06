all:
	python3 setup.py build_ext --inplace

clean:
	rm -f goal_generator.c goal_generator.so
	rm -f heuristic.c heuristic.so
	rm -f isSolvable.c isSolvable.so

re: clean all
