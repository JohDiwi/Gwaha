try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    # Handle the ZeroDivisionError exception
    print("An error occurred:", e)
