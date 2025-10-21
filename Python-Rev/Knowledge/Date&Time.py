import time
import datetime

# -----------------------------------------
# Time Module Basics
# -----------------------------------------
# The time module deals with "epoch time" (number of seconds since Jan 1, 1970 UTC).

print(time.time())
# ✅ Returns the number of seconds elapsed since the Unix Epoch (1 Jan 1970).
# Example Output: 1739792567.7890115


# -----------------------------------------
# Local Time (Structured Time)
# -----------------------------------------
print(time.localtime())
# ✅ Converts epoch seconds into a 'struct_time' object
#    struct_time has fields like tm_year, tm_mon, tm_mday, tm_hour, etc.

lt = time.localtime()   # Get current local time

# Accessing specific time components
print(lt.tm_mday)   # ✅ Day of the month (1–31)
print(lt.tm_hour)   # ✅ Current hour (0–23)


# -----------------------------------------
# Custom Time Conversion
# -----------------------------------------
# You can convert any epoch value into a structured localtime.
# Here, we use half of the current epoch seconds for demonstration.
lt = time.localtime(time.time() / 2)

print(lt.tm_year)   # ✅ Year corresponding to that earlier epoch time

print(time.ctime())


# The datetime.time class represents only the time portion (hour, minute, second)
# — it does NOT include a date or timezone.

tim1 = datetime.time(10, 10, 10)   # 10:10:10 AM
tim2 = datetime.time(11, 11, 11)   # 11:11:11 AM

# -----------------------------------------
# Invalid operation: subtraction
# -----------------------------------------
# ❌ You cannot directly subtract two 'time' objects because
# 'time' represents only a specific time of day, not a full point in time.
# Python doesn't know what date to associate with them.
# Example:
# print(tim2 - tim1)   # ➜ TypeError

# Uncommenting the line below would raise:
# TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'

# -----------------------------------------
# Valid operation: comparison
# -----------------------------------------
print(tim2 > tim1)
# ✅ Comparison is allowed — Python compares hour, minute, and second lexicographically.
# So here, 11:11:11 > 10:10:10 → Output: True
