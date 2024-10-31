import pandas as pd

# Load data from Excel file
df = pd.read_excel("./Base Luce Abélès modifiée TABLEAU.xlsx")

# Convert DataFrame to JSON
json_data = df.to_json(orient='records')

# Save to a JSON file
with open("Base Luce Abélès modifiée TABLEAU.json", "w", encoding='utf-8-sig') as json_file:
    json_file.write(json_data)

