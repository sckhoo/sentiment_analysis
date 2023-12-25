# Python3 code to demonstrate
# Getting date and time values
# in ISO 8601 format
 
# importing datetime module
import datetime
 
# Getting today's date and time
DateTime_in_ISOFormat = datetime.datetime.now()
 
# Printing Today's date and time in ISO format of
# auto value for the format specifier
print(DateTime_in_ISOFormat.isoformat("#", "auto"))
 
# Printing Today's date and time format specifier
# as hours
print(DateTime_in_ISOFormat.isoformat("#", "hours"))
 
# Printing Today's date and time format specifier 
# as minutes
print(DateTime_in_ISOFormat.isoformat("#", "minutes"))
 
# Printing Today's date and time format specifier 
# as seconds
print(DateTime_in_ISOFormat.isoformat("#", "seconds"))
 
# Printing Today's date and time format specifier
# as milliseconds
print(DateTime_in_ISOFormat.isoformat("#", "milliseconds"))
 
# Printing Today's date and time format specifier
# as microseconds
print(DateTime_in_ISOFormat.isoformat("#", "microseconds"))