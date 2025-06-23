def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) < 2:
        return full_name
    first = parts[0]
    last = parts[-1]
    return f"{last}, {first}"

# Example:
print(format_name("Areeba Atiq"))

