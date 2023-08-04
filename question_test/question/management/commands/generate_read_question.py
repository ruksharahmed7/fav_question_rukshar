# myapp/management/commands/populate_favorite_questions.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from question.models import ReadQuestion, Question

# python manage.py generate_read_question <no. of FReadQuestion instances to generate>

class Command(BaseCommand):
    help = 'Populates the database with instances of the ReadQuestion model.'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of ReadQuestion instances to be created.')

    def handle(self, *args, **kwargs):
        fake = Faker()
        total = kwargs['total']

        # Get all the users and questions from the database
        users = User.objects.all()
        questions = Question.objects.all()

        for _ in range(total):
            # Choose a random user and question from the lists
            user = fake.random_element(elements=users)
            question = fake.random_element(elements=questions)

            # Create and save the ReadQuestion instance to the database
            ReadQuestion.objects.create(user=user, question=question)
