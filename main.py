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

final_json = {}
def modern(data, obj):
    global final_json
    for element in data['costs']:
        if(element['technology_type_id'] == obj['technology_type_id']):
            rate_array = []
            for rate in element['detail']['rates']:
                if(rate['rate_id'] == obj['rate_id']):
                    rate_array.append(rate)
                    element['detail']['rates'].remove(rate)
            if(len(rate_array)> 0):
                element['price'] = float(element['price'] - float(rate_array[0]['price']))
    final_json['new_object'] = data

def array_loop(json_array, data):
    for element in data:
        modern(json_array, element)

changes = [
    {
    'technology_type_id': 7,
    'rate_id': 155,
    },
    {
        'technology_type_id': 6,
        'rate_id': 150,
    },
    {
        'technology_type_id': 6,
        'rate_id': 152,
    },
    {
        'technology_type_id': 5,
        'rate_id': 161,
    },
    {
        'technology_type_id': 7,
        'rate_id': 166,
    },
]
array_loop(newresult, changes)
#modern(newresult)
#print(final_json)
change_location = {}
def change_location(data, props):
    global change_location
    for element in data['new_object']['costs']:
        if(element['location_id'] == props['location_id']):
            element['location_id'] = props['new_location_id']
    change_location = data

props = [
    {
        'location_id': 91,
        'new_location_id': 82
    }
]

for location in props:
    change_location(final_json, location)

change_material_price = {}
def material_price(data, props):
    global change_material_price
    for element in data['new_object']['costs']:
        for element_2 in element['detail']['rates']:
            if(element_2['materials'] != None):
                for element_3 in element_2['materials']:
                    if(element_3['material_id'] == props['material_id']):
                        element_3['price'] = props['price_koef'] * element_3['price']
    change_material_price = data

material_price_changes = [
    {'material_id': 171,
     'price_koef': 1.8}
]
for element in material_price_changes:
    material_price(change_location, element)

with open("newfile.json", "w", encoding='utf-8') as filenewrates:
        json.dump(change_material_price, filenewrates, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
        filenewrates.close()

#    with open("all_regions_21_04_2023-new.json", "w", encoding='utf-8') as filenewrates:
 #       json.dump(newresult, filenewrates, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
  #      filenewrates.close()






