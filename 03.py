# Here is a Python code to solve the problem:

def get_char_at_index(s, k):
    n = len(s)
    # Find the length of the new string
    new_len = n
    while new_len <= k:
        new_len *= 2
    # Traverse the new string backwards to find the character at index k
    i = new_len // 2
    while i > 0:
        if k >= i:
            k -= i
        else:
            i //= 2
        if i == 1:
            return s[k % n]

# Example usage
s = "abc"
n = len(s)
k = 7
char_at_k = get_char_at_index(s * (k // n + 1), k)
print(char_at_k) # Output: c