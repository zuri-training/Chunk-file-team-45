
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
    chucked_file = models.FileField(upload_to='zipped/%Y/%m/%d/')
    _file_size = models.PositiveSmallIntegerField(default=0)
    _file_url = models.URLField()
    size_type = models.CharField(
        max_length=3, choices=SIZE_TYPE, blank=False, null=False)
    chunk_num = models.PositiveSmallIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name_plural = 'Shredit'

    def __str__(self):
        return self._file_name

    @property
    def file_name(self):
        name = self._file_name.split('.')[0].upper()
        extension = self._file_name.split('.')[1]
        return f'{name}-(.{extension})'

    @property
    def file_size(self):
        _size = self.chucked_file.size
        if self.size_type == 'KB':
            size = _size / 1024
        if self.size_type == 'MB':
            size = _size / (1024 * 1024)

        self._file_size = size
        self.save()
        return size

    @property
    def file_url(self):
        pass
