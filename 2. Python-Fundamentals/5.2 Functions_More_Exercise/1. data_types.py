def data_type(some_type, some_data):
    if some_type == "int":
        some_data = int(some_data) * 2
        return some_data
    elif some_type == "real":
        some_data = float(some_data) * 1.5
        return f"{some_data:.2f}"
    elif some_type == "string":
        some_data = "$" + some_data + "$"
        return some_data



type_of_data = input()
given_data = input()
print(data_type(type_of_data, given_data))