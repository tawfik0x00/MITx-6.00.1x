s = input("s: ")

longest = current = s[0]

for i in range(1, len(s)):
    # check alphapetical order
    if s[i] >= s[i - 1]:
        current += s[i]
    else:
        # if not, check if the current substring is the longest
        if len(current) > len(longest):
            longest = current
        
        # reset the current substring
        current = s[i]

# last check
if len(current) > len(longest):
    longest = current

print(longest)