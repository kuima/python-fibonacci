=========
Fibonacci
=========

This is a Python project template using Fibonacci number as example, well organized with package, configuration, testing, and documentation. It's very suitable as the starting point for a new project.

Structure
---------

::

    ROOT
    │
    ├── .gitignore ┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Git configuration to ignore files
    │
    ├── COMMANDS ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Instruction of common commands
    │
    ├── LICENSE ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ License declaration
    │
    ├── MANIFEST.in ┄┄┄┄┄┄┄┄┄┄┄┄┄ List of additional files to attach
    │
    ├── README.rst ┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Project instruction
    │
    ├── setup.cfg ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Configurations
    │
    ├── setup.py ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Build script for setuptools
    │
    ├── requirements.txt ┄┄┄┄┄┄┄┄ Dependencies
    │
    ├── docs ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Documentation directory
    │   └── index.rst
    │
    ├── fibonacci ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Main package directory
    │   ├── __init__.py
    │   │
    │   └── bin ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Command line tools directory
    │       └── __init__.py
    │
    └── tests ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄ Unit tests directory
        ├── test_cli.py
        └── test_fibonacci.py

Usage
-----

From code:

.. code-block:: python

    import fibonacci

    f = fibonacci.compute(5)

From command line:

::

    $ fibonacci 5
    > [2020-03-03 12:34:56 +0800][fibonacci.bin][INFO] Fibonacci(5) = 5
