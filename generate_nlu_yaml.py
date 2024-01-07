import pandas as pd
import os

# Load your Excel file
data = pd.read_excel('MOCK_DATA.xlsx')

# Extract software names from the 'Software' column
software_names = data['Software'].tolist()

# Create the directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Path to save the nlu.yml file inside the 'data' folder
file_path = os.path.join('data', 'nlu.yml')

# Create the NLU YAML content
nlu_content = "version: '3.0'\n\nnlu:\n  - intent: get_architect\n    examples:\n      - text: Which software's architect are you looking for?\n      - text: Whose architect information do you need?\n"

# Add software names to the inform intent examples
nlu_content += "  - intent: inform\n    examples:\n"
for software in software_names:
    nlu_content += f"      - text: I need information about [{software}](Software)\n"

# Write the generated content to the nlu.yml file inside the 'data' folder
with open(file_path, 'w') as file:
    file.write(nlu_content)

print(f"nlu.yml file generated at {file_path}")
