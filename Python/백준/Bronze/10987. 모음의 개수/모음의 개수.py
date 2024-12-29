s = input().strip()

vowels = {'a', 'e', 'i', 'o', 'u'}

count = sum(1 for char in s if char in vowels)

print(count)
