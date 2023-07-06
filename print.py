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

def readxlsx(data):
    global costs_list
    if(data):
        wookbook = openpyxl.load_workbook(data)
         # Define variable to read the active sheet:
        worksheet = wookbook.active
        # Iterate the loop to read the cell values
        for i in range(0, worksheet.max_row):
            for col in worksheet.iter_cols(1, worksheet.max_column):
                costs_list.append({"building_category_id": col[3].value,
                                   "technology_type_id": col[4].value,
                                   "koef_etazh": col[5].value,
                                   "koef_m2_doma": col[6].value,
                                   "koef_m2_uchastka": col[7].value,
                                   "location_id": col[1].value,
                                   "price": col[8].value,
                                   "detail": {
                                   }
                                   })
                #print(col[i].value, end="\t\t")
            print('success')
    else:
        print('reading file error')

def test(data):
    global costs_list
    if(data):
        wookbook = openpyxl.load_workbook(data)
         # Define variable to read the active sheet:
        worksheet = wookbook.active
        # Iterate the loop to read the cell values
        print('rows', worksheet.max_row)
        print('cols', worksheet.max_column)

#readxlsx(costs)
#f.write(str(costs_list) + '\r\n')
test(costs)

#with open("costs.json", "w", encoding='utf-8') as filecosts:
 #   json.dump(costs_list, filecosts, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
  #  filecosts.close()
#print(costs_list)