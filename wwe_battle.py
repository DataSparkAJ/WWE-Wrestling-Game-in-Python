# Step 1: wrestlers
the_rock = { 
    "name": "The Rock",
    "hp": 120,
    "moves": {"Rock Bottom": 30,
              "People's Elbow": 25,
              "Punch": 10
              }
}
john_cena = { 
    "name": "John Cena",
    "hp": 130,
    "moves": {"Attitude Adjustment": 30,
              "STF": 20,
              "Punch": 10
              }
}
wrestlers = [the_rock, john_cena]

# Step 2: Let the player choose
print("Choose your wrestler")
for i, wrestler in enumerate(wrestlers, 1):
    print(f"{i} . {wrestler['name']}")

choice = int(input("Enter the number: "))
player = wrestlers[choice-1]

# Step 3: computer pick someone different from the player

import random

opponent = random.choice([w for w in wrestlers if w != player])
print(f"Match: {player['name']} vs {opponent['name']}!")



# while player_hp > 0 and opponent_hp > 0:
player_hp = player["hp"]
opponent_hp = opponent["hp"]
while player_hp > 0 and opponent_hp > 0:
    print(f"{player['name']} HP: {player_hp} | {opponent['name']} HP: {opponent_hp}")
   
    print("Choose your move: ")
    moves = list(player["moves"].items())
    for i, (move, dmg) in enumerate(moves, 1):
        print(f"{i}. {move} ({dmg} dmg)")
# player move
    choice = int(input("Enter move number: "))
    move_name, damage = moves[choice - 1]
    print(f"{player['name']} hits {opponent['name']} with {move_name} for {damage} damage!")
    opponent_hp -= damage

    if opponent_hp <= 0:
        print(f"\n💥 {opponent['name']} is down! 1...2...3! {player['name']} wins the match! 💥")
        break

# opponent move
    opp_move = random.choice(list(opponent["moves"].items()))
    print(f"{opponent['name']} counters with {opp_move[0]} for {opp_move[1]} damage!")
    player_hp -= opp_move[1]


    if player_hp <= 0:
        print(f"\n💥 {player['name']} is knocked out! 1...2...3! {opponent['name']} wins the match! 💥")
