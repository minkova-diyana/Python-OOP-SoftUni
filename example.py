def calculate_ram_cost(ram_size):
    # Check if ram_size is a positive integer
    if not isinstance(ram_size, int) or ram_size <= 0:
        raise ValueError("RAM size should be a positive integer.")

    # Calculate the cost based on the exponent in the sequence of powers of 2
    cost = ram_size // 2 * 100


    return cost

# Examples
ram_size_2GB = 2
ram_size_4GB = 4

cost_2GB = calculate_ram_cost(ram_size_2GB)
cost_4GB = calculate_ram_cost(ram_size_4GB)

print(f"{ram_size_2GB}GB RAM will cost ${cost_2GB}")
print(f"{ram_size_4GB}GB RAM will cost ${cost_4GB}")
