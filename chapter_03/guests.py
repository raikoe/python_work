guests = ["Alice", "Bob", "Charlie"]
print(f"Hello, {guests[0]}! You are invited to dinner.")
print(f"Hello, {guests[1]}! You are invited to dinner.")
print(f"Hello, {guests[2]}! You are invited to dinner.")

print(f"{guests[1]} can't make it to dinner.")
guests[1] = "David"
print(f"Hello, {guests[0]}! You are invited to dinner.")
print(f"Hello, {guests[1]}! You are invited to dinner.")
print(f"Hello, {guests[2]}! You are invited to dinner.")

print("Good news! We found a bigger dinner table.")
guests.insert(0, "Eve")
guests.insert(2, "Frank")
guests.append("Grace")
print(f"Hello, {guests[0]}! You are invited to dinner.")
print(f"Hello, {guests[1]}! You are invited to dinner.")
print(f"Hello, {guests[2]}! You are invited to dinner.")
print(f"Hello, {guests[3]}! You are invited to dinner.")
print(f"Hello, {guests[4]}! You are invited to dinner.")
print(f"Hello, {guests[5]}! You are invited to dinner.")
print(len(guests))
while len(guests) > 2: 
    no_guest_anymore = guests.pop()
    print(f"Sorry {no_guest_anymore}, I can't invite you to dinner.")


for guest in guests:
    print(f"Hello, {guest}! You are still invited to dinner.")

del guests[0]
del guests[0]  
print(guests)
