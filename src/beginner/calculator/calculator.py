#TODO: Implement the calculator functionality

global_value = 1

def add(value):
    global global_value
    global_value += value
    return global_value

print(add(5))
