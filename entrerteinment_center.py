import fresh_tomatoes
import media

pulp_fiction = media.Movie('Pulp Fiction',
                           'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits.',
                           'https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg',
                           'https://www.youtube.com/watch?v=5ZAhzsi1ybM')

joker = media.Movie('Joker',
                    'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society',
                    'https://upload.wikimedia.org/wikipedia/pt/6/63/Joker_%282019%29.jpg',
                    'https://www.youtube.com/watch?v=zAGVQLHvwOY')

interstellar = media.Movie('Interstellar',
                           'A team of explorers travel through a wormhole in space',
                           'https://upload.wikimedia.org/wikipedia/pt/3/3a/Interstellar_Filme.png',
                           'https://www.youtube.com/watch?v=Lm8p5rlrSkY')

the_lord_of_the_rings_the_return_of_the_king = media.Movie('The Lord of the Rings: The Return of the King',
                                                           'Gandalf and Aragorn lead the World of Men against Sauron',
                                                           'https://upload.wikimedia.org/wikipedia/pt/0/0d/EsdlaIII.jpg',
                                                           'https://www.youtube.com/watch?v=r5X-hFf6Bwo')

fight_club = media.Movie('Fight Club',
                         'An insomniac office worker and a devil-may-care soap maker form an underground fight club',
                         'https://upload.wikimedia.org/wikipedia/pt/2/2b/FightClubPoster.jpg',
                         'https://www.youtube.com/watch?v=qtRKdVHc-cE')

the_matrix = media.Movie('The Matrix',
                         'A beautiful stranger leads computer hacker Neo to a forbidding underworld',
                         'https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg',
                         'https://www.youtube.com/watch?v=vKQi3bBA1y8')

movies = [pulp_fiction, joker, interstellar, the_lord_of_the_rings_the_return_of_the_king, fight_club, the_matrix]
fresh_tomatoes.open_movies_page(movies)


