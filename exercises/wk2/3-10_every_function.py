
def create_flowers():
    flowers = ['rose', 'pansy', 'tulip']
    flowers.append('carnation')
    return flowers

def print_flowers(flowers):
    for i in range(len(flowers)):
        print(f"{flowers[i].strip().title()}")

def arrange_flowers(flowers):
    print(f"{flowers}")
    print(f"{sorted(flowers, reverse=True)}")
    print(f"{sorted(flowers)}")
    print(f"{flowers}")
    flowers.sort()
    print(f"{flowers}")
    flowers.sort(reverse=True)
    print(f"{flowers}")
    return flowers

def add_flower(flower, flowers):
    flowers.insert(0, flower)
    print(f"added {flower} to {flowers}")
    return flowers

def give_flower(flowers):
    try:
        gift_flower = flowers.pop()
        print(f"Please have a {gift_flower}, the {get_flower_description(gift_flower)}.")
        return flowers
    except:
        IndexError

def give_all(flowers):
    while len(flowers) > 0:
        popped_flower = flowers.pop()
        print(f"Have a {popped_flower} the {get_flower_description(popped_flower)}.")
    if flowers == []:
        return flowers
    else:
        raise IndexError
    # check flowers == []

def get_flower_description(flower):
    while True:
        description_mapping = {
            "rose": "flower of love, romance and passion",
            "tulip": "tame flower of ordinary kindness and strength",
            "carnation": "prom invite flower; cheap and long living off the stem",
            "pansy": "classic flower with beautiful colors and petals with deep black hue in center",
        }
        return description_mapping.get(flower, "Invalid flower.")

def main():
    flowers = create_flowers()
    print_flowers(flowers)
    add_flower('tulip', flowers)
    arrange_flowers(flowers)
    give_flower(flowers)
    give_all(flowers)

if __name__ == "__main__":
    main()
