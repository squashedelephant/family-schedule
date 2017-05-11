from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=30)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=20)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class WeekDay(models.Model):
    name = models.CharField(max_length=9)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class Parent(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    deleted = models.BooleanField(default=False)

    def __repr__(self):
        return '{} {}'.format(self.first_name,
                              self.last_name)

    def __str__(self):
        return '{} {}'.format(self.first_name,
                              self.last_name)

class ParentImage(models.Model):
    parent = models.ForeignKey(Parent,
                               null=False,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    
    def __repr__(self):
        return self.url

    def __str__(self):
        return self.url

class Child(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    parents = models.ManyToManyField(Parent)
    deleted = models.BooleanField(default=False)

    def __repr__(self):
        return '{} {}'.format(self.first_name,
                              self.last_name)

    def __str__(self):
        return '{} {}'.format(self.first_name,
                              self.last_name)

class ChildImage(models.Model):
    child = models.ForeignKey(Child,
                              null=False,
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    deleted = models.BooleanField(default=False)
    
    def __repr__(self):
        return self.url

    def __str__(self):
        return self.url

class Dashboard(models.Model):
    child = models.ForeignKey(Child,
                              null=False,
                              on_delete=models.CASCADE)
    parents = models.ManyToManyField(Parent)
    weekday = models.ForeignKey(WeekDay,
                                null=False)

    def __repr__(self):
        return '{}: {}: {}'.format(self.child,
                                   self.parents,
                                   self.weekday)

    def __str__(self):
        return '{}: {}: {}'.format(self.child,
                                   self.parents,
                                   self.weekday)

class Event(models.Model):
    child = models.ForeignKey(Child,
                              null=False,
                              on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent)
    created = models.DateTimeField(db_index=True,
                                   null=False)
    name = models.ForeignKey(Activity,
                              null=False)
    color = models.ForeignKey(Color,
                              null=False)
    count = models.IntegerField(default=0)
    deleted = models.BooleanField(default=False)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
