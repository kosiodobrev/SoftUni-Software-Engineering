countries = input().split(", ")
capitals = input().split(", ")
final_information = dict(zip(countries, capitals))
for key, value in final_information.items():
    print(f"{key} -> {value}")