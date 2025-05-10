import streamlit as st

def load_library():
    library = []
    with open("Syed Hammad.txt", "r") as file:
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
            read = read_str.strip() == "True"

            library.append({
                "title": title.strip(),
                "author": author.strip(),
                "year": year,
                "read": read
            })
    return library

library = load_library()

def save_library():
    with open("Syed HammadAli.", "w") as file:
        for book in library:
            file.write(f"{book['title']},{book['author']},{book['year']},{book['read']}\n")

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
    selected_book = st.selectbox("Select a book to remove", book_titles)

    if st.button("Remove Book"):
        title = selected_book
        for book in library:
            if book["title"].lower() == title.lower():
                library.remove(book)
                save_library()
                st.success(f"✅ '{title}' removed successfully!")
                break
        else:
            st.error(f"❌ Sorry, '{title}' is not in the library.")

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
            st.write(f"{book['title']} by {book['author']}")

elif menu == "Statistics":
    st.subheader("📊 Library Statistics")

    total_books = len(library)
    total_read = len([book for book in library if book["read"]])
    percentage_read = (total_read / total_books) * 100 if total_books > 0 else 0

    st.write(f"Total Books: {total_books}")
    st.write(f"Books Read: {total_read}")
    st.write(f"📊 Percentage Read: {percentage_read:.2f}%")
