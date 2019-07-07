from django.conf import settings
from django.db import models
import datetime
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    pass

class Ceo(models.Model):
    ITEM_FIELDS_SELECT=(
        ('기술분야','기술분야'),
        ('BM분야','BM분야'),
    )
    WORK_FIELDS_SELECT=(
        ('제조업','제조업'),
        ('서비스업','서비스업'),
    )
    SETUP_FIELDS_SELECT=(
        ('기창업','기창업'),
        ('창업','창업'),
    )
    YEARS=(
        (2019, 2019),
        (2020, 2020),
        (2021, 2021),
    )
    ceoname = models.CharField(max_length=30, blank=False)
    years = models.IntegerField(choices=YEARS, blank=False, default=datetime.datetime.now().year)
    item_fields = models.CharField(choices=ITEM_FIELDS_SELECT, max_length=30, blank=False)
    work_fields = models.CharField(choices=WORK_FIELDS_SELECT, max_length=30, blank=False)
    setup_fields = models.CharField(choices=SETUP_FIELDS_SELECT, max_length=30, blank=False)
    plus_points = models.FloatField(null=False, blank=True, default=0.0)
    itemname = models.CharField(max_length=200, blank=False, unique=True)
    ceo_relation = models.ManyToManyField(MyUser, through='Score')

    def __str__(self):
        return self.ceoname

class Score(models.Model):
    TH_SELECT = (
        ('1차','1차'),
        ('2차','2차'),
    )
    myuser = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    ceo = models.ForeignKey(Ceo, on_delete=models.CASCADE, related_name='related_ceo')
    th = models.CharField(choices=TH_SELECT, max_length=20, blank=False)
    score_0 = models.IntegerField(null=False)
    score_1 = models.IntegerField(null=False)
    score_2 = models.IntegerField(null=False)
    score_3 = models.IntegerField(null=False)
    score_4 = models.IntegerField(null=False)
    score_5 = models.IntegerField(null=False)
    score_6 = models.IntegerField(null=False)
    score_7 = models.IntegerField(null=False)
    # score_8 = models.IntegerField(null=False)
    comment = models.TextField(default="", null=False)
    # subtotal = models.IntegerField(null=True, blank=True)
    # total = models.IntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.id, self.ceo)
        # return "self.{}".format(self.ceo) - self까지 반환하면 에러남 (__str__ returned non-string (type int))

    class Meta:
        unique_together = (
            ('myuser', 'ceo',),
            )
