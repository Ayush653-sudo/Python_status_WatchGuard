Menu_PROMPT="\nEnter 'a' to add a movie , '1' to see your movie,'f' to find a movie by title, or 'q to quite:"
movies=[]
def add_movie():
    tilte=input("Enter a movie title:")
    director=input("Enter the movie director:")
    year=input("Enter the movie release year")
    movies.append({
        'title':tilte,
        'director':director,
        'year':year
    })
def show_movie():
    for movie in movies:
        print(movie)
def find_movie():
    title=input("Enter title of the movie which you want to find")
    for movie in movies:
        if movie["title"]==title:
            print(movie)
def menu():
    section=input(Menu_PROMPT)
    while section!='q':
        if section=="a":
            add_movie()
        elif section=="1":
            show_movie()
        elif section=="f":
            find_movie()
        else:
            print("Unknown commad")
        section=input(Menu_PROMPT)


menu()