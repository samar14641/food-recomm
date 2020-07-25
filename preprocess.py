import os
# import unicodedata


toRemove = set(['& half', '& half\n'])  # list of ingredients to remove

def cleanIngredients():
    filePath = os.getcwd() + '/Data/annotations/ingredients_simplified_Recipes5k.txt'
    cleaned = []

    with open(filePath) as dataset:
        line = dataset.readline().lower().strip()
        
        while line:
            # line = unicodedata.normalize('NFKD', line).encode('ascii', 'ignore').decode('utf-8')  # this didn't work

            ingredients = ','.join(list(set([i.strip() for i in line.split(',') if i not in toRemove])))
            if '\\u' in ingredients:
                ingredients = ingredients.replace('\\u00ae', '').replace('\\u00e2', 'a').replace('\\u00e8', 'e').replace('\\u00e9', 'e').replace('\\u00ee', 'i').replace('\\u00fa', 'u').replace('\\u00fc', 'u').replace('\\u2122', '')
                
            cleaned.append(ingredients)

            line = dataset.readline().lower().strip()

    opFile = open(os.getcwd() + '/Data/annotations/cleaned_ingredients.txt', 'w+')

    for i in cleaned:
        opFile.write(i + '\n')

    opFile.close()

def uniqueIngredients():
    filePath = os.getcwd() + '/Data/annotations/cleaned_ingredients.txt'
    ingredients = []

    with open(filePath) as dataset:
        line = dataset.readline().strip()

        while line:
            ingredients.extend(line.split(','))

            line = dataset.readline().strip()

    ingredients = set(ingredients)

    opFile = open(os.getcwd() + '/Data/annotations/all_ingredients.txt', 'w+')

    for i in ingredients:
        opFile.write(i + '\n')

    opFile.close()

# cleanIngredients()
uniqueIngredients()