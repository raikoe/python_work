name = "Raiko"
print(f"Hello {name}, would you like to learn some Python today?")

print(name.lower())
print(name.upper())
print(name.title())

author = "Albert Einstein"
quote = '“A person who never made a mistake never tried anything new.”'
message = f"{author} once said, {quote}"
print(message)

name = " albert "
print(f"\t{name.lstrip()}")
print(f"\n{name.rstrip()}")
print(name.strip())

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
