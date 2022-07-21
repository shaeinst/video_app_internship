from django.db import models
from django.core.validators import FileExtensionValidator


class Video(models.Model):

    # upload file to MEDIA_ROOT/videos/uploads/2022/07/20
    upload = models.FileField(
        upload_to="uploads/videos/%Y/%m/%d/",
        validators=[FileExtensionValidator(["mp4", "mkv"])],
    )
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500, blank=True, default="")

    class Meta:
        ordering = ["created"]

    def __str__(self):
        if self.title:
            return f"{self.id} | {self.title}"
        return f"{self.id} | untitled"
