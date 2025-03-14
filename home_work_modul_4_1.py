from pathlib import Path


path = Path("salary_file.txt")

def total_salary(path):
    
    try:
        with open(path, "r", encoding="utf-8") as file:
            salary = list()
            for line in file:
                salary.append (float(line.split(",")[1]))
            total = sum(salary)
            average = total / len(salary)
            total_salary = (total, average)
        return total_salary  
    except FileNotFoundError:
        print(f"Файл {path} не найден.")    
    except Exception as e:
        print(f"Ошибка{e}")       
                
                    
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


                
            
    