import matplotlib.pyplot as plt
import numpy as np

countries = ['Turkey', 'USA', 'UK']
months = ['January', 'February', 'March']
case_numbers = [5789, 11320, 17634]
death_numbers = [178, 786, 567]


bar_width = 0.35


bar_positions = np.arange(len(months))
fig, ax = plt.subplots()


rects1 = ax.bar(bar_positions, case_numbers, bar_width, label='Case Numbers')


rects2 = ax.bar(bar_positions + bar_width, death_numbers, bar_width, label='Death Numbers')


ax.set_xlabel('Months')
ax.set_ylabel('Numbers')
ax.set_title('COVID-19 Case and Death Numbers for Countries')
ax.set_xticks(bar_positions + bar_width / 2)
ax.set_xticklabels(months)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Displaying the graph
plt.show()