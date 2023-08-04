# myapp/management/commands/populate_users.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker

# python manage.py generate_users <no. of user instances to generate>

class Command(BaseCommand):
    help = 'Populates the database with instances of the Django User model.'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of User instances to be created.')

    def handle(self, *args, **kwargs):
        fake = Faker()
        total = kwargs['total']

        #existing_usernames = set(User.objects.values_list('username', flat=True))

        suffix = 400
        for _ in range(total):
            # Generate fake data using Faker

            #Faker can't generate unique username all the time
            username = 'aaabbbrrraaarrr' + str(suffix); suffix += 1 
            #print(username)
            
            # while not username or username in existing_usernames:
            #     username = fake.user_name()

            email = fake.email()
            password = fake.password(length=12)  # You can adjust the password length if needed
            first_name = fake.first_name()
            last_name = fake.last_name()

            # Create and save the User instance to the database
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            #existing_usernames.add(username)  # Update the set of existing usernames
