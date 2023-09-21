budget = float(input())
number_of_gpus = int(input())
number_of_processors = int(input())
number_of_ram = int(input())

gpu_price = number_of_gpus * 250
processors_price = gpu_price * 0.35
ram_price = gpu_price * 0.10

total_sum = gpu_price \
            + number_of_processors * processors_price \
            + number_of_ram * ram_price

if number_of_gpus > number_of_processors:
    total_sum *= 0.85

difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
