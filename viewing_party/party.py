# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not title or not genre or not rating:
        return None

    movie = {"title": title, "genre": genre, "rating" : rating}
    return movie

def add_to_watched(user_data, movie):
    watched_movie = user_data["watched"]
    watched_movie.append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist_movie = user_data["watchlist"]
    watchlist_movie.append(movie)
    
    return user_data 

def watch_movie(user_data, title):
    user_watchlist = user_data["watchlist"]
    user_watched = user_data["watched"]
    for movie in user_watchlist:
        if movie["title"] == title:
            user_watched.append(movie)
            user_watchlist.remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data or not user_data["watched"]:
        return 0.0
    
    watched = user_data["watched"]
    avg_rating = []

    for movie in watched:
        avg_rating.append(movie["rating"])
        
    average = sum(avg_rating) / len(avg_rating)
    return average

def get_most_watched_genre(user_data):
    if not user_data or not user_data["watched"]:
        return None
    
    watched = user_data["watched"]
    genre_list = []
    freq_genre = {}

        
    for movie in watched:
        genre = movie["genre"]
        freq_genre[genre] = 0
        genre_list.append(genre)

    for i in genre_list:
        if i in freq_genre:
            freq_genre[i] += 1
    most_freq = max(freq_genre, key=freq_genre.get)
    return most_freq

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):  
    friend_movie =[]
    user_watched = user_data["watched"]
    user_movie = [movie for movie in user_watched]
    
    for friend in user_data["friends"]:
        for title in friend["watched"]:
            friend_movie.append(title)

    for i in friend_movie:
            if i in user_movie:
                user_movie.remove(i)
    return user_movie

def get_friends_unique_watched(user_data):
    friend_movie = []
    user_watched = user_data["watched"]
    user_movie = [movie for movie in user_watched]

    friends_watched = user_data["friends"]
    for movie in friends_watched:
        for title in movie["watched"]:
            if title not in friend_movie:
                friend_movie.append(title)
    
    for title in user_movie:
        if title in friend_movie:
            friend_movie.remove(title)
            
    return friend_movie

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """
    create user_only movie list
    create friends_only movie list
    compare user and friend movie lists: remove user movies from friend list = recom_movies
    compare recom_movies to user host: remove any movies not in user host/subscription
    """
    friend_rec = []
    user_watched = user_data["watched"]
    friends = user_data["friends"]

    for friend in friends:
        for movie in friend["watched"]:
            if movie not in user_watched and movie["host"] in user_data["subscriptions"]:
                friend_rec.append(movie)

    return friend_rec

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_friend_movies(friends):
    if not friends:
        return friends
    friend_watched = [movie for movie in friends[0]["watched"]]
    return friend_watched

def get_new_rec_by_genre(user_data):
    """
    get fav genre
    compare user_movie list to friend movie list
    remove user_movies from friend movie list
    return friend list
    """

    if not user_data or not user_data["watched"]:
        return user_data["watched"]

    # get user most freq genre = fav_genre
    fav_genre = get_most_watched_genre(user_data)

    user_movies = user_data["watched"]
    friends = user_data["friends"]
    friend_movies = get_friend_movies(friends)
    
    rec_genre = []
    for movie in friend_movies:
            if movie["genre"] == fav_genre and movie not in user_movies:
                rec_genre.append(movie)
    return rec_genre

def get_rec_from_favorites(user_data):
    user_favs = []
    friends_movies = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)

    for movie in user_data["favorites"]:
        if movie not in friends_movies:
            user_favs.append(movie)
    return user_favs
    