# Day 17 Concepts: Debugging Basics

Debugging is the process of finding and fixing bugs in code.

## 1) What is a bug

A bug is any wrong behavior in a program.

Examples:
1. crash due to zero division
2. wrong formula result
3. wrong loop condition

## 2) Read traceback carefully

When Python crashes, it shows a traceback.
Traceback tells:
1. file name
2. line number
3. error type
4. error message

Always start debugging from the last line of traceback.

## 3) Debugging tools

1. print statements
2. logging module
3. VS Code breakpoints and step controls

Use logging when you need structured, readable debug output.

## 4) Logging configuration basics

`logging.basicConfig()` sets global logging behavior.

Common setup:
`logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")`

Important options:
1. level: minimum severity to show
2. format: how each log line looks
3. filename: write logs to a file instead of console

Common levels (low to high):
1. DEBUG: detailed internal values
2. INFO: normal app flow
3. WARNING: unexpected but recoverable
4. ERROR: operation failed
5. CRITICAL: severe failure

Useful format fields:
1. %(asctime)s timestamp
2. %(levelname)s level name
3. %(message)s log text
4. %(name)s logger name

Example with timestamp:
`logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s: %(message)s")`

Tip:
Use `INFO` while learning, `DEBUG` when actively troubleshooting bugs.

## 5) Breakpoints in VS Code

Workflow:
1. Click left of line number to add breakpoint
2. Press F5 to start debugging
3. Use F10 (Step Over)
4. Inspect variable values in Debug panel

## 6) Common bug patterns

1. wrong operator (+ instead of /)
2. off-by-one index issues
3. missing condition checks
4. assuming input is always valid

## 7) Defensive coding

Defensive coding means writing code that handles bad input safely.

Examples:
1. check list is not empty before average
2. check denominator is not zero
3. return default or clear error message

## 8) Practice checklist

After Day 17, you should be able to:
1. read traceback and find error line
2. add logs to inspect values
3. use breakpoints and step through code
4. fix logic and runtime bugs
5. make functions safer against invalid input
