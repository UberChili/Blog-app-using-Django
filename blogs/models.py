from django.db import models

# Create your models here.


class Tag(models.Model):
    """A keyword to describe or categorize user posts."""
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    """A blog post written by the user."""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name_plural = 'posts'

    def __str__(self):
        """Return a string representation of the model, especifically the title of the post."""
        return self.title

    def short_body(self):
        """Return a string representation of the shortened body of the post"""
        if len(self.body) <= 500:
            return self.body
        else:
            return f"{self.body[:500]}..."

    def shorter_body(self):
        """Return a string representation of the shortened body of the post"""
        if len(self.body) <= 250:
            return self.body
        else:
            return f"{self.body[:250]}..."
