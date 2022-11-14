# WAD_documenting_example

Simple program for demonstrating:

 - comments
 - docstrings
 - pdoc

## The `README.md`

This file is also part of documentation of a program. It should
explain the purpose of the code and give information on how to use it,
the development environment, etc.

## Generating Documentation

Make sure you have `pdoc` installed you're in the root of the
repository, not in the src directory, unless you want to adjust the
paths in the commands below.

To view documentation in the terminal, use `pdoc ./src/cards.py`

To create an HTML document, use: `pdoc --force --html ./src/cards.py -o docs/` which will put `cards.html` into the `docs` directory.

There are many more options, which you can read about here: <https://pdoc3.github.io/pdoc/>

