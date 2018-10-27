from django.contrib.auth.models import User
from django.db import models

class Anxiety(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="anxieties")

    fear = models.TextField(max_length=2048)
    action = models.TextField(max_length=2048)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'user_id: %d, fear: %s, action: %s' % (self.user.id, self.fear, self.action)
