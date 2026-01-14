import pygame, sys, random, json, os

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life Simulator")

font = pygame.font.SysFont("arial", 22)
clock = pygame.time.Clock()

# ===================== PLAYER =====================

class Player:
    def __init__(self):
        self.money = 500
        self.energy = 100
        self.happiness = 50
        self.job = "İşsiz"
        self.city = "Merkez"
        self.house = False
        self.car = False
        self.company = False

player = Player()

# ===================== WORLD DATA =====================

cities = {
    "Merkez": 1.0,
    "Sahil": 1.2,
    "Teknoloji Vadisi": 1.5,
    "Doğa": 0.8
}

npc_names = ["Ahmet", "Ayşe", "Mehmet", "Zeynep"]
npc_friendship = 0

# ===================== SAVE SYSTEM =====================

def save_game():
    data = player.__dict__
    with open("save.json", "w") as f:
        json.dump(data, f)

def load_game():
    if os.path.exists("save.json"):
        with open("save.json") as f:
            player.__dict__.update(json.load(f))

load_game()

# ===================== GAME LOOP =====================

def draw(text, x, y):
    screen.blit(font.render(text, True, (255,255,255)), (x,y))

while True:
    screen.fill((25,30,40))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            save_game()
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_1:
                bonus = cities[player.city]
                earn = int(random.randint(50,100) * bonus)
                player.money += earn
                player.energy -= 10

            if e.key == pygame.K_2:
                player.energy = min(100, player.energy + 20)
                player.happiness += 5

            if e.key == pygame.K_3:
                npc_friendship += 10
                player.happiness += 8

            if e.key == pygame.K_4:
                player.city = random.choice(list(cities.keys()))

            if e.key == pygame.K_5 and not player.house and player.money >= 1000:
                player.money -= 1000
                player.house = True
                player.happiness += 15

            if e.key == pygame.K_6 and not player.car and player.money >= 600:
                player.money -= 600
                player.car = True
                player.happiness += 10

            if e.key == pygame.K_7 and not player.company and player.money >= 1500:
                player.money -= 1500
                player.company = True

            if e.key == pygame.K_s:
                save_game()

    draw("1: Çalış  2: Dinlen  3: NPC  4: Şehir  5: Ev  6: Araba  7: Şirket  S: Kaydet", 20, 560)

    draw(f"Para: {player.money}", 20, 30)
    draw(f"Enerji: {player.energy}", 20, 60)
    draw(f"Mutluluk: {player.happiness}", 20, 90)
    draw(f"Şehir: {player.city}", 20, 120)
    draw(f"Ev: {player.house}  Araba: {player.car}  Şirket: {player.company}", 20, 150)
    draw(f"NPC Dostluk: {npc_friendship}", 20, 180)

    pygame.display.flip()
    clock.tick(60)
