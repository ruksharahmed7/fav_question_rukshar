# tests.py

from django.test import TestCase, Client
from django.urls import reverse
import random
from django.contrib.auth.models import User
from .models import FavoriteQuestion, ReadQuestion, Question

class UserQuestionCountsViewTestCase(TestCase):

    def setUp(self):
        # Create some users and related data for testing
        print('Creating Users...')
        self.users = []
        for i in range(300):
            tmp_user = User.objects.create_user(username='user'+str(i), password='testpassword')
            self.users.append(tmp_user)
        
        # Create some questions
        print('Creating Questions...')
        self.questions = []
        for i in range(300):
            tmp_question = Question.objects.create( option1='Option 1', option2='Option 2', option3='Option 3',option4='Option 4', option5='Option 5', answer='Option 1', explain='Explanation for Question 1')
            self.questions.append(tmp_question)
        
        #create some favorite/read questions by randomly picking up users and questions
        print('Creating Fav and Read Questions...')
        self.fav_questions = []
        self.read_questions = []
        for i in range(300):
            tmp_user = random.choice(self.users)
            tmp_question = random.choice(self.questions)
            tmp_fav_question = FavoriteQuestion.objects.create(user=tmp_user, question =tmp_question)
            tmp_read_question = ReadQuestion.objects.create(user=tmp_user, question =tmp_question)
            self.fav_questions.append(tmp_fav_question); self.read_questions.append(tmp_read_question)

        

    def test_user_question_counts_view(self):
        client = Client()
        url = reverse('user_question_counts')
        response = client.get(url)

        # Test that the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

        # Test that pagination works as expected
        url = f"{reverse('user_question_counts')}?page=2"
        response = client.get(url)

        #print(response.context)
        # Test that the response contains the correct list of users for the selected page
        expected_users = User.objects.all()[100:200]
        self.assertEqual(list(response.context['page_obj']), list(expected_users))


        #Test if the count of favorite and read questions is correct for each user
        #We conduct the test on the first 20 users for the page 2
        
        #get a list of dictionary that includes user, count of favorite/read questions from the page response
        user_counts = response.context['user_counts']
        user_counts2 = []
        for i in range(20): #count favorite/read questions for the first 20 users of page 2 
            favorite_count = FavoriteQuestion.objects.filter(user=expected_users[i]).count()
            read_count = ReadQuestion.objects.filter(user=expected_users[i]).count()
            user_counts2.append({'user': expected_users[i], 'favorite_count': favorite_count, 'read_count': read_count})

        self.assertEqual(user_counts[:20], user_counts2)


class UserProfileViewTestCase(TestCase):

    def setUp(self):
        # Create some users and related data for testing
        self.user1 = User.objects.create_user(username='user1', password='testpassword')

        # Create some questions
        print('Creating Questions...')
        self.questions = []
        for i in range(300):
            tmp_question = Question.objects.create( option1='Option 1', option2='Option 2', option3='Option 3',option4='Option 4', option5='Option 5', answer='Option 1', explain='Explanation for Question 1')
            self.questions.append(tmp_question)
        
        #create some favorite/read questions by randomly picking up users and questions
        print('Creating Fav and Read Questions...')
        self.fav_questions = []
        self.read_questions = []
        for i in range(150):
            tmp_fav_question = FavoriteQuestion.objects.create(user=self.user1, question =self.questions[i])
            tmp_read_question = ReadQuestion.objects.create(user=self.user1, question =self.questions[i])
            self.fav_questions.append(tmp_fav_question); self.read_questions.append(tmp_read_question)


    def test_user_profile_view(self):
        client = Client()
        #url for favorite questions of the user
        url = f"{reverse('user_profile', kwargs={'user_id': self.user1.id})}?status=favorite"
        response = client.get(url)

        # Test that the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

        # Test that the response contains the correct user profile information
        self.assertEqual(response.context['user'], self.user1)

        # Test that the response contains the correct list of favorite questions
        # Get the first 100 favorite questions for this user
        questions_count = FavoriteQuestion.objects.filter(user=self.user1)[:100]
        self.assertEqual(list(response.context['page_obj']), list(questions_count))

        #url for read questions of the user
        url = f"{reverse('user_profile', kwargs={'user_id': self.user1.id})}?status=read&page=2"
        response = client.get(url)

        # Test that the response contains the correct list of read questions
        # Get the last 50 read questions for this user
        questions_count = ReadQuestion.objects.filter(user=self.user1)[100:]
        self.assertEqual(list(response.context['page_obj']), list(questions_count))

        #url for unread questions of the user
        url = f"{reverse('user_profile', kwargs={'user_id': self.user1.id})}?status=unread"
        response = client.get(url)

        # Test that the response contains the correct list of unread questions
        # Get the first 100 unread questions for this user
        questions_count = ReadQuestion.objects.exclude(user=self.user1)[:100]
        self.assertEqual(list(response.context['page_obj']), list(questions_count))

        #url for unfavorite questions of the user
        url = f"{reverse('user_profile', kwargs={'user_id': self.user1.id})}?status=unfavorite&page=2"
        response = client.get(url)

        # Test that the response contains the correct list of unfavorite questions
        # Get the first 100 unread questions for this user
        questions_count = FavoriteQuestion.objects.exclude(user=self.user1)[100:]
        self.assertEqual(list(response.context['page_obj']), list(questions_count))

       

