# Parsing Metacritic

The result of using these files to generate html can be found at [darrenabramson.github.io/ParsingMetacritic/fresh_tomatoes.html](http://darrenabramson.github.io/ParsingMetacritic/fresh_tomatoes.html)

To use these files, simply run ``entertainment_center.py``. You will see new functionality at the command line, and in the resulting html page. While processing, the metascore and title of each movie is printed to the terminal to show successful parsing for each movie. 

This directory contains 4 files. The only new file is ``python
getmetascore.py``, although all of the others have been changed. Here are the most significant changes.

##``fresh_tomatoes.py``

The definition of the ``content`` field in the ``create_movie_tiles`` function is expanded to allow for metacritic score and brief description (according to me) of the plot.

##``entertainment_center.py``

The movies are sorted by their metascore before ``fresh_tomatoes.open_movies_page`` is called.


##``media.py``

The class initializer now calls ``getmetascore.getscore`` and intializes the field to its value. 

##``getmetascore.py``

There is no publicly available API for retrieving metascores for movies from [Metacritic](http://www.metacritic.com). 

A shameful company is offering unofficial APIs but requires a credit card for even low volume, noncommercial use. So I rolled my own. It looks for the ``ratingValue`` tag in the html of the appropriately formatted URL, and extracts the score as a string.

Movies without metascores, such as the excellent [Krush Groove](https://www.youtube.com/watch?v=uhx60w2_51Y), [had to be omitted](http://www.metacritic.com/search/all/krush%20groove/results).




