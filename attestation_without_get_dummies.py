#здесь идем через создание столбцов вручную.
# создаем исходный DataFrame data.
# получаем уникальные значения из столбца whoAmI.
# для каждого уникального значения создаем новый столбец, где 1 указывает на наличие этого значения в исходном столбце, а 0 — на отсутствие.
# удаляем исходный столбец whoAmI, так как он больше не нужен.
# теперь DataFrame data будет содержать столбцы 'robot' и 'human' в one-hot кодированном виде.

import pandas as pd
import random

# Создание исходного DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создание one-hot кодированного DataFrame
unique_values = data['whoAmI'].unique()
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаление исходного столбца 'whoAmI'
data = data.drop(columns=['whoAmI'])

data.head()