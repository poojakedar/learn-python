# Day 11 Concepts: Modules and Project Structure

Day 11 teaches how to split code into multiple files like real projects.

## 1) What is a module

A module is a Python file containing functions, classes, or variables.

Example:
- day11_math_utils.py has math helper functions
- day11_modules_main.py imports and uses them

## 2) Why modules are useful

1. Keep code organized
2. Reuse functions in many files
3. Make large projects easier to manage
4. Improve readability and teamwork

## 3) Import basics

Import selected functions:
from module_name import function1, function2

Import full module:
import module_name

Then call function:
module_name.function1()

## 4) Good folder structure idea

For beginner projects:
1. lessons folder for concept demos
2. exercises folder for practice files
3. solutions folder for your answers
4. projects folder for full mini apps

## 5) Common module errors

1. ModuleNotFoundError:
- file name mismatch
- wrong folder

2. ImportError:
- function name typo

3. Circular import:
- file A imports B and B imports A

## 6) How to avoid import issues

1. Keep helper and main file in same folder for simple practice
2. Use clear function names
3. Run script from project root folder
4. Check spelling carefully

## 7) Practice checklist

After Day 11, you should be able to:
1. Create helper module file
2. Import functions from another file
3. Handle errors in imported functions
4. Organize a small project across multiple files
