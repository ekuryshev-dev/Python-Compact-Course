dictionaries = [
    {"make": "Google", "model": 216, "color": "Black"},
    {"make": "Mi Max", "model": "2", "color": "Gold"},
    {"make": "Samsung", "model": 7, "color": "Blue"},
]

# Sort the dictionaries by color
sorted_dictionaries = sorted(dictionaries, key=lambda dictionary: dictionary["color"])

print(sorted_dictionaries)