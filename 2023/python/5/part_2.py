def handler():
    with open('input.txt') as f:
        text = f.read()
    seeds_ranges = []
    map_ranges = []
    text = text.split("\n\n")
    for line in text:
        if line.startswith("seeds"):
            seeds = list(map(int, line.split(":")[1].strip().split(" ")))
            for s in range(0, len(seeds), 2):
                seeds_ranges.append((seeds[s], seeds[s+1]))
        else:
            ranges = line.split(":")[1].strip().split("\n")
            for r in ranges:
                map_ranges.append(list(map(int, r.split(" "))))
    locations = []
    for seed_range in seeds_ranges:
        for seed in range(seed_range[0], seed_range[0] + seed_range[1] + 1):
            for map_rules in map_ranges:
                destination_start, source_start, range_length = map_rules
                if source_start <= seed <= source_start + range_length:
                    seed = destination_start + (seed - source_start)


            locations.append(seed)
    return min(locations)



if __name__ == '__main__':
    print(handler())