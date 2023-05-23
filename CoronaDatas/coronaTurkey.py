import matplotlib.pyplot as plt

# Daily case numbers in Turkey
dates = ['01/01/2022', '02/01/2022', '03/01/2022', '04/01/2022', '05/01/2022']
cases = [179, 231, 186, 289, 175]

plt.plot(dates, cases, marker='o')

plt.xlabel('Date')
plt.ylabel('Daily Cases')
plt.title('COVID-19 Cases in Turkey')


plt.xticks(rotation=45)
plt.show()
