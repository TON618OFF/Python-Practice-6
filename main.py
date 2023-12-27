# %% [markdown]
# Цель: на данной практической работе необходимо использовать датасет с прошлой практической работы и визуализировать данные в виде графиков. 
# 
# Вы должны использовать:
# 
# 1. Линейный график - минимум 3 штуки (можете использовать наложение графиков)
# 2. Столбчатая диаграмма- минимум 3 штуки (можете также использовать наложение)
# 3. Круговая диаграмма - минимум 2 штуки
# 4. Диаграмма рассеяния - минимум 2 штуки
# 5. Гистограмма - минимум 3 штуки
# 
# Для каждого графика необходимо сделать вывод, вы должны написать, что у вас изображено на графике, как вы это получили, какие выводы сделали исходя из полученных данных
# 

# %% [markdown]
# 1. Линейные графики.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (15, 5))
WoT = WOT.astype(str).sort_values("Battles")
plt.plot(WoT["Name"].head(), WoT["Battles"].head(), color = "green", marker = "o", markersize = 5)
plt.title('Статистика боёв')
plt.xlabel('Имена игроков')
plt.ylabel('Кол-во боёв')
plt.grid()
plt.legend()
plt.show()


# %% [markdown]
# Второй график:

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (15, 5))
WoT = WOT.astype(str).sort_values("Average Tier")
plt.plot(WoT["Name"].head(), WoT["Average Tier"].head(), color = "green", marker = "o", markersize = 5)
plt.title('Уровень "крутости" игроков')
plt.xlabel('Имена игроков')
plt.ylabel('"Крутость"')
plt.grid()
plt.legend()
plt.show()

# %% [markdown]
# Третий график:

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (15, 5))
WoT = WOT.astype(str).sort_values("Average Kills")
plt.plot(WoT["Name"].head(), WoT["Average Kills"].head(), color = "green", marker = "o", markersize = 5, label = "крутость")
plt.title('Уровень "крутости" игроков')
plt.xlabel('Имена игроков')
plt.ylabel('Количество убийств')
plt.legend()
plt.grid()
plt.show()

# %% [markdown]
# ПРИЧЕЧАНИЕ:
# 
# ГРАФИК ИДЁТ РОВНОЙ ЛИНИЕЙ ИЗ-ЗА ТОГО, ЧТО ДАННЫЕ В САМОЙ ТАБЛИЦЕ НЕ ОТСОРТИРОВАНЫ ПО ЗНАЧЕНИЯМ, ПОЭТОМУ ОН БЕРЁТ ПРОСТО ПОСЛЕДНИЕ 7 ЗНАЧЕНИЙ.

# %% [markdown]
# 2. Столбчатая диаграмма.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (10, 5))
WoT = WOT.astype(str).sort_values("Battles")
plt.bar(WoT["Name"].head(), WoT["Battles"].head(), label = "Battles")
plt.title('Кол-во сражений')
plt.xlabel('Имена')
plt.ylabel('Кол-во боёв')
plt.legend()
plt.show()

# %% [markdown]
# Второй график:

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (10, 5))
WoT = WOT.astype(str).sort_values("Average Tier")
plt.bar(WoT["Name"].head(), WoT["Average Tier"].head(), label = "Average Tier")
plt.title('Средняя "крутость" игрока')
plt.xlabel('Имена')
plt.ylabel('Уровень крутости')
plt.legend()
plt.show()

# %% [markdown]
# Третий график:

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (10, 5))
WoT = WOT.astype(str).sort_values("Win Rate")
plt.bar(WoT["Name"].head(), WoT["Win Rate"].head(), label = "Win Rate")
plt.title('Процентность побед')
plt.xlabel('Имена')
plt.ylabel('Процент побед')
plt.legend()
plt.show()

# %% [markdown]
# 3. Круговая диаграмма.
# 

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (25, 20))
quantity = WoT['Win Rate'].value_counts().tail(15)
plt.pie(quantity, labels = quantity.index, autopct = '%1.1f%%', colors = ['pink', 'green', 'red', 'purple'])
plt.title('Соотношение процентности побед')
plt.legend()
plt.show()

# %% [markdown]
# Вторая диаграмма:

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (25, 20))
quantity = WoT['Battles'].value_counts().tail(5)
plt.pie(quantity, labels = quantity.index, autopct = '%1.1f%%', colors = ['pink', 'green', 'red', 'purple'])
plt.title('Кол-во боёв')
plt.legend()
plt.show()

# %% [markdown]
# Третья диаграмма:

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (25, 20))
quantity = WoT['Average Tier'].value_counts().tail(6)
plt.pie(quantity, labels = quantity.index, autopct = '%1.1f%%', colors = ['yellow', 'black'])
plt.title('Средняя "крутость"')
plt.legend()
plt.show()

# %% [markdown]
# 4. Диаграммы рассеяния.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (13, 7))
WoT = WOT.astype(str).sort_values("Battles")
plt.scatter(WoT['Name'].head(7), WoT['Battles'].head(7), color = 'purple')
plt.title('Кол-во сражений')
plt.xlabel('Имена')
plt.ylabel('Кол-во боёв')
plt.legend()
plt.show()

# %% [markdown]
# Вторая диаграмма рассеивания:

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (13, 7))
WoT = WOT.astype(str).sort_values("Win Rate")
plt.scatter(WoT['Name'].head(7), WoT['Win Rate'].head(7), color = 'purple')
plt.title('Процентность побед')
plt.xlabel('Имена')
plt.ylabel('Кол-во боёв')
plt.legend()
plt.show()

# %% [markdown]
# 5. Гистограмма.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (8, 3))
WoT = WOT.astype(str).sort_values("Battles").head(6)
plt.hist(WoT['Battles'], bins = 30, color = ["black"], edgecolor = 'yellow', alpha = 0.7, label = 'Боёв')
plt.title('Кол-во сражений')
plt.ylabel('Кол-во боёв')
plt.legend()
plt.show()

# %% [markdown]
# Вторая гистограмма:

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (8, 3))
WoT = WOT.astype(str).sort_values("Win Rate").head(6)
plt.hist(WoT['Win Rate'], bins = 30, color = ["yellow"], edgecolor = 'black', alpha = 0.7, label = 'Процентность побед')
plt.title('Процентность побед')
plt.ylabel('Процент побед')
plt.legend()
plt.show()

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


WOT = pd.read_csv("WoT_clear.csv")
plt.figure(figsize = (11, 6))
WoT = WOT.astype(str).sort_values("Average Tier").head(6).sort_values("Average Tier")
plt.hist(WoT['Average Tier'], bins = 30, color = ["black"], edgecolor = 'yellow', alpha = 0.7, label = 'Крутость')
plt.title('"Крутость" игроков')
plt.ylabel('Средняя "крутость"')
plt.legend()
plt.show()


