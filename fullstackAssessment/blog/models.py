from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index


@register_snippet
class Author(models.Model):
    """
    Author snippet for blog posts.
    """
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, help_text="Short biography")
    photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('bio'),
        FieldPanel('photo'),
    ]
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['name']


class BlogIndexPage(Page):
    """
    Index page for blog posts. Lists all blog posts.
    """
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)
        # Get all live blog posts, ordered by publish date (newest first)
        blog_posts = BlogPage.objects.live().public().descendant_of(self).order_by('-publish_date')
        context['blog_posts'] = blog_posts
        return context
    
    # Limit to only one instance
    max_count = 1
    
    # Only allow BlogPage as children
    subpage_types = ['blog.BlogPage']


class BlogPage(Page):
    """
    A single blog post.
    """
    publish_date = models.DateField("Post date")
    intro = models.CharField(
        max_length=250,
        help_text="Brief introduction shown in listings"
    )
    body = RichTextField()
    author = models.ForeignKey(
        'blog.Author',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='blog_posts'
    )
    featured = models.BooleanField(
        default=False,
        help_text="Feature this post on the homepage"
    )
    
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel('publish_date'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('author'),
        FieldPanel('featured'),
    ]
    
    # Only allow BlogPage to be created under BlogIndexPage
    parent_page_types = ['blog.BlogIndexPage']
    
    # No children allowed
    subpage_types = []
    
    class Meta:
        ordering = ['-publish_date']