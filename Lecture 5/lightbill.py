def calculate_consumption(price):
    consumption = 0
    consumption += min(price // 2, 100)
    price -= min(price, 2 * 100)
    consumption += min(price // 3, 9900)
    price -= min(price, 3 * 9900)
    consumption += min(price // 5, 990000)
    price -= min(price, 5 * 990000)
    consumption += price // 7
    return consumption
def calculate_price(consumption):
    price = 0
    price += min(consumption * 2, 2 * 100)
    consumption -= min(consumption, 100)
    price += min(consumption * 3, 3 * 9900)
    consumption -= min(consumption, 9900)
    price += min(consumption * 5, 5 * 990000)
    consumption -= min(consumption, 990000)
    price += consumption * 7
    return price


while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    total_consumption = calculate_consumption(a)
    min_consumption = 0
    max_consumption =total_consumption
    answer = 0
    while min_consumption < max_consumption:
        my_consumption= ( min_consumption + max_consumption) //2
        neighbor_consumption = total_consumption - my_consumption
        diff = abs(calculate_price(neighbor_consumption) - calculate_price(my_consumption))

        if diff > b:
            min_consumption = my_consumption + 1
        elif diff < b:
            max_consumption = my_consumption
        else:
            answer = my_consumption
            break
    print(calculate_price(answer))
