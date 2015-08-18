# This is a hack. The only API I could find for metacritic is run by
# Mashape.com which wants a credit card for free trial accounts.
import urllib2

def getscore(title):

    urlPrefix = "http://www.metacritic.com/movie/"

    # Metacritic movie URLs need lower case, space replaced by - 
    title = title.lower()
    title = title.replace(" ", "-")

    # This line made necessary by 2001:...
    title = title.replace(":", "")

    # urllib2 is needed because metacritic replies with 403 forbidden
    # to python requests. Meanies!
    connection = urllib2.Request(urlPrefix + title, headers ={'User-Agent':'Chrome'})
    output = urllib2.urlopen(connection).read()


    # The metascore will occur after the ratingValue string and ">
    ratingIndex = output.find("ratingValue") + 13

    # This code assumes 2 digit ratings.
    ratingString = output[ratingIndex : ratingIndex + 2] 
    print(title + ": ")
    return int(ratingString)
