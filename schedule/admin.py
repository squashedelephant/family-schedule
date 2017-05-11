from django.contrib import admin

from schedule.models import Activity, Child, ChildImage, Color, Event, Parent, ParentImage, WeekDay

admin.site.register(Activity)
admin.site.register(Child)
admin.site.register(ChildImage)
admin.site.register(Color)
admin.site.register(Event)
admin.site.register(Parent)
admin.site.register(ParentImage)
admin.site.register(WeekDay)
