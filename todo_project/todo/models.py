from django.db import models
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
    """
    Model to store multiple tags for each todo item also will prevent duplicate tags
    """
    name = models.CharField(max_length=100, help_text='Enter a tag (e.g. Important)')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Tags"



class TodoItem(models.Model):
    """
    Model to store todo items
    """

    title = models.CharField(max_length=100, help_text='Enter a title for the todo item', null=False, blank=False)
    description = models.TextField(max_length=1000, help_text='Enter a description for the todo item', null=False, blank=False)
    tags = models.ManyToManyField(Tag, help_text='Select a tag for this todo item', blank=True)
    created_at = models.DateTimeField(default=timezone.now, auto_now_add=True)
    due_date = models.DateTimeField(help_text='Enter the due date for the todo item', null=True, blank=True)

    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled')
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN',
        help_text='Select the status of the todo item',
        null=False,
        blank=False
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Todo Entries"
        ordering = ['-created_at']  # Order by most recently created first

    def save(self, *args, **kwargs):
        """
        Override save method to handle status updates based on due date
        """
        # Automatically mark as overdue if due date has passed and not already completed or cancelled
        if (self.due_date and 
            self.due_date < timezone.now() and 
            self.status not in ['COMPLETED', 'CANCELLED']):
            self.status = 'OVERDUE'
        
        super().save(*args, **kwargs)
