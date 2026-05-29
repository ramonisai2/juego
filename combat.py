import math
ATTACK_RANGE = 3
ATTACK_DAMAGE = 25

def attack_enemy(player, enemies):
    for enemy in enemies:
        dx = player.x - enemy.x
        dz = player.z - enemy.z
        dist = math.sqrt(dx*dx + dz*dz)
        if dist < ATTACK_RANGE:
            enemy.health -= ATTACK_DAMAGE

    enemies[:] = [e for e in enemies if e.health > 0]
