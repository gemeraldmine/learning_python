def number_pattern(n):
    pattern = ""
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    for i in range(n):
        i += 1
        pattern += f"{i} "
    return pattern.strip()


print(number_pattern(-1))
