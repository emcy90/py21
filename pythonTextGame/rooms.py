room1 = {
    "description": "bedroom",
    "items": ["alarm"],
    "exits": ["north", "west"]
}

room2 = {
    "description": "bathroom",
    "items": ["bathrobe"],
    "exits": ["north", "east",  "south"]
}

room3 = {
    "description": "kitchen",
    "items": ["food"],
    "exits": ["west", "south"]
}

room4 = {
    "description": "living room",
    "items": ["laptop"],
    "exits": ["east", "south"]
}


the_map = [
    [room1, room2],
    [room3, room4]
]
