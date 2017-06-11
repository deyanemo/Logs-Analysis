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
    ~> vagrant up
    ~>ssh 127.0.0.1 2222
    username : vagrant
    password : vagrant

    after signing in :
    install PostgersSQl:            [ sudo apt-get install postgres ]
    Run psql and install db:        [ psql -d news -f sqlfile.sql ]

Now wait till finish
and you are ready to go :)

Files:
    - deyanemo.py
    - README.md



NOTE :

ADD THE VIEW INSIDE THE CODE AS FUNCTION BUT HERE ITS

create or replace view nemo as select status count(path) as num from log group by status;

**** Note ADDED THE VIEW INTO THE CODE ****