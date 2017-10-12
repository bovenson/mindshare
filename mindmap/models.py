from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

User.add_to_class('nickname', models.CharField(max_length=200, null=True, default="#"))


class Category(models.Model):
    """分类"""
    title = models.CharField('标题', max_length=30)
    parent = models.ForeignKey('Category', null=True, blank=True)

    def __str__(self):
        return self.title

    def convert_to_dict(self):
        _res = {
            'id': self.id,
            'title': self.title,
            'parent': self.parent.id if self.parent else ''
        }
        return _res


class Tag(models.Model):
    """标签"""
    title = models.CharField('标题', max_length=30)
    cnt = models.IntegerField('属于该标签记录数量', default=0)

    def __str__(self):
        return self.title


class MindMap(models.Model):
    """思维导图"""
    title = models.CharField('标题', max_length=50)
    description = models.CharField('描述', max_length=1000, blank=True)
    img = models.ImageField('图片', upload_to='img/%Y/%m/%d/', blank=True, null=True)
    mindmap = models.FileField('思维导图文件', upload_to='file/%Y/%m/%d/', blank=True, null=True)
    public = models.BooleanField('是否公开', default=True)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, null=True, blank=True)
    author = models.ForeignKey(User, null=True, default=1)
    share = models.URLField('分享地址', max_length=300, null=True, blank=True)

    vote = models.IntegerField('投票', default=0)
    visit = models.IntegerField('浏览', default=0)
    create_date = models.DateTimeField('创建时间', default=timezone.now, null=True)
    update_date = models.DateTimeField(verbose_name='最后更新时间', auto_now=True)

    def __str__(self):
        return self.title


class MindMapVote(models.Model):
    """思维导图投票"""
    mindmap = models.ForeignKey(MindMap)
    author = models.ForeignKey(User)

    def __str__(self):
        return str(self.mindmap.title)


class FeedbackMessage(models.Model):
    """反馈"""
    content = models.TextField('内容', max_length=2000)
    create_date = models.DateTimeField('创建时间', default=timezone.now, null=True)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.concrete_model[:30]


class Article(models.Model):
    """文章"""
    title = models.CharField("标题", max_length=200, blank=True, null=True)
    content = models.TextField("内容", max_length=10000, blank=True)
    create_date = models.DateTimeField('创建时间', default=timezone.now, null=True)

    def __str__(self):
        return self.title

