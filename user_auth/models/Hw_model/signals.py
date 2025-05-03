from django.db.models.signals import post_save
from django.dispatch import receiver
from user_auth.models.Hw_model.model_home_work_lesson import GroupHomework, StudentHomework

@receiver(post_save, sender=GroupHomework)
def create_student_homework(sender, instance, created, **kwargs):
    if created:
        students = instance.group.students.all()
        for student in students:
            StudentHomework.objects.create(student=student, group_homework=instance)
