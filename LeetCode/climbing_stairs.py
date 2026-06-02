stairs1 = 2
stairs2 = 3
stairs3 = 15
stairs4 = 45


def climb_stairs(n):
    """
    prev = 1
    curr = 1

    for i in range(n):
        prev, curr = curr, prev + curr

    return prev
    """


print(climb_stairs(stairs1))
print(climb_stairs(stairs2))
print(climb_stairs(stairs3))
print(climb_stairs(stairs4))
