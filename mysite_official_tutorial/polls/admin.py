from django.contrib import admin

# Register your models here.
from .models import Question
# Questionオブジェクトがadminインターフェースを持つということを
# adminに伝える
admin.site.register(Question)
