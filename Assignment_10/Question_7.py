import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

# Grades for two semesters
Sem1 = ['B', 'C+', 'A+', 'A+', 'B']
Sem2 = ['A+', 'A+', 'A++', 'A+', 'A++']

# Count frequencies
sem1_counts = Counter(Sem1)
sem2_counts = Counter(Sem2)

# Unique grades
grades = sorted(set(Sem1 + Sem2))
sem1_freq = [sem1_counts.get(g, 0) for g in grades]
sem2_freq = [sem2_counts.get(g, 0) for g in grades]

# Pie chart for Sem1
plt.pie(sem1_freq, labels=grades, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel1.colors)
plt.title('Grade Proportions - Sem1')
plt.show()

# Pie chart for Sem2
plt.pie(sem2_freq, labels=grades, autopct='%1.1f%%', startangle=140, colors=plt.cm.Pastel2.colors)
plt.title('Grade Proportions - Sem2')
plt.show()
