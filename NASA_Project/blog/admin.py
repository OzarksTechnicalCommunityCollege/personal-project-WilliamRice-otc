from django.contrib import admin
from .models import Post
@admin.register(Post)

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    # Displays these items in the admin menu for user identification
    list_display = ['article_title', 'slug', 'publish', 'status']
    
    # Allows filtering by these fields in admin menu
    list_filter = ['status','created','publish', 'author']
    
    # Enables value search for these fields
    search_fields = ['article_title','body']

    # Creates url slug based on title
    prepopulated_fields = {'slug': ('article_title',)}

    # Changes author field on add/change post page to search bar rather than dropdown list of all options
    raw_id_fields = ['author']

    # organize by publish date
    date_hierarchy = 'publish'

    # Sets default ordering based on status, then published values
    ordering = ['status', 'publish']

    # enables count display next to sorting fields for number of returns matching criteria
    show_facets = admin.ShowFacets.ALWAYS
