#!/usr/bin/env python2
from database_setup import MyDB

db = MyDB()


def Most_popular():
    """ this function send a query todatabase asking for the title
         from articles the count of path from log
         then substring the path to get rid of the // and group
         and order DESC and limit the articles by 4
    """
    rows = db.query("select title,count(path) as num from articles,log\
                     where articles.slug = substring(path from 10 for 100)\
                     group by title order by num DESC limit 4;")
    print("\n-------------~ MOST POPULAR ARTICLES ~-------------\n")
    for row in rows:
        print "\"{}\" --- {} views".format(row[0], row[1])
    print("\n-------------~~~~~~~~~~~~~~~~~~~~~~~~~-------------\n")


def Most_autors():
    """
        Please Note Very important:
            This function exepect a view to be created before the
            execution to this code Or Just uncomment The CreateView
            Function

       this function send a query to database asking for the
       authors names and then select the number from a view
       and join them and goup them by name

    """
    rows = db.query("select authors.name, mautors.num from authors join mautors \
                    on authors.id = mautors.author group by authors.name, \
                    mautors.num order by mautors.num DESC")
    print("\n-------------~ MOST POPULAR AUTHORS ~-------------\n")
    for row in rows:
        print "\"{}\" --- {} views".format(row[0], row[1])
    print("\n-------------~~~~~~~~~~~~~~~~~~~~~~~~~-------------\n")


def Error_date():
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
    rows = db.query("select err.date ,(err.count / ok.count::float)*100 \
                    from ok left outer join err on err.date = ok.date order\
                    by err.date ASC;")
    print("\n-------------~ ERROR REPORTING  ~-------------\n")
    for row in rows:
        if row[1] >= 1:
            print "At : {} error percent is : {}% ".format(
                row[0], round(row[1]), 2)
    print("\n-------------~~~~~~~~~~~~~~~~~~~~~~~~~-------------\n")


# def CreateView():
#     """
#         Please Note Very important:
#             This function exepect Two views to be created before the
#             execution to this code Or Just uncomment The CreateView
#             Function
#         This function create the view for you !
#     """
#     # The mauthors View
#     try:
#         db._db_cur.execute("create or replace view mautors as select author,count(log.path) \
#                 as num from articles, log where articles.slug= \
#                 substring(path from 10 for 100) group by author order\
#                 by num DESC")
#     # The error Count View
#         db._db_cur.execute("create or replace view ok as select to_char(time,'Mon DD, YYYY') \
#                 as date , count(status) from log where status!='200 OK'\
#                 group by date order by date ASC;")
#     # The Ok View
#         db._db_cur.execute("create or replace view ok as select to_char(time,'Mon DD, YYYY') \
#                 as date , count(status) from log where status='200 OK'\
#                 group by date order by date ASC;")
#     except psycopg2.Error as e:
#         raise e
#     print ("Views Created!")

if __name__ == "__main__":
    # Creating the view
#     CreateView()
    # Most popular articles
    Most_popular()
    # Most popular authors
    Most_autors()
    # The Erro percentage
    Error_date()
    # Closing the database
    db.close()
