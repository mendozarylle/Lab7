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

    def format_time(self):
        """Return the Time object as a formatted string."""
        return f'{self.hour:02}:{self.minute:02}:{self.second:02}'

    def time_to_sec(self):
        """Convert the Time object to the total number of seconds since midnight."""
        return self.hour * 3600 + self.minute * 60 + self.second

    def change_time(self, seconds):
        """Modify the current Time object by adding or subtracting seconds."""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second

    def sum_times(self, other_time):
        """Add another Time object to the current Time object and return the result."""
        total_seconds = self.time_to_sec() + other_time.time_to_sec()
        return sec_to_time(total_seconds)

    def valid_time(self):
        """Check if the Time object attributes are valid."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True


def sec_to_time(seconds):
    """Convert a total number of seconds into a Time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
