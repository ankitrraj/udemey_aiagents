# from collections import defaultdict 

# char_count = defaultdict(int)

# text = "hey there when its go"

# for char in text:
#     char_count[char] +=1

#     print(char_count)

# from collections import defaultdict

# counts = defaultdict(int)

# for c in "banana":
#     counts[c] += 1

# print(counts)

from collections import defaultdict

groups = defaultdict(list)

pairs = [("a",1), ("b",2), ("a",3)]

for k, v in pairs:
    groups[k].append(v)

print(groups)

