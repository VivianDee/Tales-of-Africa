from django.db import models
from uuid import uuid4
# Create your models here.


class Story(models.Model):i
    '''
        This  is the Story model.It has everything a story needs

        Arg:
            id(UUID4) : story Id
            title(str): story title
            description(text) : story description
            content(text) : story
    '''
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()

    def __str__(self):
        return f"id: {self.id}, title: {self.title}, description: {self.description}"
