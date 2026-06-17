numbers = [5, 2.7, -3, 10.5, 0, 8, -1.2, 4.9]

def find_min_max_sum(lst):
    if not lst:
        print("listi aris carieli!")
        return 0
    
    min_num = min(lst)
    max_num = max(lst)
    
    print(f"Minimum number: {min_num}")
    print(f"Maximum number: {max_num}")
    
    return min_num + max_num


result = find_min_max_sum(numbers)
print(f"Sum of min and max: {result}")