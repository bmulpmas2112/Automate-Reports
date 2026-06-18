Because I want to work in analysis. I learnt how to use Python to create PDF reports with the data from an Excel spreadsheet

# Code

import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv ('Money.csv')

data.dropna(inplace=True)


category_data = data['Category'].value_counts()

plt.figure(figsize=(10,7))
plt.pie(category_data, labels=category_data.index,autopct='%1.1f%%', startangle=140)

plt.title('Amount and Description')
plt.axis('equal')
plt.savefig('report_pie.png')


from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('report.pdf') as pdf:
    plt.figure(figsize=(8,7))
    plt.pie(category_data, labels=category_data.index,autopct='%1.1f%%')
    plt.title('Percentage of Categories')
    pdf.savefig()
    plt.close()

print("Report succesfully created")
