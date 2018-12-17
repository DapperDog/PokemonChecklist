import json
import os

for filename in os.listdir('cards'):
    with open('cards/'+filename) as f:
        print filename
        data = json.load(f)
        children = []
        for v in data:
            name = v["name"]
            number = v["number"]
            if "rarity" in v:
                rarity = v["rarity"]
            else:
                rarity = "unknown"
            series = v["series"]
            set = v["set"]
            id = v["id"]
            children.append({"name": name,"number":number,"rarity":rarity,"series":series,"set":set,"id":id})
        with open('simplifiedcards/'+filename, 'w') as outfile:
            json.dump(children, outfile, indent=2)
