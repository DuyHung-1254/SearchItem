import pandas as pd

# Đọc dữ liệu từ file Excel
file_path = "./database.xlsx"
df = pd.read_excel(file_path)

# Tạo file Markdown từ dữ liệu
with open("excel_data.md", "w", encoding="utf-8") as f:
    f.write("# Dữ Liệu Tác Giả\n\n")
    grouped = df.groupby("Author_Name")
    for author, group in grouped:
        f.write(f"## {author}\n")
        for _, row in group.iterrows():
            f.write(f"- Tác phẩm: {row['Work_Title']}\n")
            f.write(f"  - Phiên bản chỉnh sửa: {row['Revised_Version']}\n\n")

print("Đã tạo file excel_data.md")