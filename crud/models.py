from django.db import models

STATUS_CHOICES = (
    ('Scheduled', 'Scheduled'),
    ('On Track', 'On Track'),
    ('Off Track', 'Off Track'),
    ('In Jeopardy', 'In Jeopardy'),
    ('Complete', 'Complete'),
    ('Closed', 'Closed'),
)


class Task(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Scheduled'
    )

    class Meta:
        db_table = 'task'

    def __str__(self):
        return self.name
