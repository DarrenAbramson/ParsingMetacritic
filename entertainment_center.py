import media
import fresh_tomatoes

print("Movies' metascores are printed as they are extracted from the web. Movies are then sorted before being displayed.")


blade_runner = media.Movie("Blade Runner",
                           "Combines a lack of directorial control with voice overs.",
                           "http://www.thebestlittlefilmhouse.com/ekmps/shops/tblfh01/images/blade-runner-1982-original-us-one-sheet-film-poster-linen-backed-and-ready-to-frame-ridley-scott.-with-harrison-ford--9943-p.jpg",
                           "https://www.youtube.com/watch?v=KPcZHjKJBnE")

m_2001 = media.Movie("2001: A Space Odyssey",
                   "What happens when the computer takes over.",
                   "https://d12vb6dvkz909q.cloudfront.net/uploads/galleries/23552/2001-poster.jpg",
                   "https://www.youtube.com/watch?v=N6ywMnbef6Y")

repo_man = media.Movie("Repo Man",
                       "Life's what you make it.",
                       "http://d12vb6dvkz909q.cloudfront.net/uploads/galleries/29209/repo-man.jpg",
                       "https://www.youtube.com/watch?v=DLGrXGEMOSo")

prometheus = media.Movie("Prometheus",
                         "Imagine if people were cattle.",
                         "http://static.comicvine.com/uploads/original/1/15659/4073325-prometheus-2012-movie_poster.jpg",
                         "https://www.youtube.com/watch?v=sftuxbvGwiU")

the_fountain = media.Movie("The Fountain",
                           "Philosophy, done by movie.",
                           "http://thepulppress.com/wp-content/uploads/2015/01/Poster-The-Fountain.jpg",
                           "https://www.youtube.com/watch?v=dAuxryJ6pv8")

groundhog_day= media.Movie("Groundhog Day",
                           "This was great long before the Bill Murray bandwagon.",
                           "https://www.movieposter.com/posters/archive/main/13/MPW-6738",
                           "https://www.youtube.com/watch?v=tSVeDx9fk60")

uhf = media.Movie("UHF",
                  "This was great long before the Weird Al bandwagon. Wait, is there one?",
                  "http://www.circlecinema.com/wp-content/uploads/2013/08/936full-uhf-poster.jpg",
                  "https://www.youtube.com/watch?v=tIJ6utj-DcU")




movies = [blade_runner, m_2001, repo_man, prometheus, the_fountain, groundhog_day, uhf]


# Sort movies in list from best to worst reviewed.
movies.sort(key = lambda x: x.metascore, reverse = True)

fresh_tomatoes.open_movies_page(movies)
