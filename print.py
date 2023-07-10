# Import openyxl module
import openpyxl
import json
import xlrd

f = open('results.txt', 'w', encoding='utf-8')

rates = './data/rates.xlsx'
costs = './data/costs.xlsx'
materials = './data/materials.xlsx'
# Define variable to load the wookbook
costs_list = []
#new_costs_list1 = str(costs_list)

newcosts = {'costs': costs_list}


def readxlsx(data):
    global costs_list

    if (data):
        wookbook = openpyxl.load_workbook(data)
        # Define variable to read the active sheet:
        worksheet = wookbook.active
        # Iterate the loop to read the cell values

        # for col in worksheet.iter_cols(1, worksheet.max_column):

        for col in worksheet.iter_rows(min_row=2, max_row=100):
            new_materials = []
            if col[14].value:
                new_materials.append({'material_id': col[14].value,
                'price': str(col[13].value)})
                #material = '[{"material_id":'+ str(col[14].value) + ', "price": ' + str(col[13].value) + '}]'
                #new_material = material.replace('"[', '[')
                #new2_material = new_material.replace(']"', ']')
                #material=new2_material
            else:
                new_materials.append("null")
                #material = material.replace('"', '')

            rates = []
            detail = {}
            rate = {'rate_id': col[9].value, 'price': float(col[11].value), 'materials': new_materials}
            rates.append(rate)
            detail['rates'] = rates
            costs_list.append({'building_category_id': col[3].value,
                               'technology_type_id': col[4].value,
                               'koef_etazh': col[5].value,
                               'koef_m2_doma': col[6].value,
                               'koef_m2_uchastka': col[7].value,
                               'location_id': col[1].value,
                               'price': float(col[8].value),
                               'detail': detail
                               })
            # print(col[i].value, end="\t\t")
            #print('success')

    else:
        print('reading file error')


def test(data):
    global costs_list
    if (data):
        wookbook = openpyxl.load_workbook(data)
        # Define variable to read the active sheet:
        worksheet = wookbook.active
        # Iterate the loop to read the cell values
        print('rows', worksheet.max_row)
        print('cols', worksheet.max_column)
        for col in worksheet.iter_rows(1, worksheet.max_row):
            print(col[0].value)


readxlsx(costs)
result = str(newcosts)
result = result.replace('"[', '[')
result = result.replace(']"', ']')
result = result.replace('"null"', 'null')
result = result.replace("'null'", "null")
result = result.replace("'", '"')

#result = result.replace('\"', '"')
materials_list=[]
def read_obj(data):
    global materials_list
    new_obj = {}
    for obj in data:
        detail = obj['detail']
        cat_price = obj['price']
        materials = detail['rates'][0]
        material_obj = {}
        material_obj['cat_price'] = cat_price
        single_material = materials['materials'][0]
        one_material = {}
        one_material['material_id'] = single_material['material_id']
        one_material['price'] = single_material['price']
        material_obj['single_material'] = one_material
        materials_list.append(material_obj)

read_obj(costs_list)

#запись в файл работает
#f.write(result)
print(materials_list)

#with open("new-costs.json", "w", encoding='utf-8') as filenewrates:
    #json.dump(result, filenewrates, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    #filenewrates.close()
# test(costs)

# with open("costs.json", "w", encoding='utf-8') as filecosts:
#   json.dump(costs_list, filecosts, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
#  filecosts.close()
# print(costs_list)