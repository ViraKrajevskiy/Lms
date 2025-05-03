from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from user_auth.models.pay_model_salary.pay_model_for_student import StudentPay
from user_auth.pagination import StandardResultsSetPagination
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.pay_serializer.pay_student_serializer import PayStudentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class PayStudentViewsSet(viewsets.ModelViewSet):
    queryset = StudentPay.objects.all()  # Получаем все объекты StudentPay
    serializer_class = PayStudentSerializer  # Указываем сериализатор для преобразования данных
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Разрешаем доступ только авторизованным пользователям с нужной ролью
    pagination_class = StandardResultsSetPagination

    @action(detail=False, methods=['get'], url_path='my-payments')
    def my_payments(self, request):
        """
        Метод для получения всех платежей конкретного студента.
        Ограничивает доступ только к платежам того студента, который сделал запрос.
        """
        user = request.user  # Получаем текущего пользователя из запроса
        if not hasattr(user, 'student'):  # Проверяем, что у пользователя есть привязка к студенту
            return Response({"detail": "Вы не являетесь студентом."}, status=403)  # Если это не студент, возвращаем ошибку 403

        payments = StudentPay.objects.filter(student=user.student)  # Получаем все платежи, связанные с этим студентом
        serializer = self.get_serializer(payments, many=True)  # Сериализуем данные
        return Response(serializer.data)  # Отправляем сериализованные данные в ответ
