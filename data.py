sample = {
  "data": {
      "samples": {
        "triggers": {
          "any_new_hero": None,
        },
        "triggerFieldValidations": {
        },
        "actions": {
          "generate_a_hero": {
            "gender": "Male"
          }
        },
        "actionRecordSkipping": {
        }
      }
    }
  }

heroes_list = ["Super Man", "Wonder Woman", "Spider Man", "Black Panther", 
              "Green Arrow", "Captain America", "Iron Fist", "Professor X", 
              "Silver Surfer", "Doctor Strange", "Captain Marvel", "Beast Boy",
              "Martian Manhunter", "Scarlet Witch", "Sailor Moon", "Poison Ivy", 
              "Black Widow", "Wonder Girl", "Miss Martian", "Big Barda", 
              "Goblin Queen", "Emma Frost", "Bomb Queen", "Bumble Bee",
              "Jesse Quick"]

heroes_data = {
  "data": [
    {
      "name": "Super Man",
      "gender": "male",
      "abilities": [
        "superhuman strength", "super speed"
      ],
      "meta": {
        "id": "b32a4f0002b511e7a1c5d0577b0ce54e",
        "timestamp": 1488836083
      }
    },
    {
      "name": "Wonder Woman",
      "gender": "female",
      "abilities": [
        "superhuman strength", "super speed"
      ],
      "meta": {
        "id": "1c472ee102b611e78e2ed0577b0ce54e",
        "timestamp": 1488836098
      }
    },
    {
      "name": "Spider Man",
      "gender": "male",
      "abilities": [
        "spider-sense", "wall crawling"
      ],
      "meta": {
        "id": "260bf23002b611e7a245d0577b0ce54e",
        "timestamp": 1488836099
      }
    },
    {
      "name": "Black Panther",
      "gender": "male",
      "abilities": [
        "super reflexes", "enhanced agility"
      ],
      "meta": {
        "id": "43e279c002c811e7bb8fd0577b0ce54e",
        "timestamp": 1488836199
      }
    },
    {
      "name": "Green Arrow",
      "gender": "male",
      "abilities": [
        "master archer"
      ],
      "meta": {
        "id": "4ca9550f02c811e7ae67d0577b0ce54e",
        "timestamp": 1488836229
      }
    },
    {
      "name": "Captain America",
      "gender": "male",
      "abilities": [
        "super speed", "enhanced endurance"
      ],
      "meta": {
        "id": "546e9ee102c811e7bc56d0577b0ce54e",
        "timestamp": 1488836248
      }
    },
    {
      "name": "Iron Fist",
      "gender": "male",
      "abilities": [
        "master martial art abilities", "telepathy"
      ],
      "meta": {
        "id": "5badefcf02c811e78ecdd0577b0ce54e",
        "timestamp": 1488836258
      }
    },
    {
      "name": "Professor X",
      "gender": "male",
      "abilities": [
        "telepathy", "enhanced psionic powers"
      ],
      "meta": {
        "id": "60588c1e02c811e7b7b5d0577b0ce54e",
        "timestamp": 1488836262
      }
    },
    {
      "name": "Silver Surfer",
      "gender": "male",
      "abilities": [
        "avility to navigate through interstellar space and hyperspace", "super speed"
      ],
      "meta": {
        "id": "690ddb4002c811e78ed7d0577b0ce54e",
        "timestamp": 1488836272
      }
    },
    {
      "name": "Doctor Strange",
      "gender": "male",
      "abilities": [
        "manipulate forces of the universe"
      ],
      "meta": {
        "id": "69c9ff4f02c811e79bb5d0577b0ce54e",
        "timestamp": 1488836280
      }
    },
    {
      "name": "Captain Marvel",
      "gender": "male",
      "abilities": [
        "superhuman strength", "enhanced stamina"
      ],
      "meta": {
        "id": "6a320ff002c811e7ac44d0577b0ce54ee",
        "timestamp": 1488836289
      }
    },
    {
      "name": "Beast Boy",
      "gender": "male",
      "abilities": [
        "therianthropy", "shapeshifting"
      ],
      "meta": {
        "id": "7ba2c8b002c811e78595d0577b0ce54e",
        "timestamp": 1488836299
      }
    },
    {
      "name": "Martian Manhunter",
      "gender": "male",
      "abilities": [
        "invisibility", "telekinesis"
      ],
      "meta": {
        "id": "81ac58c002c811e7b28ad0577b0ce54e",
        "timestamp": 1488836312
      }
    },
    {
      "name": "Scarlet Witch",
      "gender": "female",
      "abilities": [
        "probability manipulation", "reality warping"
      ],
      "meta": {
        "id": "821ccdcf02c811e79d77d0577b0ce54e",
        "timestamp": 1488836322
      }
    },
    {
      "name": "Jesse Quick",
      "gender": "female",
      "abilities": [
        "superhuman strength", "flight"
      ],
      "meta": {
        "id": "827af36102c811e7a9a1d0577b0ce54e",
        "timestamp": 1488836332
      }
    },
    {
      "name": "Sailor Moon",
      "gender": "female",
      "abilities": [
        "elemental powers", "transformation"
      ],
      "meta": {
        "id": "903a3cde02c811e7b4f9d0577b0ce54e",
        "timestamp": 1488836345
      }
    },
    {
      "name": "Poison Ivy",
      "gender": "female",
      "abilities": [
        "manipulation of plant life", "immunity to all toxins, bacteria, and viruses"
      ],
      "meta": {
        "id": "90d432f002c811e7bfb2d0577b0ce54e",
        "timestamp": 1488836352
      }
    },
    {
      "name": "Black Widow",
      "gender": "female",
      "abilities": [
        "marksman mastership", "mastery of all weapons"
      ],
      "meta": {
        "id": "95f6e57002c811e79a4cd0577b0ce54e",
        "timestamp": 1488836362
      }
    },
    {
      "name": "Wonder Girl",
      "gender": "female",
      "abilities": [
        "superhuman strength", "super agility"
      ],
      "meta": {
        "id": "965c850f02c811e781a9d0577b0ce54e",
        "timestamp": 1488836368
      }
    },
    {
      "name": "Miss Martian",
      "gender": "female",
      "abilities": [
        "regeneration", "longevity"
      ],
      "meta": {
        "id": "abfe646102c811e7a66bd0577b0ce54e",
        "timestamp": 1488836378
      }
    },
    {
      "name": "Big Barda",
      "gender": "female",
      "abilities": [
        "superhuman strength", "resistance to blunt force trauma, temperture and pressure extremes"
      ],
      "meta": {
        "id": "ad671c1e02c811e7aaadd0577b0ce54e",
        "timestamp": 1488836398
      }
    },
    {
      "name": "Goblin Queen",
      "gender": "female",
      "abilities": [
        "psychokinesis", "teleportation"
      ],
      "meta": {
        "id": "bc68d0b002c811e788ded0577b0ce54e",
        "timestamp": 1488836452
      }
    },
    {
      "name": "Emma Frost",
      "gender": "female",
      "abilities": [
        "mind control", "shapeshifting"
      ],
      "meta": {
        "id": "bceea28002c811e7bb99d0577b0ce54e",
        "timestamp": 1488836452
      }
    },
    {
      "name": "Bomb Queen",
      "gender": "female",
      "abilities": [
        "expertise in explosive devices", "skilled fighter"
      ],
      "meta": {
        "id": "c4e0efc002c811e79114d0577b0ce54e",
        "timestamp": 1488836452
      }
    },
    {
      "name": "Bumble Bee",
      "gender": "female",
      "abilities": [
        "create painful electric blasts", "flight"
      ],
      "meta": {
        "id": "cbead8cf02c811e79ef2d0577b0ce54e",
        "timestamp": 1488836452
      }
    }
  ]
}

generated_heroes = {}

error_channel_key = {
  "errors": [
      {
        "message": "Invalid channel key"
       }
  ]
}
