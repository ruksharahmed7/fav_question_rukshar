# fav_question_rukshar

## [Views](https://github.com/ruksharahmed7/fav_question_rukshar/blob/main/question_test/question/views.py)

- A view(**user_question_counts**) that provides a count of total favorite questions and read questions per user, paginated to 100 users per page. Clicking on the usernames will lead to the userprofile view.

- Userprofile view(**user_profile**) lists read, unread, favorite, and unfavorite questions. One can filter questions by read, unread, favorite, and unfavorite status.

## Data Generation

- Four scripts are written to generate users, questions, favorite questions, and read questions data. They are in the [management](https://github.com/ruksharahmed7/fav_question_rukshar/tree/main/question_test/question/management/commands) folder. 

- To run a data generation script, the CLI command is 
```
python manage.py generate_users 100
``` 
- The above command will generate 100 random user instances for the database 

## Unit Tests
- [tests.py](https://github.com/ruksharahmed7/fav_question_rukshar/blob/main/question_test/question/tests.py) script has unit tests for the previously mentioned 2 API views

- For unit testing each view, random test data is generated using the *setUp* method. 

- For **user_question_counts** view, we conduct the following tests:
    - Whether the url response status code is 200(indicating success)
    - Pagination testing: if a particular page loads the intended order of users.
    - If a page loads the correct number of favorite and read questions

- For **user_profile** view, we conduct the following tests:
    - Whether the url response status code is 200(indicating success)
    - Whether the page loads the info. of the correct user
    - Whether the response contains the correct list of favorite/read/unread/unfovorite questions of the user with proper pagination

- The CLI command for conducting test script:
```
python manage.py test
``` 

## Environment

- Python 3.9
- Additional library: [faker](https://faker.readthedocs.io/en/master/) 

## Containerization

- To dockerize the Django app, I created a [Dockerfile](https://github.com/ruksharahmed7/fav_question_rukshar/blob/main/question_test/Dockerfile) that defines the environment and configuration for running the Django application inside a Docker container. Additionally, I created a [docker-compose.yml](https://github.com/ruksharahmed7/fav_question_rukshar/blob/main/question_test/docker-compose.yml) file to manage the entire application stack.

-  To build and run the Docker containers, open a terminal in the django project root and run the following commands:

```
docker-compose build  # Build the Docker image for your Django app
docker-compose up     # Run the Django app and database in containers
```