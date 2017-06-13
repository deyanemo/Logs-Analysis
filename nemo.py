#!/usr/bin/env python2
from database_setup import MyDB


def most_popular():
    """ this function send a query todatabase asking for the title
         from articles the count of path from log
         then substring the path to get rid of the // and group
         and order DESC and limit the articles by 4
    """
    db = MyDB()
    rows = db.query("select title,count(path) as num from articles,log\
                     where articles.slug = substring(path from 10 for 100)\
                     group by title order by num DESC limit 3;")
    print("\n-------------~ MOST POPULAR ARTICLES ~-------------\n")
    for row in rows:
        print "\"{}\" --- {} views".format(row[0], row[1])
    print("\n-------------~~~~~~~~~~~~~~~~~~~~~~~~~-------------\n")
    db.close()


def most_authors():
    """
        Please Note Very important:
            This function exepect a view to be created before the
            execution to this code Or Just uncomment The CreateView
            Function

       this function send a query to database asking for the
       authors names and then select the number from a view
       and join them and goup them by name

    """
    db = MyDB()
    rows = db.query("select authors.name, mauthors.num from authors join mauthors \
                    on authors.id = mauthors.author group by authors.name, \
                    mauthors.num order by mauthors.num DESC")
    print("\n-------------~ MOST POPULAR AUTHORS ~-------------\n")
    for row in rows:
        print "\"{}\" --- {} views".format(row[0], row[1])
    print("\n-------------~~~~~~~~~~~~~~~~~~~~~~~~~-------------\n")
    db.close()


def error_reporting():
    """
        Please Note Very important:
            This function exepect Two views to be created before the
            execution to this code Or Just uncomment The CreateView
            Function

       this function send a query to database asking for the
            select the date from the err view and select
            the count from err and the count from ok
            and divide them then multiply them by 100 to get
            the percentage of that day error percantage
            and left outer join them
    """
    db = MyDB()
    rows = db.query("select err.date ,(err.count / ok.count::float)*100 \
                    from ok left outer join err on err.date = ok.date order\
                    by err.date ASC;")
    print("\n-------------~ ERROR REPORTING  ~-------------\n")
    for title, view in rows:
        if view >= 1:
            print "At : {} error percent is : {}% ".format(
                title, round(view, 2))
    print("\n-------------~~~~~~~~~~~~~~~~~~~~~~~~~-------------\n")
    db.close()

if __name__ == "__main__":
    # Most popular articles
    most_popular()
    # Most popular authors
    most_authors()
    # The Erro percentage
    error_reporting()
    # Closing the database
