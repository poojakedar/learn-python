"""Day 17 mini exercise: Logging configuration practice.

Goal:
1) Configure logging levels
2) Customize log format
3) Write logs to both console and file

Save your final version as solutions/day17_logging_config_solution.py
"""

import logging

print("=== Day 17 Mini Exercise: Logging Config ===")

# TODO 1:
# Change level to DEBUG and observe extra logs.
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def process_order(order_id, amount):
    logging.debug("process_order called with order_id=%s amount=%s", order_id, amount)
    logging.info("Processing order %s", order_id)

    if amount <= 0:
        logging.warning("Order %s has invalid amount: %s", order_id, amount)
        return False

    if amount > 10000:
        logging.error("Order %s exceeds max allowed amount", order_id)
        return False

    logging.info("Order %s processed successfully", order_id)
    return True


# TODO 2:
# Add timestamp to format using %(asctime)s.

# TODO 3:
# Add filename="day17_debug.log" in basicConfig and run again.
# Then open day17_debug.log and inspect output.


process_order("A100", 250)
process_order("A101", -10)
process_order("A102", 15000)

print("\nMini exercise complete. Now apply TODO changes and rerun.")
