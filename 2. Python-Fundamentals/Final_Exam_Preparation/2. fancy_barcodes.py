import re
pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
n = int(input())
for current_code in range(n):
    code = input()
    match = re.findall(pattern, code)
    if match:
        if not bool(re.search(r"\d+", code)):
            group = "00"
        else:
            group = ""
            for char in code:
                if char.isnumeric():
                    group += char
        print(f"Product group: {group}")
    else:
        print("Invalid barcode")