import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# pollアプリケーションでは、QuestionとChoiceの2つのモデルを使う

"""
各モデルは1つのクラスで表現
いずれもdjango.db.models.Modelのサブクラス
個々のクラス変数は、モデルのデータベースフィールドを表す

question_textやpub_dateのようなFieldインスタンスの名前は、
pythonコードで使うと共に、データベースも列の名前として使う
xxxField()の第一引数で、フィールド名を設定できる（下の'date published'のように）

ForeignKeyはリレーションシップの定義
以下では、Choiceが1つのQuestionに関連づけられることを意味している
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # 文字フィールド
    pub_date = models.DateTimeField('date published')  # 日時フィールド

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=10)

    def __str__(self):
        return self.choice_text

