import json
import os

seriesName = 'Series/XY Series/'
for filename in os.listdir(seriesName):
    if filename!='simplifiedcards':
        with open(seriesName+filename) as f:
            print filename
            data = json.load(f)
            output = {"cardVariants":["core","reverse"],"version":1.0}
            output['coreCards'] = []
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
                output['coreCards'].append({"name": name,"number":number,"rarity":rarity,"id":id})
            with open(seriesName+'simplifiedcards/'+filename, 'w') as outfile:
                output['additionalCards'] = []
                output['other'] = []
                json.dump(output, outfile, indent=2)
