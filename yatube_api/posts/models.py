"""Posts models configuration"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        _('Название'),
        max_length=200,
        help_text=_('Дайте короткое название группе')
    )
    slug = models.SlugField(
        _('Короткая метка'),
        max_length=50,
        unique=True,
        help_text=_('Укажите адрес для страницы задачи. Используйте только '
                    'латиницу, цифры, дефисы и знаки подчёркивания')
    )
    description = models.TextField(
        _('Описание'),
        help_text=_('Опишите суть группы')
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Группа')
        verbose_name_plural = _('Группы')


class Post(models.Model):
    text = models.TextField(
        _('Текст'),
        help_text=_('Текст поста')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name=_('Автор'),
        help_text=_('Автор, к которому будет относиться пост')
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name=_('Группа'),
        help_text=_('Группа, к которой будет относиться пост'),
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name=_('Картинка'),
        upload_to='posts/',
        blank=True,
        null=True
    )
    pub_date = models.DateTimeField(
        _('Дата создания'),
        auto_now_add=True,
        help_text=_('Дата создания будет автоматически установлена '
                    'в текущую дату при создании')
    )

    class Meta():
        ordering = ('pub_date',)
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return '{:.10} {} {} {}'.format(
            self.text,
            self.pub_date,
            self.author.get_username(),
            self.group,
        )


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Пост'),
        help_text=_('Пост, к которому будет относиться комментарий')
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('Автор'),
        help_text=_('Автор, к которому будет относиться комментарий')
    )
    text = models.TextField(
        _('Текст'),
        help_text=_('Текст комментария')
    )
    created = models.DateTimeField(
        _('Дата создания'),
        auto_now_add=True,
        help_text=_('Дата создания будет автоматически установлена '
                    'в текущую дату при создании')
    )

    class Meta():
        ordering = ('-created',)
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')

    def __str__(self):
        return '{:.15}'.format(self.text)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name=_('Подписчик'),
        help_text=_('Пользователь, который подписывается'),
        blank=True,
        null=True
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name=_('Автор'),
        help_text=_('Пользователь, на которого подписываются'),
    )

    class Meta:
        verbose_name = _('Подписка')
        verbose_name_plural = _('Подписки')
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='unique_relationships'),
            models.CheckConstraint(check=~models.Q(user=models.F("following")),
                                   name="prevent_self_follow"),
        ]

    def __str__(self):
        return '{} followed {}'.format(
            self.user.get_username(),
            self.following.get_username()
        )
