from pathlib import Path


path = Path("cats_file.txt")

def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_info = []
            for line in file:
                cat_info = line.split(",")
                id, name, age = cat_info
                age = int(age)
                cats_info.append({"id": id, "name": name, "age": age})
        return cats_info 
    except FileNotFoundError:
        print(f"Файл {path} не найден.")       
    except Exception as e:
        print(f"Ошибка{e}" )             
                
cats_info = get_cats_info(path)
print(cats_info)                
            
            

