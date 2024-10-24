from django.db import models

class BlackAndWhiteImage(models.Model):
    original_image = models.ImageField(upload_to='original/')
    bw_image = models.ImageField(upload_to='bw/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"