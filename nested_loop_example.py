# Start at 1 o'clock
hours = 1
while hours <= 12:
    # Each hour starts at 0 minutes
    minutes = 0
    while minutes < 60:
        print(f'{hours}:{minutes}')
        # After printing the current hour:minutes,
        # increment the minutes counter
        minutes = minutes + 1
    # After we reach 59 minutes. go to the next hour
    hours = hours + 1