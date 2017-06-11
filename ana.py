#!/usr/bin/env python2
import psycopg2
import sys
db = "news"


def create_view():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        conn = psycopg2.connect("dbname={} user=vagrant".format(db))
        cur = conn.cursor()
        cur.execute("create or replace view nemo as select\
        count(path) as num from log group by status;")
        conn.close()
    except psycopg2.Error as e:
        print "Unable to connect to database"
        sys.exit(1)
        raise e


def Most_Viewed():
    try:
        conn = psycopg2.connect("dbname={} user=vagrant".format(db))
        cur = conn.cursor()
        cur.execute("select path ,count(*) as num from log group by path order \
            by num DESC limit 3 offset 1;")
        rows = cur.fetchall()
        for row in rows:
            nemo = row[0].replace("/article/", "\"")
            print "%s ---- %s  views" % (nemo + "\"", row[1])
        conn.close()
    except psycopg2.Error as e:
        print "Unable to connect to database"
        sys.exit(1)
        raise e


def Most_authors():
    try:
        conn = psycopg2.connect("dbname={} user=vagrant".format(db))
        cur = conn.cursor()
        cur.execute("select author,count(log.path) as num from articles, \
            log where articles.slug=substring(path from 10 for 100) group\
            by author order by num DESC limit 4")
        rows = cur.fetchall()
        cur.execute("select name from authors")
        name = cur.fetchall()
        for row in rows:
            print "\"%s\"  %s -- views" % (name[row[0] - 1][0], row[1])
        conn.close()
    except psycopg2.Error as e:
        print "Unable to connect to database"
        sys.exit(1)
        raise e


def Most_error():
    try:
        conn = psycopg2.connect("dbname={} user=vagrant".format(db))
        cur = conn.cursor()
        cur.execute("SELECT  to_char(time, 'Mon DD, YYYY') as date, count(status) \
                        AS errors, status FROM log  WHERE status !='200 OK' \
                        GROUP BY date , status ORDER BY date ASC;")
        rows = cur.fetchall()
        cur.execute("select * from nemo;")
        total = cur.fetchall()
        totals = total[0][0]
        # print(total[0][0])
        for i in rows:
            deya = float(i[1] * 100)/long(totals)
            deya = round(deya, 2)
            if deya >= 5:
                print "AT {} {}% --errors".format(i[0], deya)
        conn.close()
    except psycopg2.Error as e:
        print "Unable to connect to database"
        sys.exit(1)
        raise e

if __name__ == "__main__":
    create_view()
    Most_Viewed()
    Most_authors()
Most_error()