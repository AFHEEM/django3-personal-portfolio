from django.db import models


class Blog(models.Model):
    """
    Blog class - used to create each blog
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        """
        Get object details from the model
        :return:
        """
        return self.title
