import time

def reminder(interval, message):
    while True:
        time.sleep(interval)
        print(message)

interval = int(input("Enter time interval (in seconds): "))
message = input("Enter reminder message: ")

print(f"Starting a reminder every {interval} seconds.")
reminder(interval, message)
