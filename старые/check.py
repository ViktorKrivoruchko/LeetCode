import matplotlib.pyplot as plt

# Названия решений
solutions = ["4RM Systems", "X5 Group", "TOUCHPLAT", "NCR Corporation"]

# Предположительная точность решений (в процентах, основано на информации из текста)
accuracy = [96, 92, 94, 90]

# Создание графика
plt.figure(figsize=(10, 6))
bars = plt.bar(solutions, accuracy, color=['#4c72b0', '#55a868', '#c44e52', '#8172b2'])

# Добавление значений на столбики
for bar, acc in zip(bars, accuracy):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f'{acc}%', ha='center', va='bottom', fontsize=12)

plt.title('Сравнительная точность нейросетевых систем касс самообслуживания', fontsize=14)
plt.ylabel('Точность распознавания (%)')
plt.ylim(85, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()