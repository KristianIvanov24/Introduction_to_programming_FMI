def is_geometric_progression(*args):
    if len(args) < 2:
        return True
    ratio = args[1] / args[0]
    for i in range(1, len(args)):
        if not isinstance(args[i], (int, float)):
            print("All arguments must be numbers")
            return
        if args[i] / args[i-1] != ratio:
            return False
    return True

print(is_geometric_progression(1, 2, 4, 8, 16))  # True
print(is_geometric_progression(1, 2, 4, "8", 16))  # All arguments must be numbers
print(is_geometric_progression(1, 2, 3, 4, 5))  # False
