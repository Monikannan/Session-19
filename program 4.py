def find_pillow_holder(n, time):
    forward = True
    current_holder = 1
    for _ in range(time):
        if forward:
            current_holder += 1
            if current_holder == n:
                forward = False
        else:
            current_holder -= 1
            if current_holder == 1:
                forward = True
    return current_holder
n = 4  
time = 5
result = find_pillow_holder(n, time)
print("The person holding the pillow after {} seconds is at index {}".format(time, result))
