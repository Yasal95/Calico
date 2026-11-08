def solve(B, L, E):
    first = (E + B) % 50
    if first > L:
        return 0
    return 1 + (L - first) // 50
