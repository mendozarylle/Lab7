#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object with input validation."""
        if not isinstance(hour, int) or not isinstance(minute, int) or not isinstance(second, int):
            raise ValueError("Hour, minute, and second must be integers.")
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(time):
    """Return time object as a formatted string."""
    return f'{time.hour:02}:{time.minute:02}:{time.second:02}'

def time_to_sec(time):
    """Convert a Time object to a single integer representing the number of seconds from midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two Time objects and return the sum as a new Time object."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Modify the given Time object by adding or subtracting the given number of seconds."""
    total_seconds = time_to_sec(time) + seconds
    new_time = sec_to_time(total_seconds)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second
    return None

def valid_time(time):
    """Check if the time object attributes are valid."""
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.hour >= 24 or time.minute >= 60 or time.second >= 60:
        return False
    return True
