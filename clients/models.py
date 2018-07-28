from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    company = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    interests = models.TextField()

    def __str__(self):
        return ''.join([
            self.name,
            self.email,
            self.company,
            self.phone,
            self.interests
        ])

