with open("all_regions_21_04_2023-new.json", "w", encoding='utf-8') as filenewrates:
    json.dump(newresult, filenewrates, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))
    filenewrates.close()