player_health = 100
player_damage = 10
    

def get_health():
    return player_health


def get_damage():
    return player_damage


def take_damage(damage):
    global player_health
    player_health -= damage