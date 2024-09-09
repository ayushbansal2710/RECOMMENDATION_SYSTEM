import pandas as pd

books = pd.DataFrame({
    'title': [
        'Hobbit', 'Rings',
        'Alchemist', 'Solitude',
        'Prejudice', 'Gatsby',
        'Diary', 'Freedom',
        '1984', 'Fahrenheit'
    ],
    'genre': [
        'Fantasy', 'Fantasy',
        'Adventure', 'Adventure',
        'Romantic', 'Romantic',
        'Biography', 'Biography',
        'Dystopian', 'Dystopian'
    ]
})

def recommend_books(genre, books):
    genre_books = books[books['genre'].str.lower() == genre.lower()]
    if genre_books.empty:
        return pd.DataFrame()
    return genre_books

print("Select a genre by pressing the corresponding number:")
print("1. Fantasy")
print("2. Adventure")
print("3. Romantic")
print("4. Biography")
print("5. Dystopian")

user_choice = input("Enter the number of your preferred genre: ")

genre_dict = {
    '1': 'Fantasy',
    '2': 'Adventure',
    '3': 'Romantic',
    '4': 'Biography',
    '5': 'Dystopian'
}

selected_genre = genre_dict.get(user_choice, None)

if selected_genre:
    recommended_books = recommend_books(selected_genre, books)
    if not recommended_books.empty:
        print("\nRecommended Books:")
        for _, row in recommended_books.iterrows():
            print(f"{row['title']} - {row['genre']}")
    else:
        print("No books found for the selected genre.")
else:
    print("Invalid selection. Please choose a number between 1 and 5.")
