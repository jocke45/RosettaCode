doors = [1] * 100
round = 2

def toggle(val):
    return 1 if val == 0 else 0

while round <= 100:
    print(doors)
    print(round)
    for ind, door in enumerate(doors,0):
        if (ind+1) % round == 0:
            doors[ind] = toggle(doors[ind])
    round += 1
print(doors)
