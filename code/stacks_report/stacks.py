#!/usr/bin/env python3
import time
import numpy as np
from datetime import datetime
from numpy import random as rd


def Stack_Report(stack, stats_details, file_stack):
    """
    * Takes the stack which raised unusual behavior for a particular system stat.
    * Saves the stack to a file
    * Writes some information with regards to the analysis, like the timestamp and direct comparison with the threshold value.
    """

    # Gather the stack information from the `stack_details` dictionary
    threshold = stats_details["threshold"]
    cycle_time = stats_details["cycle_time"]
    stack_type = stats_details["stack_type"]
    stack_issue = stats_details["stack_issue"]

    avg_stack_value = stack.mean()
    time_stamp = str(datetime.utcnow())[0:22]
    head = f'Analysis report for the {stack_type}\nGenerated at -> {time_stamp}\n'
    body = f'{stack_issue} -> The average value of the stack is {avg_stack_value}%, which is above the threshold value of {threshold}%.\nStack values for the past {cycle_time} seconds ->\n************\n{stack}\n************'
    STACK_MESSAGE = head + body

    with open(file_stack, 'w+') as stack_writer:
        stack_writer.write(STACK_MESSAGE)


if __name__ == '__main__':
    stack = np.arange(0, 100, 1)
    file_stack = 'failed_stack_report.dat'

    stack_issues = {"CPU": "High CPU usage",
                    "MEM": "High MEMORY usage"}

    stack_type = {"CPU": "CPU_USAGE_STACK",
                  "MEM": "MEM_USAGE_STACK"}

    stack_details = lambda threshold, cycle_time, stack_type, stack_issue: {
        "threshold": threshold, "cycle_time": cycle_time, "stack_type": stack_type, "stack_issue": stack_issue}

    cpu_stack_stats = stack_details(
        30, 60, stack_type["CPU"], stack_issues["CPU"])
    mem_stack_stats = stack_details(
        30, 60, stack_type["MEM"], stack_issues["MEM"])

    Stack_Report(stack, cpu_stack_stats, file_stack),
    # Stack_Report(stack, mem_stack_stats, file_stack)
