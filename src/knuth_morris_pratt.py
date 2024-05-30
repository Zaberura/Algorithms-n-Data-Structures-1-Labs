def build_prefix_table(input_text):
    prefix_table = [0] * len(input_text)
    i = 1
    j = 0
    while i < len(input_text):
        if input_text[i] == input_text[j]:
            j += 1
            prefix_table[i] = j
            i += 1
        elif j != 0:
            j = prefix_table[j-1]
        else:
            i += 1

    return prefix_table


def kmp_search(haystack, needle):

    prefix_table = build_prefix_table(needle)
    matches = []

    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = prefix_table[j - 1]
        if haystack[i] == needle[j]:
            j += 1
        if j == len(needle):
            matches.append(i - j + 1)
            j = prefix_table[j - 1]

    return matches

# Example usage:
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matches = kmp_search(text, pattern)
print("Pattern found at indices:", matches)



