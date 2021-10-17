from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        end_time = localtime() if self.leaved_at is None else localtime(self.leaved_at)
        delta = end_time - localtime(self.entered_at)
        return delta.seconds

    def is_long(self, minutes=60):
        return self.get_duration() // 60 > minutes

    def format_entered_at(self):
        return localtime(self.entered_at).strftime("%d-%m-%Y %H:%M")

    def format_duration(self, duration):
        hours = duration // 3600
        minutes = duration % 3600 // 60
        return '{:0=2}h {:0=2}m'.format(hours, minutes)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= 'leaved at ' + str(self.leaved_at) if self.leaved_at else 'not leaved'
        )
