# Day 20 Concepts: Capstone App

Day 20 combines many ideas from earlier lessons into one small practical app.

## 1) What this capstone combines

1. class to manage app data
2. JSON file to save and load state
3. logging for app activity
4. argparse for command-line commands
5. methods to keep behavior organized

## 2) Why a capstone matters

A capstone helps you stop learning topics in isolation.
You start seeing how real programs are built from small pieces.

## 3) App structure idea

A simple structure is:
1. constants for file paths
2. class for app logic
3. methods like load, save, add, list
4. parser builder for CLI commands
5. main() entry point

## 4) JSON persistence

The app should load saved data at startup and save after changes.
That is how simple apps keep state between runs.

## 5) Logging in apps

Logging is useful for events like:
1. file loaded
2. item added
3. invalid input
4. file saved

## 6) CLI subcommands

Subcommands make tools easier to use.
Examples:
1. add
2. list
3. done

This is more readable than one very long command with many flags.

## 7) Common beginner mistakes

1. forgetting to save after changing data
2. not loading file before using data
3. mixing print output and logging without purpose
4. forgetting list indexes start at 0 inside code

## 8) Practice checklist

After Day 20, you should be able to:
1. design a small app class
2. save and load JSON state
3. add CLI commands with argparse
4. use logging for useful events
5. build a basic real-world Python utility
