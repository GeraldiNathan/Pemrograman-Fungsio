movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Function Tampil Data
def get_movie_data(title):
    movie = next((m for m in movies if m["title"] == title), None)
    return movie

# Count Movie by genre menggunakan filter dan list
def count_movies_by_genre(genre):
    count = len(list(filter(lambda movie: movie["genre"] == genre, movies)))
    return count

# Function avarage rating by years
def average_rating_by_year(year):
    movies_of_year = list(filter(lambda movie: movie["year"] == year, movies))
    if not movies_of_year:
        return None
    total_rating = sum(map(lambda movie: movie["rating"], movies_of_year))
    return total_rating / len(movies_of_year)

# Function Rating Tertinggi
def highest_rated_movie():
    highest_rated = max(movies, key=lambda movie: movie["rating"])
    return highest_rated

while True:
    print("Pilih Tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")

    task = input("Masukkan nomor tugas (1/2/3/4/5): ")

    if task == "1":
        genre_input = input("Masukkan genre film untuk menghitung jumlah: ")
        genre_count = count_movies_by_genre(genre_input)
        print(f"\n\nJumlah film genre {genre_input}: {genre_count}")
    elif task == "2":
        year_input = int(input("Masukkan tahun rilis untuk menghitung rata-rata rating: "))
        average_rating = average_rating_by_year(year_input)
        if average_rating is not None:
            print(f"Rata-rata rating film tahun {year_input}: {average_rating}")
        else:
            print(f"Tidak ada film yang dirilis pada tahun {year_input}.")
    elif task == "3":
        best_movie = highest_rated_movie()
        print(f"Film dengan rating tertinggi: {best_movie['title']} ({best_movie['rating']})")
    elif task == "4":
        selected_movie_title = input("Masukkan judul film yang ingin ditampilkan: ")
        selected_movie = get_movie_data(selected_movie_title)
        if selected_movie:
            print(selected_movie)
        else:
            print("Film tidak ditemukan.")
    elif task == "5":
        break
    else:
        print("Masukan tidak valid. Pilih nomor tugas yang sesuai.")
