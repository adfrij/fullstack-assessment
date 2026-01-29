from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField


# TODO 1: Create a Question snippet
# - Fields: question_text (TextField), answer_text (RichTextField), 
#   difficulty (CharField with choices: Easy, Medium, Hard), tags (CharField, optional)
# - Register as a snippet
# - Add appropriate panels for admin


class StudyGuideIndexPage(Page):
    """
    Landing page for the study guide. Lists all topics.
    """
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    # TODO 2: Override get_context to pass child TopicPage items to the template


class TopicPage(Page):
    """
    A page representing a topic (e.g., "System Design", "Python Basics").
    Contains multiple questions.
    """
    description = RichTextField(blank=True)
    difficulty_level = models.CharField(
        max_length=20,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced'),
        ],
        default='intermediate'
    )
    # TODO 3: Add a connection to the Question snippet (consider which type of relationship to use)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('difficulty_level'),
        # TODO 4: Make sure the questions are editable in the admin interface
    ]

    # TODO 5: Make sure the questions are passed to the template