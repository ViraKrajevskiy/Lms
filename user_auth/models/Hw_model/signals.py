from django.db.models.signals import post_save
from django.dispatch import receiver
from user_auth.models.Hw_model.model_home_work_lesson import GroupHomework, StudentHomework

# Этот сигнал срабатывает после создания новой записи GroupHomework
@receiver(post_save, sender=GroupHomework)
def create_student_homework(sender, instance, created, **kwargs):
    # Проверка, что запись была только что создана (не обновлена)
    if created:
        # Получаем всех студентов, которые принадлежат группе, к которой привязан GroupHomework
        students = instance.group.students.all()

        # Перебираем всех студентов, чтобы для каждого создать запись StudentHomework
        for student in students:
            # Создаем новую запись StudentHomework для каждого студента
            StudentHomework.objects.create(student=student, group_homework=instance)

            # Логирование для отладки (необязательно, но полезно для отладки)
            print(f"Создано домашнее задание для студента {student} по группе {instance.group}")

