from random import randint

def roll(dice_number, dice_sides=6, modify=0):
    accepted_types = [3, 4, 6, 8, 10, 12, 100]
    dice_throws = [randint(1, dice_sides) for _ in range(1, dice_number+1)]
    if dice_sides not in accepted_types:
        raise Exception("No such dice!")
    return sum(dice_throws) + modify


print(roll(2, 10, 20))  # rzut 2 kostkami 10-ściennymi, do wyniku dodać 20
print(roll(3, 6, -3))  # rzut 3 kostkami 6-ściennymi, od wyniku odjąć 3
print(roll(0, 6, -3))  # rzut 3 kostkami 6-ściennymi, od wyniku odjąć 3