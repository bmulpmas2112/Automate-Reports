# This is a python script aimed to automate reports
#Columns in Money.csv are; Date, Description, Amount, Balance and Category

import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
data = pd.read_csv ('Money.csv')


# Clean and preprocess the data
data.dropna(inplace=True)


category_data = data['Category'].value_counts()

# Create a Pie chart using matplotlib

plt.figure(figsize=(10,7))
plt.pie(category_data, labels=category_data.index,autopct='%1.1f%%', startangle=140)

plt.title('Amount and Description')
plt.axis('equal')
plt.savefig('report_pie.png')

# Generate a report in PDF format

from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('report.pdf') as pdf:
    plt.figure(figsize=(8,7))
    plt.pie(category_data, labels=category_data.index,autopct='%1.1f%%')
    plt.title('Percentage of Categories')
    pdf.savefig()
    plt.close()

print("Report succesfully created")