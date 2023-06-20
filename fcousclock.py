import time

def countdown(timer):
    """
    A function that starts a countdown from a given time in seconds
    """
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Time left: {timeformat} minutes", end='\r')
        time.sleep(1)
        timer -= 1

print("Focus Timer")
# Set the countdown timer for 25 minutes
countdown(25*60)
# Time's up!
print("Time's up! Take a break.")
