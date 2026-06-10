# Day 18 Concepts: Command-Line Arguments and CLI Tools

Command-line arguments let users pass values when running a Python program.
This is useful for automation and real tools.

## 1) What is a CLI tool

A CLI tool is a program you run from terminal with arguments.

Example:
python script.py Pooja --times 3

## 2) argparse module

argparse is the standard library module for parsing command-line arguments.
It helps read positional arguments and options safely.

## 3) Positional vs optional arguments

Positional arguments:
- required and ordered
- example: name

Optional arguments:
- start with --
- example: --times, --shout

## 4) Common argparse parts

1. ArgumentParser() creates parser
2. add_argument() defines arguments
3. parse_args() reads terminal input

## 5) Argument types

1. type=str, int, float
2. action="store_true" for flags
3. choices=[...] to restrict valid values
4. default=... to provide fallback

## 6) Why CLI tools are useful

1. automate repetitive work
2. create reusable utilities
3. integrate with scripts and batch jobs
4. separate input from code

## 7) Common beginner mistakes

1. forgetting required positional argument
2. passing wrong type to option
3. dividing by zero without handling
4. confusing positional and optional order

## 8) Practice checklist

After Day 18, you should be able to:
1. create a parser
2. add positional and optional args
3. use flags like --verbose
4. validate choices
5. build a small CLI calculator
