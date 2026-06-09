# Day 10 Concepts: Beginner Capstone

Day 10 combines everything you learned into one complete app.

## 1) Capstone meaning

A capstone is a final practice project that uses many concepts together.

For this course, the app combines:
1. class and objects
2. functions/methods
3. loops and conditions
4. list/dictionary data
5. file save/load
6. error handling

## 2) Recommended app flow

1. Start app
2. Load old data from file
3. Show menu repeatedly
4. Perform selected action
5. Save data before exit

## 3) Why use a class here

A class groups related data and methods.

Example:
- data: tasks
- methods: add, show, complete, save, load

This keeps code cleaner than many global variables.

## 4) Menu design pattern

Use while True for continuous menu.
Use if/elif for options.
Use break to exit.

## 5) Data format

For tasks, a good shape is:
{"title": "Learn Python", "done": False}

Many such items go in a list.

## 6) File persistence

Saving means writing app data to disk.
Loading means reading it back when app restarts.

JSON is beginner-friendly because it matches Python dict/list structure.

## 7) Input validation

Always validate:
1. empty task titles
2. invalid menu choices
3. non-number task index

This prevents crashes and improves user experience.

## 8) Common beginner mistakes

1. Not subtracting 1 for list index when user enters task number
2. Forgetting to load data at startup
3. Forgetting to save before exit
4. Mixing app logic and print logic in one giant block

## 9) Capstone checklist

By end of Day 10, your app should:
1. add tasks
2. show tasks
3. complete tasks
4. save to file
5. load from file
6. handle invalid input safely
