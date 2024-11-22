#!/usr/bin/env python3
# Student ID: [seneca_id]

from lab7c import *

# Create Time objects
t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

# Create a Time object representing the time delta
td = Time(0, 50, 0)

# Test sum_times
tsum1 = sum_times(t1, td)  # Add 50 minutes to 08:00:00
tsum2 = sum_times(t2, td)  # Add 50 minutes to 08:55:00

# Test change_time
change_time(t3, 1800)  # Add 1800 seconds (30 minutes) to 09:50:00

# Alias for format_time function
ft = format_time

# Print formatted results
print(ft(t1), '+', ft(td), '-->', ft(tsum1))  # Expected: 08:00:00 + 00:50:00 --> 08:50:00
print(ft(t2), '+', ft(td), '-->', ft(tsum2))  # Expected: 08:55:00 + 00:50:00 --> 09:45:00
print('09:50:00 + 1800 sec -->', ft(t3))     # Expected: 09:50:00 + 1800 sec --> 10:20:00
