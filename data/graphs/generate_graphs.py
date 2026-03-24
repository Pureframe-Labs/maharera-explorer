import json
import random
import os

os.makedirs("graphs", exist_ok=True)

for project in range(1,301):

    towers=["Tower 1","Tower 2"]

    flats=[]
    floor_prices=[]

    floors=random.sample(range(0,32),random.randint(10,15))

    # floor pricing
    for f in floors:

        t1=random.randint(90,180)*100000
        t2=random.randint(90,180)*100000

        floor_prices.append({
            "floor":f,
            "tower1":t1,
            "tower2":t2
        })

    # flats
    for i in range(random.randint(28,40)):

        tower=random.choice(towers)

        buying_price=random.randint(90,180)*100000
        market_value=int(buying_price*random.uniform(0.7,0.9))

        renting_price=int(buying_price*random.uniform(0.003,0.006))

        flats.append({
            "tower":tower,
            "floor":random.randint(0,31),
            "flat":random.randint(1001,3205),
            "area":random.choice([70,75,80,110,115]),

            "buying_price":buying_price,
            "market_value":market_value,
            "renting_price":renting_price
        })

    tower_dist={
        "Tower 1":sum(1 for f in flats if f["tower"]=="Tower 1"),
        "Tower 2":sum(1 for f in flats if f["tower"]=="Tower 2")
    }

    data={
        "tower_distribution":tower_dist,
        "floor_prices":floor_prices,
        "flats":flats
    }

    with open(f"graphs/project_{project}.json","w") as f:
        json.dump(data,f,indent=2)

print("Graph data generated.")