# npuzzle

This program solve n-puzzle game using A* algorithm. It's a _work in progress_.

## How to use this software?

First, we need to compile `Cython` code to `.c`.

```
python3 setup.py build_ext --inplace
```

Then:

```
python3 main.py
```

## Tips

With `Cython`, use:

```
cython file.pyx -a
```

To generate `.html` file with Cython's annotation telling you where your program is taking time.
