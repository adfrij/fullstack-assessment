from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    """
    The home page of the site.
    """
    hero_title = models.CharField(
        max_length=255,
        default="Master Technical Interviews",
        help_text="Main headline on the homepage"
    )
    hero_subtitle = RichTextField(
        blank=True,
        default="<p>Prepare for your next software engineering interview with our comprehensive study guides and expert insights.</p>",
        help_text="Subtitle text below the main headline"
    )
    
    # CTA buttons
    cta_primary_text = models.CharField(
        max_length=50,
        default="Browse Study Guide",
        help_text="Text for the primary call-to-action button"
    )
    cta_primary_link = models.CharField(
        max_length=255,
        default="/study-guide/",
        help_text="Link for the primary CTA button"
    )
    
    cta_secondary_text = models.CharField(
        max_length=50,
        default="Read Our Blog",
        help_text="Text for the secondary call-to-action button"
    )
    cta_secondary_link = models.CharField(
        max_length=255,
        default="/blog/",
        help_text="Link for the secondary CTA button"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('cta_primary_text'),
        FieldPanel('cta_primary_link'),
        FieldPanel('cta_secondary_text'),
        FieldPanel('cta_secondary_link'),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        
        # Get latest 3 blog posts
        from blog.models import BlogPage
        latest_posts = BlogPage.objects.live().public().order_by('-publish_date')[:3]
        context['latest_posts'] = latest_posts
        
        # Get latest 3 study topics
        from study_guide.models import TopicPage
        latest_topics = TopicPage.objects.live().public().order_by('-first_published_at')[:3]
        context['latest_topics'] = latest_topics
        
        return context
    
    # Limit to only one instance
    max_count = 1