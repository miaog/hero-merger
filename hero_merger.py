from data import *
import random
import time
import uuid

def add_heroes(new_heroes):
    for hero, data in new_heroes.iteritems():
        if hero in heroes_list:
            print hero + " is not a new hero."
        else:
            heroes_list += [hero]
            heroes_data[data] += {
                "name": hero,
                "gender": data["gender"],
                "abilities": data["abilities"],
                "meta": {
                       "id": uuid.uuid1().hex,
                       "timestamp": int(time.time())     
                    }
                }

def generate_hero(gender="neutral"):
    qualified = []
    if gender != "neutral":
        for hero in heroes_data["data"]:
            if hero["gender"] == gender.lower():
                qualified += [hero]
    else:
        qualified = heroes_data["data"]
    random_two = random.sample(qualified, 2)
    new_name = random_two[0]["name"].split(" ")[0]+ " " +random_two[1]["name"].split(" ")[1]
    new_abilities = list(set(random_two[0]["abilities"] + random_two[1]["abilities"]))
    merged = {"name": new_name, "abilities": new_abilities}
    return merged