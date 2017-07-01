Log Analysis
=========================== 

### Project Description
> In this project, you'll work with data that could have come from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

### Requirements
- Python
- Vagrant
- VirtualBox

### Running the project
- Install vagrant and virtualbox
- Clone [Full Stack Repo](https://github.com/udacity/fullstack-nanodegree-vm)
- Go to vagrant sub-directory in [Full Stack Repo](https://github.com/udacity/fullstack-nanodegree-vm) using command:
```
$ cd fullstack-nanodegree-vm\vagrant
```
- Unzip [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) here.
- Lauch the vagrant vm using command : **(It may take a while for first time)**
```
$ vagrant up
```
- Log in to vm using command:
```
$ vagrant ssh
```
- Dowload/Clone the files from this [repo](https://github.com/rishabmps/Log-analysis).
- Setup the database in vm using command:
```
$ psql -d news -f newsdata.sql
```
- Connect to database in vm using command:
```
$ psql -d news
```
- To execute queries, run this command in vm: 
```
$ cd Log Analysis 
$ python report.py
```