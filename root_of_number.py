# https://www.pramp.com/challenge/jKoA5GAVy9Sr9jGBjzN4
def error_cond(current_midpoint, last_midpoint):
    midpoint_difference = abs(current_midpoint - last_midpoint)
    if midpoint_difference < .001:
        return True
    else:
        False


def root(x, n):
    lo = 0
    hi = x
    midpoint = (lo + hi) / 2.0
    previous_midpoint = 0
    while not error_cond(midpoint, previous_midpoint):
        # If our midpoint value was too small
        if midpoint ** n < x:
            lo = midpoint
        else:
            # If our midpoint value was too big
            hi = midpoint
        previous_midpoint = midpoint
        midpoint = (lo + hi) / 2.0
    return midpoint





print(root(4, 2))
