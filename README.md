Logs-Analysis :
a project for Full Stack developer nano degere
for reporting logs stored into a database

Why we report anyway ?
We report to get the summary from the logs , to get a more information
about whats going on on our site , what type of errors or what type of
articles that the visiters admires...etc


Requirements
- Python 2.X (2.7 is expected)
- PostgerSql latest version
- Vagrang and VirtualBox
- and the SQLEXAMPLEFILE (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


Installation :
this will not provide tips to install vagrant and virtualbox
    after starting the Vagrant and Virtualbox
    open cmd as administrator(*) and type :
    vagrant up
    ssh 127.0.0.1 2222
    username : vagrant
    password : vagrant

    after signing in :
    - install PostgersSQl:            [ sudo apt-get install postgres ]
    - Run psql and install db:        [ psql -d news -f newsdata.sql ]
    Please Note before running the script please create the views in order to the program to run

    For creating the author view to answer question 2:

            create or replace view mauthors as select author,count(log.path)
                as num from articles, log where articles.slug=
                substring(path from 10 for 100) group by author order
                by num DESC

    For creatin error view answering question 3:

            create or replace view err as select to_char(time,'Mon DD, YYYY')
                as date , count(status) from log where status!='200 OK'
                group by date order by date ASC;

            create or replace view ok as select to_char(time,'Mon DD, YYYY')
                as date , count(status) from log
                group by date order by date ASC;

    - Run Script using :              [python nemo.py]

Files:
    - database_setup.py *
    - nemo.py *
    - README.md


NOTE :
Thank you

