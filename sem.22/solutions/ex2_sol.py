import matplotlib.pyplot as plt
import numpy as np

# височини
heights = np.array([160, 155, 163, 155, 190, 195, 168, 172, 162, 205])

# статистически мерки
mean_height = np.mean(heights) #Средна височина
std_dev = np.std(heights) #Стандартно отклонение

# сортиране
sorted_heights = np.sort(heights)

# категоризиране
short_category = sorted_heights[sorted_heights < mean_height - std_dev]
medium_category = sorted_heights[(sorted_heights >= mean_height - std_dev) & (sorted_heights <= mean_height + std_dev)]
tall_category = sorted_heights[sorted_heights > mean_height + std_dev]

# Намиране на броя за всяка категория
short_count = len(short_category)
medium_count = len(medium_category)
tall_count = len(tall_category)

# Създаване на стълбовидна диаграма
categories = ["Short", "Medium", "Tall"]
counts = [short_count, medium_count, tall_count]
plt.bar(categories, counts)

# Персонализиране на диаграмата
plt.title("Categorized Heights")
plt.xlabel("Height Category")
plt.ylabel("Number of People")

# Display the plot
plt.show()
