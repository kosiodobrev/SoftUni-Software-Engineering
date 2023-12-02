path = input().split("\\")
needed_item = path[-1]
name, extension = needed_item.split(".")
print(f"File name: {name}")
print(f"File extension: {extension}")