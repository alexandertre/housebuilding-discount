import json

with open('all_regions_21_04_2023.json', encoding="utf-8") as f:
    data = json.loads(f.read())

    windowtypes = {'20': 0.6, '201': 0.58, '202': 0.71, '203': 0.82, '204': 0.58, '205': 0.71, '206': 0.82}

# сначала считаем забор
    def costsfun (data):
        costs = data['costs']
        costscount = []
        newrates = []
        for costsEl in costs:
            if(costsEl['building_category_id'] == 10):
                costscount.append(costsEl['detail'])
                newrates.append(costsEl['detail'])
                #print(costsEl['detail'])
                for costsElDetails in costsEl['detail']['rates']:
                    costsElDetails['price'] = costsElDetails['price'] * 0.57
                    costsElDetails['price'] = round(costsElDetails['price'], 2)
                    #print(costsElDetails['price'])
                costsEl['price'] = costsElDetails['price']
                costsEl['price'] = round(costsEl['price'], 2)
        return data

    newdata = costsfun(data)

    def okna(newdata, windowtypes):
        costs = newdata['costs']
        costscount = []
        newrates = []
        temp = []
        for windowEl in windowtypes.items():
            for costsEl in costs:
               if(costsEl['technology_type_id'] == int(windowEl[0])):
                costscount.append(costsEl['detail'])
                newrates.append(costsEl['detail'])
                #print(costsEl['detail'])
                for costsElDetails in costsEl['detail']['rates']:
                    costsElDetails['price'] = costsElDetails['price'] * windowEl[1]
                    costsElDetails['price'] = round(costsElDetails['price'], 2)
                    temp.append(costsElDetails['price'])
                    #print(costsElDetails['price'])
                    costsEl['price'] = sum(temp)
                    costsEl['price'] = round(costsEl['price'], 2)
                temp = []
        return newdata


# считаем окна и прочие элементы
    newresult = okna(newdata, windowtypes)

    with open("all_regions_21_04_2023-new.json", "w", encoding='utf-8') as filenewrates:
        json.dump(newresult, filenewrates, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
        filenewrates.close()






