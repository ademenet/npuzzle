all:
	python setup.py build_ext --inplace

clean:
	rm -f goal_generator.c goal_generator.so

re: clean all
