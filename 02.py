# To solve this problem, we can first sort the array in descending order. Then, we can divide the sorted array into 'M' groups of size 'M'. For each group, we can find the 'M' largest elements and move them to the beginning of the group. This ensures that the largest 'M' elements are present in the first 'M' indices of each group.

# Next, we need to reorder the elements within each group to meet the condition that the largest 'M' elements are present in the first 'M' indices, the second-largest 'M' elements are present in the indices '[M.. 2*M-1]' and so on. To do this, we can simply sort each group in descending order.

# Finally, we need to count the number of elements that were moved during the process. This is equal to the sum of the differences between the original indices and the new indices of the 'M' largest elements in each group.

# Here is the Python code to implement this approach:

def min_elements_to_reorder(A, M):
    n = len(A)
    # Sort the array in descending order
    A_sorted = sorted(A, reverse=True)
    # Divide the sorted array into M groups of size M
    groups = [A_sorted[i:i+M] for i in range(0, n, M)]
    # Move the M largest elements to the beginning of each group
    for group in groups:
        for i in range(M):
            max_idx = i
            for j in range(i+1, M):
                if group[j] > group[max_idx]:
                    max_idx = j
            if max_idx != i:
                group[i], group[max_idx] = group[max_idx], group[i]
    # Sort each group in descending order
    for group in groups:
        group.sort(reverse=True)
    # Count the number of elements that were moved
    moves = 0
    for group in groups:
        for i in range(M):
            orig_idx = A.index(group[i])
            new_idx = groups.index(group)*M + i
            if orig_idx != new_idx:
                moves += 1
    return moves

# Example usage
A = [10, 8, 7, 5, 4, 3, 2, 1]
M = 2
min_moves = min_elements_to_reorder(A, M)
print(min_moves) # Output: 4