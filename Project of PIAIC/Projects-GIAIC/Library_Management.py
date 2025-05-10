import os
import streamlit as st

# Load library from file
def load_library():
    library = []
    file_name = "Syed Hammad.txt"
    
    if not os.path.exists(file_name):
        st.warning(f"File '{file_name}' not found. Starting with an empty library.")
        return library

    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:  # Skip empty lines
                continue

            parts = line.split(",")
            if len(parts) != 4:
                st.warning(f"Skipping malformed line: {line}")
                continue

            title, author, year_str, read_str = parts
            try:
                year = int(year_str)
            except ValueError:
                st.warning(f"Skipping line with invalid year: {line}")
                continue

            # Convert the read indicator to boolean
            read = read_str.strip().lower() == "true"

            library.append({
                "title": title.strip(),
                "author": author.strip(),
                "year": year,
                "read": read
            })
    return library

# Save library to file
def save_library():
    file_name = "Syed_Hammad_Library.txt"
    with open(file_name, "w") as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['read']}\n")

# Main library data
library = load_library()

st.title("📚 Personal Library Manager")

menu = st.sidebar.radio("📌 Menu", ["Add Book", "Remove Book", "Search Book", "View Library", "Statistics"])

if menu == "Add Book":
    st.subheader("➕ Add a New Book")

    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author")
    year = st.number_input("Enter Publication Year", min_value=0, step=1)
    read = st.radio("Have you read this book?", ["Yes", "No"])

    if st.button("Add Book"):
        book = {
            "title": title,
            "author": author,
            "year": year,
            "read": read == "Yes"
        }
        library.append(book)
        save_library()
        st.success(f"✅ '{title}' added successfully!")

elif menu == "Remove Book":
    st.subheader("Remove a Book")

    book_titles = [book["title"] for book in library]
    if book_titles:
        selected_book = st.selectbox("Select a book to remove", book_titles)

        if st.button("Remove Book"):
            for book in library:
                if book["title"].lower() == selected_book.lower():
                    library.remove(book)
                    save_library()
                    st.success(f"✅ '{selected_book}' removed successfully!")
                    break
            else:
                st.error(f"❌ Sorry, '{selected_book}' is not in the library.")
    else:
        st.warning("No books available to remove.")

elif menu == "Search Book":
    st.subheader("🔍 Search for a Book")

    search_query = st.text_input("Enter the title")

    if st.button("Search"):
        found_books = [book for book in library if search_query.lower() in book["title"].lower()]

        if found_books:
            for book in found_books:
                st.write(f"📖 {book['title']} by {book['author']}")
        else:
            st.error("No books found.")

elif menu == "View Library":
    st.subheader("📚 Your Library")

    if not library:
        st.warning("No books in your library.")
    else:
        for book in library:
            st.write
