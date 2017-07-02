
import psycopg2 as ps


# prints question1 result
def question_1():
    question_1 = "\n1. What are the most popular three articles of all time?\n"
    # unoptimese query
    query_1 = "select title, count(*) as views from articles join log on \
    log.path like concat('%',articles.slug,'%') where log.status = '200 OK' \
    and log.method = 'GET' group by articles.title order by views desc \
    limit 3;"
    # Optimised query
    query_optimised = "select title, count(*) as views from articles join log on \
    log.path = concat('/article/',articles.slug) where log.status = '200 OK'\
    and log.method = 'GET' group by articles.title order by views desc \
    limit 3;"
    print(question_1)
    print_resuts_views(query_optimised)


# prints question2 result
def question_2():
    question_2 = "\n2. Who are the most popular article authors of all time?\n"
    query_2 = "select authors.name,count(*) as views from authors join \
    articles on authors.id = articles.author join log on log.path = \
    concat('/article/',articles.slug) where log.status = '200 OK' and \
    log.method = 'GET' group by authors.name order by views desc;"
    print(question_2)
    print_resuts_views(query_2)


# prints question3 result
def question_3():
    question_3 = "\
    \n3. On which days did more than 1% of requests lead to an errors?\n"
    query_3 = "select date, error from ( select date(time) as date, \
    round(100.0*sum(case status when '200 OK' then 0 else 1 end)/count\
    (status),2) as error  from log group by date order by error desc) \
    as me where error >1;"
    print(question_3)
    print_resuts_error(query_3)


# Connect to default database named news
def connect_database(dbName="news"):
    try:
        db = ps.connect(database=dbName)
        c = db.cursor()
        return db, c
    except Exception as e:
        print("Cannot connect to database due to" + str(e))


# Prints the result of a query for views
def print_resuts_views(query):
    try:
        results = get_query_results(query)
        for i, result in enumerate(results):
            print(str(i + 1) + " " +
                  str(result[0]) + " ---> " + str(result[1]) + " views")
    except Exception as e:
        print(e)


# Prints the result for query for error
def print_resuts_error(query):
    results = get_query_results(query)
    for i, result in enumerate(results):
        print(str(i + 1) + " " +
              str(result[0]) + " ---> " + str(result[1]) + "% error")


# Returns the results for a query
def get_query_results(query):
    try:
        db, c = connect_database()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except Exception as e:
        print("Database error: " + str(e))


# Main function
if __name__ == '__main__':

    question_1()
    question_2()
    question_3()
