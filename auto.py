# whatsapp automation
import pywhatkit
from datetime import datetime

# Define the time in 12-hour format
hour = 12
minute = 52
period = "PM"  # or "AM"

# Convert to 24-hour format
if period == "PM" and hour != 12:
    hour += 12
elif period == "AM" and hour == 12:
    hour = 0

# Schedule the message
pywhatkit.sendwhatmsg('+918921401731', 'Hi', hour, minute)
