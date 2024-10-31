import streamlit as st
import pandas as pd 

# Đọc dữ liệu từ file Excel
df = pd.read_excel("./database.xlsx")
# Giao diện nhập dữ liệu với Streamlit
st.title("Search Works by Author or Title")

# Thêm thanh chọn để chọn phương thức tìm kiếm
search_option = st.selectbox("Search by:", ("Author", "Work Title"))

# Nhập dữ liệu tùy theo lựa chọn
if search_option == "Author":
    author_name = st.text_input("Enter author name:")
    # Tìm và hiển thị tác phẩm của tác giả
    if author_name:
        results = df[df['Author_Name'].str.contains(author_name, case=False)]
        if not results.empty:
            st.write(f"Works by {author_name}:")
            for title in results['Work_Title']:
                st.write(f"- {title}")
        else:
            st.write("Author not found in the database.")
            
elif search_option == "Work Title":
    work_title = st.text_input("Enter work title:")
    # Tìm và hiển thị tác giả của tác phẩm
    if work_title:
        results = df[df['Work_Title'].str.contains(work_title, case=False)]
        if not results.empty:
            st.write(f"Authors of '{work_title}':")
            for author in results['Author_Name']:
                st.write(f"- {author}")
        else:
            st.write("Work title not found in the database.")
