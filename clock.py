import time

def countdown_timer(n):
    while n > 0:
        minutes, seconds = divmod(n, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print('Remaining time: ' + timer, end="\r")
        time.sleep(1)
        n -= 1

print("Starting focus timer for 25 minutes...")
countdown_timer(1500)
print("Focus session ended!")
