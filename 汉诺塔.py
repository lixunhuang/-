def mov(m):
    if m == 1:
        return 1
    use = mov(m - 1)
    return use + mov(1) + mov(m - 1)


print(mov(10))
