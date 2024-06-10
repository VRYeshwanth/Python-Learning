import time
def countdown(t):
    while t >= 0:
        hours = t // 3600
        mins = (t % 3600) // 60
        secs = (t % 3600) % 60
        timer = "{:02d}:{:02d}:{:02d}".format(hours, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("TIME UP !!!!!")

while True:
    t_str = input("Enter the countdown (in seconds): ")
    if t_str.isdigit():
        break
    else:
        print("Please enter a valid positive integer.")

countdown(int(t_str))
