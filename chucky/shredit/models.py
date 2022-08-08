
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Shredit(models.Model):
    SIZE_TYPE = (
        ("KB", "KB"),
        ("MB", "MB")
    )

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users_file')
    _file_name = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    _file_size = models.PositiveSmallIntegerField(default=0)
    _file_url = models.URLField()
    size_type = models.CharField(
        max_length=3, choices=SIZE_TYPE, blank=False, null=False)
    chunk_num = models.PositiveSmallIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-updated',)
        # verbose_plural_name = 'Shredit'

    @property
    def file_name(self):
        pass

    @property
    def file_size(self):
        pass

    @property
    def file_url(self):
        pass
