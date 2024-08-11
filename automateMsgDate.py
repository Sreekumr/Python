from apscheduler.schedulers.blocking import BlockingScheduler
import pywhatkit
from datetime import datetime  # Import datetime module

def send_whatsapp_message():
    pywhatkit.sendwhatmsg('+918921401731', 'Hi', 13, 3)  # Send at 2:30 PM

# Create a scheduler
scheduler = BlockingScheduler()

# Schedule the task
scheduler.add_job(send_whatsapp_message, 'date', run_date=datetime(2024, 8, 11, 13, 3))

# Start the scheduler
scheduler.start()
