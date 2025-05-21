enemies = 1


def increase_enemies():
    global enemies
    enemies += 1


increase_enemies()

print(f"enemies: {enemies}")
