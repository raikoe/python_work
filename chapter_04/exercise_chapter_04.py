# 4-3
for number in range(1,21):
    print(number)

# 4-4
million = list(range(1,1000001))
print(million)
print(f"Min: {min(million)}, Max: {max(million)}, Sum: {sum(million)}")

odd_numbers = list(range(1,21,2))
print(odd_numbers)
three_multiples = list(range(3,31,3))
for number in three_multiples:
    print(number)

cubes = [values**3 for values in range(1,11)]
for cube in cubes:
    print(cube)

# 4-10
