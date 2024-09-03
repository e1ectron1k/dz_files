from collections import defaultdict
import os

def get_cook_book(filename="files/recipes.txt"):

  cook_book = {}
  with open('recipes.txt', "r", encoding="utf-8") as f:
    current_recipe = None
    ingredients_count = 0
    ingredients = []
    for line in f:
      line = line.strip()
      if not line:
        continue
      if not current_recipe:
        current_recipe = line
        ingredients_count = int(f.readline().strip())
      else:
        ingredient_name, quantity, measure = line.split(" | ")
        ingredients.append(
          {"ingredient_name": ingredient_name, "quantity": int(quantity), "measure": measure}
        )
        if len(ingredients) == ingredients_count:
          cook_book[current_recipe] = ingredients
          current_recipe = None
          ingredients = []
  return cook_book

def get_shop_list_by_dishes(dishes, person_count):

    shop_list = defaultdict(lambda: {"measure": "", "quantity": 0})
    for dish in dishes:
        for ingredient in cook_book[dish]:
            shop_list[ingredient["ingredient_name"]]["measure"] = ingredient["measure"]
            shop_list[ingredient["ingredient_name"]]["quantity"] += (
                ingredient["quantity"] * person_count
            )
    return dict(shop_list)

def merge_files(folder_path):
 
  files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
  
  file_data = {}
  for file in files:
    file_path = os.path.join(folder_path, file)
    with open(file_path, 'r') as f:
      file_data[file] = len(f.readlines())

  sorted_files = sorted(file_data.items(), key=lambda item: item[1])

  # Объединяем файлы
  output_file_path = os.path.join(folder_path, 'merged.txt')
  with open(output_file_path, 'w') as output_file:
    for file, count in sorted_files:
      file_path = os.path.join(folder_path, file)
      with open(file_path, 'r') as input_file:
        output_file.write(f"{file}\n{count}\n")
        output_file.write(input_file.read())

  return output_file_path


folder_path = '/Users/sergeychalov/Desktop/Python_DZ/Files/3' 
output_file_path = merge_files('/Users/sergeychalov/Desktop/Python_DZ/Files/3')
print(f"Объединенный файл сохранен в {output_file_path}")

# Задача №1:
cook_book = get_cook_book()
print(cook_book)

# Задача №2:
shop_list = get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 2)
print(shop_list)

# Задача №3:
filenames = ["files/1.txt", "files/2.txt"]
merge_files(filenames, "files/merged.txt")