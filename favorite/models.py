from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from config import settings


class FavoritePlatforms(models.Model):
    """
        Объект описывающий сущность избранного чего либо.
    """
    created_at = models.DateTimeField(auto_now_add=True)

    # Согласно документации, создаём поля для хранения ContentType и object_id
    # https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey
    # https: // habr.com / ru / articles / 723300 /
    tag_relationship = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT)
    object_id = models.BigIntegerField()
    # Создаём генерируемый внешний ключ, который может быть связан с продуктами разных типов: решения и платформы
    content_object = GenericForeignKey("content_type", "object_id")
    class Meta:
        verbose_name = 'favorite'
        verbose_name_plural = 'favorites'

        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'object_id', 'content_type'],
                name='unique_user_content_type_object_id'
            )
        ]
    def __str__(self):
        return f'{self.object_id}'


class FavoriteSolutions(models.Model):
    """
        Объект описывающий сущность избранного чего либо.
    """
    created_at = models.DateTimeField(auto_now_add=True)

    # Согласно документации, создаём поля для хранения ContentType и object_id
    # https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey
    # https: // habr.com / ru / articles / 723300 /
    tag_relationship = models.SlugField(null=True, blank=True)# можно удалить
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT)
    object_id = models.BigIntegerField()
    # Создаём генерируемый внешний ключ, который может быть связан с продуктами разных типов: решения и платформы
    content_object = GenericForeignKey("content_type", "object_id")
    class Meta:
        verbose_name = 'favorite'
        verbose_name_plural = 'favorites'

        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'object_id', 'content_type'],
                name='unique_user_content_type_object_id_solutions'
            )
        ]
    def __str__(self):
        return f'{self.object_id}'


