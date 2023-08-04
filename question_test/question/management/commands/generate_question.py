# myapp/management/commands/populate_questions.py

from django.core.management.base import BaseCommand
from faker import Faker
from question.models import Question

# python manage.py generate_question <no. of question instances to generate>

class Command(BaseCommand):
    help = 'Populates the database with instances of the Question model.'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of Question instances to be created.')

    def handle(self, *args, **kwargs):
        fake = Faker()
        total = kwargs['total']

        for _ in range(total):
            # Generate fake data using Faker
            question_text = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            option1 = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
            option2 = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
            option3 = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
            option4 = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
            option5 = fake.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None)
            answer = fake.random_element(elements=(option1, option2, option3, option4, option5 ))
            explain = fake.paragraph(nb_sentences=3, variable_nb_sentences=True, ext_word_list=None)

            # Create and save the Question instance to the database
            Question.objects.create(
                question=question_text,
                option1=option1,
                option2=option2,
                option3=option3,
                option4=option4,
                option5=option5,
                answer=answer,
                explain=explain
            )
