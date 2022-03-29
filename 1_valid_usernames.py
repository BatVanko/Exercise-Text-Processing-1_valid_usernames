usernames_line = input().split(", ")
valid_names = []
for word in usernames_line:
    isvalid = True
    if 3 <= len(word) <= 16 and word.isalnum() or "-" in word or "_" in word:
        valid_names.append(word)

print('\n'.join(valid_names))



