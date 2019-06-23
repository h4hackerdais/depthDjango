from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)

    def get_post_details(self):
        return f"posts/{self.id}"

    def get_post_edit(self):
        return f"posts/{self.id}/edit"

    def get_post_delete(self):
        return f"posts/{self.id}/delete"

