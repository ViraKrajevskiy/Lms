from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.student_package.model_student import Student, Parents  # Импортируем модели студентов и родителей
from user_auth.pagination import StandardResultsSetPagination  # Импортируем пагинацию
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission  # Импортируем кастомные разрешения
from user_auth.serializers.student_serializer.student_serializer import StudentSerializer, ParentsSerializer  # Импортируем сериализаторы для студентов и родителей
from rest_framework import viewsets
from rest_framework.decorators import action  # Импортируем декоратор для добавления кастомных действий
from rest_framework.response import Response  # Импортируем ответ на запрос
from rest_framework.permissions import IsAuthenticated  # Импортируем разрешения для авторизации

# ViewSet для работы с моделью Student
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()  # Получаем все объекты студентов из базы данных
    serializer_class = StudentSerializer  # Указываем, какой сериализатор использовать
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Разрешаем доступ только авторизованным пользователям с нужными правами
    pagination_class = StandardResultsSetPagination

    # Кастомное действие для получения активных студентов
    @action(detail=False, methods=['get'], url_path='active')
    def active_students(self, request):
        students = Student.objects.filter(student_position='active')  # Фильтруем студентов с активной позицией
        serializer = self.get_serializer(students, many=True)  # Преобразуем данные в нужный формат
        return Response(serializer.data)  # Отправляем данные в ответе

    # Кастомное действие для получения завершивших учебу студентов
    @action(detail=False, methods=['get'], url_path='finished')
    def finished_students(self, request):
        students = Student.objects.filter(student_position='end')  # Фильтруем студентов, завершивших учебу
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)

    # Кастомное действие для получения студентов, которые ушли
    @action(detail=False, methods=['get'], url_path='left')
    def left_students(self, request):
        students = Student.objects.filter(student_position='left')  # Фильтруем студентов, покинувших учебу
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.is_admin():
            return Student.objects.all()
        elif user.is_supervisor():
            return Student.objects.filter(group__mentor__staff__user=user)
        elif user.is_teacher():
            return Student.objects.filter(group__teacher__staff__user=user)
        elif user.is_student():
            return Student.objects.filter(user=user)
        return Student.objects.none()

    @swagger_auto_schema(
        operation_summary="Список студентов",
        operation_description="Учителя видят студентов из своих групп. Менторы — своих. Студент — только себя. Админы — всех."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
# ViewSet для работы с моделью Parents
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parents.objects.all()  # Получаем все объекты родителей из базы данных
    serializer_class = ParentsSerializer  # Указываем сериализатор для родителей
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Разрешаем доступ только авторизованным пользователям с нужными правами
    pagination_class = StandardResultsSetPagination