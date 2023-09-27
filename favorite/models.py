from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from accounts.models import User

# from platforms.models import Platform



class Favorite(models.Model):
    """
        Объект описывающий сущность избранного чего либо.
    """
    created_at = models.DateTimeField(auto_now_add=True)

    # Согласно документации, создаём поля для хранения ContentType и object_id
    # https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/#django.contrib.contenttypes.fields.GenericForeignKey
    # https: // habr.com / ru / articles / 723300 /
    tag_relationship = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.RESTRICT)
    object_id = models.BigIntegerField()
    # Создаём генерируемый внешний ключ, который может быть связан с продуктами разных типов: решения и платформы
    content_object = GenericForeignKey("content_type", "object_id")
    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'object_id', 'content_type'],
                name='unique_user_content_type_object_id'
            )
        ]
    def __str__(self):
        return f'{self.object_id}'


