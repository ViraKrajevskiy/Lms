from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from user_auth.models.workers_models.model_teacher import Teacher, Mentor  # Импортируем модели преподавателя и наставника
from user_auth.models.workers_models.model_worker import Staff, WorkerAttendance  # Импортируем модели для сотрудников и их посещаемости
from user_auth.pagination import StandardResultsSetPagination  # Импортируем пагинацию (если потребуется)
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission  # Импортируем кастомные разрешения
from user_auth.serializers.stafff_serializer.staff import StaffSerializer, TeacherSerializer, MentorSerializer  # Импортируем сериализаторы для сотрудников, преподавателей и наставников
from user_auth.serializers.things_for_workers_serializer.WorkerAttandanceSerializer import WorkerAttendanceSerializer  # Импортируем сериализатор для посещаемости
from user_auth.serializers.things_for_workers_serializer.teacher_serializer import WorkerSalaryWaitedPaySerializer  # Импортируем сериализатор для зарплаты сотрудника


# ViewSet для работы с сотрудниками (Staff)
class StaffViewsSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()  # Получаем всех сотрудников из базы данных
    serializer_class = StaffSerializer  # Указываем сериализатор для сотрудников
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Только авторизованные пользователи с нужной ролью могут использовать этот ViewSet
    pagination_class = StandardResultsSetPagination
    # Кастомное действие для получения посещаемости сотрудника
    @action(detail=False, methods=['get'], url_path='my-attendance')
    def my_attendance(self, request):
        user = request.user  # Получаем текущего пользователя
        if not hasattr(user, 'staff'):  # Проверяем, является ли пользователь сотрудником
            return Response({'detail': 'Вы не сотрудник.'}, status=403)  # Если нет, возвращаем ошибку

        attendances = WorkerAttendance.objects.filter(staff=user.staff)  # Получаем посещаемость для сотрудника
        serializer = WorkerAttendanceSerializer(attendances, many=True)  # Сериализуем данные
        return Response(serializer.data)  # Отправляем данные в ответе

    # Кастомное действие для получения зарплаты сотрудника
    @action(detail=False, methods=['get'], url_path='my-salary')
    def my_salary(self, request):
        user = request.user  # Получаем текущего пользователя
        if not hasattr(user, 'staff'):  # Проверяем, является ли пользователь сотрудником
            return Response({'detail': 'Вы не сотрудник.'}, status=403)  # Если нет, возвращаем ошибку

        staff = user.staff  # Получаем объект сотрудника
        paid_salary = staff.salary_pay  # Получаем информацию о выплаченной зарплате
        waiting_salaries = staff.waiting_salaries.all()  # Получаем информацию о зарплатах, которые ожидают выплаты

        # Формируем данные для ответа
        data = {
            "paid_salary": {
                "total_amount_payed": paid_salary.total_amount_payed,  # Общая сумма выплаченной зарплаты
                "datePayDay": paid_salary.datePayDay  # Дата выплаты зарплаты
            } if paid_salary else None,
            "waiting_salaries": WorkerSalaryWaitedPaySerializer(waiting_salaries, many=True).data  # Сериализуем ожидаемые зарплаты
        }
        return Response(data)  # Отправляем данные в ответе


# ViewSet для работы с преподавателями (Teacher)
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()  # Получаем всех преподавателей из базы данных
    serializer_class = TeacherSerializer  # Указываем сериализатор для преподавателей
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Разрешения для авторизованных пользователей с нужной ролью
    pagination_class = StandardResultsSetPagination

# ViewSet для работы с наставниками (Mentor)
class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()  # Получаем всех наставников из базы данных
    serializer_class = MentorSerializer  # Указываем сериализатор для наставников
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Разрешения для авторизованных пользователей с нужной ролью
    pagination_class = StandardResultsSetPagination