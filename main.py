
def count_quantities(input: list[int]) -> list[(int, int)]:
    """Counts the number of adjacent occurrences of each element in a list.

    Parameters
    ----------
    input : list[int]
        A list of integers where adjacent occurrences of elements are counted.

    Returns
    -------
    list[(int, int)]
        A list of tuples where each tuple is (count, element).
    """

    quantities = []
    adjacent_occurrences = 1 # start with 1 because we only add to the count when we find a match

    i = 0
    while i < len(input):
        if i + 1 >= len(input): # if we are at the last element
            quantities.append((adjacent_occurrences, input[i]))
            break

        if input[i] == input[i + 1]: # if the next element is the same
            adjacent_occurrences += 1
        else: # if not, end the current count
            quantities.append((adjacent_occurrences, input[i]))
            adjacent_occurrences = 1 # reset the count for the next element
        i += 1
    
    return quantities

def flatten_quantities(quantities: list[(int, int)]) -> list[int]:
    """Flattens a list of tuples into a list of integers.

    Parameters
    ----------
    quantities : list[(int, int)]
        A list of tuples where each tuple is (count, element).

    Returns
    -------
    list[int]
        A flattened list of integers.
    """
    
    return [item for sublist in quantities for item in sublist]

start = 1
print(numbers := [start])
n = 20 # number of iterations

for _ in range(n):
    quantities = count_quantities(numbers)
    print(numbers := flatten_quantities(quantities))