import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Questions


class QuestionsModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_questions = Questions(published_on=time)
        self.assertIs(future_questions.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Questions(published_on=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Questions(published_on=time)
        self.assertIs(recent_question.was_published_recently(), True)
