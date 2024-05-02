def compute_minimum_volume(events):
    print("Events:", events)
    fuel_consumption = None
    for event in events:
        if 'Fuel consumption' in event[1]:
            fuel_consumption = int(event[1].split()[2])
            break
    if fuel_consumption is None:
        return 0  # No fuel consumption event found
    tank_volume = 0
    distance = 0

    for i in range(1, len(events)):
        event = events[i]
        print("Current event:", event)
        next_distance = event[0]
        distance_travelled = next_distance - distance
        tank_volume += distance_travelled * fuel_consumption
        if event[1] == 'Leak':
            tank_volume += distance_travelled  # compensate for leaks
        elif event[1] == 'Gas station':
            tank_volume = max(0, tank_volume)  # refill the tank
        elif event[1] == 'Mechanic':
            tank_volume = max(0, tank_volume)  # fix all leaks
        if 'Fuel consumption' in event[1]:
            fuel_consumption = int(event[1].split()[2])  # update fuel consumption
        distance = next_distance

    return round(tank_volume, 3)





def main():
    test_cases = []
    while True:
        line = input().split()
        print("Input line:", line)
        if len(line) == 4 and line[0] == '0' and line[1] == 'Fuel' and line[2] == 'consumption' and line[3] == '0':
            break
        events = [(int(line[0]), line[1] + ' ' + line[2])]
        while True:
            line = input().split()
            if len(line) == 4 and line[0] == '0' and line[1] == 'Fuel' and line[2] == 'consumption' and line[3] == '0':
                break
            if len(line) < 2:
                break
            if line[1] == 'Goal':
                events.append((int(line[0]), line[1]))
                break
            if len(line) == 3:
                events.append((int(line[0]), line[1] + ' ' + line[2]))
            else:
                events.append((int(line[0]), line[1]))
        test_cases.append(events)

    for events in test_cases:
        print(compute_minimum_volume(events))

if __name__ == "__main__":
    main()



