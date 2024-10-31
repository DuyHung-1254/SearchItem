import pandas as pd

# Create sample data
data = {
    "Author_Name": [
        "Nguyen Nhat Anh", "Nguyen Nhat Anh", "Nguyen Nhat Anh",
        "Nam Cao", "Nam Cao", "Nam Cao",
        "Ho Chi Minh", "Ho Chi Minh", "Ho Chi Minh"
    ],
    "Work_Title": [
        "Kinh Van Hoa", "Ticket to Childhood", "I See Yellow Flowers on the Green Grass",
        "Chi Pheo", "Old Man Hac", "Life Worn Out",
        "Diary in Prison", "The Colonial Regime on Trial", "Revolutionary Road"
    ],
    "Revised_Version": [
        "Kinh Van Hoa (Revised)", "Ticket to Childhood (Improved)", "I See Yellow Flowers on the Green Grass (Updated)",
        "Chi Pheo (Revised)", "Old Man Hac (Updated)", "Life Worn Out (Revised)",
        "Diary in Prison (Revised)", "The Colonial Regime on Trial (Updated)", "Revolutionary Road (Revised)"
    ]
}

# Create DataFrame and save as Excel file
df = pd.DataFrame(data)
