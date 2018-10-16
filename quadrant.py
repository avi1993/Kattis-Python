

def check_if_positive(number):
    if number > 0:
        return True
    else:
        return False


def check_quadrant(quad):
    if quad == [True, True]:
        return 1
    elif quad == [False, True]:
        return 2
    elif quad == [False, False]:
        return 3
    else:
        return 4


x = int(input())
y = int(input())
quadrant = [check_if_positive(x), check_if_positive(y)]
print(check_quadrant(quadrant))


