import json

SAVE_FILE = 'savegame.json'

def save_game(player):
    data = {
        'x': player.x,
        'y': player.y,
        'z': player.z,
        'health': player.health,
        'inventory': player.inventory
    }
    with open(SAVE_FILE, 'w') as f:
        json.dump(data, f)


def load_game(player):
    try:
        with open(SAVE_FILE, 'r') as f:
            data = json.load(f)
        player.x = data['x']
        player.y = data['y']
        player.z = data['z']
        player.health = data['health']
        player.inventory = data['inventory']
    except FileNotFoundError:
        print('No save found')
