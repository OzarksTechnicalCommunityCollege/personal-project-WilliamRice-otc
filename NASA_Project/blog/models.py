from django.conf import settings
from django.db import models
from django.utils import timezone

# I'm unsure what models I'll need yet

class Post(models.Model):

    # Defines possible statuses for ensuring unfinished posts aren't published
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # Article title
    article_title = models.CharField(max_length = 75)

    # Update Post title
    post_title = models.CharField(max_length = 75)

    # Slug for url amendment to take users to specific post
    slug = models.SlugField(max_length = 75)

    # Allows Authors of posts to be recognized
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # If author is deleted, posts stay, in documentation link on page 20 of book
        on_delete=models.SET_NULL,
        # Allows author value to be empty, in documentation link on page 20 of book
        null=True,
        # Allows form to accept empty values, in documentation link on page 20 of book
        blank=True,
        # Allows searching for authors posts
        related_name = 'blog_posts'
    )

    # Content of post
    body = models.TextField()

    # Timestamp for post publication
    publish = models.DateTimeField(default=timezone.now)

    # Tracking of original creation date, for others use in reference materials
    created = models.DateTimeField(auto_now_add = True)

    # Data recency stamp so users know the last time the data was validated
    updated = models.DateTimeField(auto_now = True)

    # Limits value to those within the Status class, and assigns a default of draft requiring committal to post
    status = models.CharField(
        max_length = 2,
        choices = Status,
        default = Status.DRAFT
    )
    # for displaying posts on page in ascending order, oldest first
    class Meta:
        ordering = ['publish']
        indexes = [
            models.Index(fields = ['publish']),
        ]


    def __str__(self):
        return self.article_title

