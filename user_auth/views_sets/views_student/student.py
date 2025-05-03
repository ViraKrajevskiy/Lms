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


# ViewSet для работы с моделью Parents
class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parents.objects.all()  # Получаем все объекты родителей из базы данных
    serializer_class = ParentsSerializer  # Указываем сериализатор для родителей
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Разрешаем доступ только авторизованным пользователям с нужными правами
