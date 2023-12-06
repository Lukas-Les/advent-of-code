class Seed:
    def __init__(self, seed_id):
        self.seed_id = seed_id
        self.soil = None
        self.fertilizer = None
        self.water = None
        self.light = None
        self.temperature = None
        self.humidity = None
        self.location = None

    def __repr__(self):
        return f"Seed({self.seed_id}), location: {self.location}"


class BaeMapper:
    def __init__(self, raw_lines):
        self.rules = self._prepare_mapper(raw_lines)

    @staticmethod
    def _prepare_mapper(raw_lines):
        rules = []
        for line in raw_lines:
            destination, source, _range = line.split(" ")
            rules.append((int(destination), int(source), int(_range)))
        return rules

    def map(self, value):
        for rule in self.rules:
            destination, source, _range = rule
            if source <= value <= source + _range:
                return destination + (value - source)

        return value


def load_input():
    with open('input.txt') as f:
        text = f.readlines()

    seeds = []
    seed_to_soil = None
    soil_to_fertilizer = None
    fertilizer_to_water = None
    water_to_light = None
    light_to_temperature = None
    temperature_to_humidity = None
    humidity_to_location = None

    for i in range(len(text)):
        if text[i].startswith('seeds:'):
            _seeds = text[i].split(':')[1].strip().split(" ")
            for seed in _seeds:
                seeds.append(Seed(int(seed)))
            continue
        print("Seeds loaded")

        if text[i].startswith('seed-to-soil'):
            stf_lines = []
            for j in range(i+1, len(text)):
                if text[j] != '\n':
                    stf_lines.append(text[j].strip())
                else:
                    seed_to_soil = BaeMapper(stf_lines)
                    break
        elif text[i].startswith('soil-to-fertilizer'):
            stf_lines = []
            for j in range(i+1, len(text)):
                if text[j] != '\n':
                    stf_lines.append(text[j].strip())
                else:
                    soil_to_fertilizer = BaeMapper(stf_lines)
                    break
        elif text[i].startswith('fertilizer-to-water'):
            stf_lines = []
            for j in range(i+1, len(text)):
                if text[j] != '\n':
                    stf_lines.append(text[j].strip())
                else:
                    fertilizer_to_water = BaeMapper(stf_lines)
                    break
        elif text[i].startswith('water-to-light'):
            stf_lines = []
            for j in range(i+1, len(text)):
                if text[j] != '\n':
                    stf_lines.append(text[j].strip())
                else:
                    water_to_light = BaeMapper(stf_lines)
                    break
        elif text[i].startswith('light-to-temperature'):
            stf_lines = []
            for j in range(i+1, len(text)):
                if text[j] != '\n':
                    stf_lines.append(text[j].strip())
                else:
                    light_to_temperature = BaeMapper(stf_lines)
                    break
        elif text[i].startswith('temperature-to-humidity'):
            stf_lines = []
            for j in range(i+1, len(text)):
                if text[j] != '\n':
                    stf_lines.append(text[j].strip())
                else:
                    temperature_to_humidity = BaeMapper(stf_lines)
                    break
        elif text[i].startswith('humidity-to-location'):
            stf_lines = []
            for j in range(i+1, len(text)):
                if text[j] != '\n':
                    stf_lines.append(text[j].strip())
                else:
                    humidity_to_location = BaeMapper(stf_lines)
                    break
    print("Mappers loaded")

    return seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location


def handler():
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location  = load_input()
    total_seeds = len(seeds)
    completed = 0
    for seed in seeds:
        print(f"Processing seed {seed.seed_id}")
        seed.soil = seed_to_soil.map(seed.seed_id)
        print(f"Seed {seed.seed_id} soil: {seed.soil}")
        seed.fertilizer = soil_to_fertilizer.map(seed.soil)
        print(f"Seed {seed.seed_id} fertilizer: {seed.fertilizer}")
        seed.water = fertilizer_to_water.map(seed.fertilizer)
        print(f"Seed {seed.seed_id} water: {seed.water}")
        seed.light = water_to_light.map(seed.water)
        print(f"Seed {seed.seed_id} light: {seed.light}")
        seed.temperature = light_to_temperature.map(seed.light)
        print(f"Seed {seed.seed_id} temperature: {seed.temperature}")
        seed.humidity = temperature_to_humidity.map(seed.temperature)
        print(f"Seed {seed.seed_id} humidity: {seed.humidity}")
        seed.location = humidity_to_location.map(seed.humidity)
        print(f"Seed {seed.seed_id} location: {seed.location}")

        completed += 1
        print(f"Completed {completed} of {total_seeds}")

    return min(seeds, key=lambda x: x.location)


if __name__ == '__main__':
    print(handler())
