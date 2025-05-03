from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from user_auth.models.workers_models.model_teacher import Teacher, Mentor
from user_auth.models.workers_models.model_worker import Staff, WorkerAttendance
from user_auth.pagination import StandardResultsSetPagination
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.stafff_serializer.staff import StaffSerializer, TeacherSerializer, MentorSerializer
from user_auth.serializers.things_for_workers_serializer.WorkerAttandanceSerializer import WorkerAttendanceSerializer
from user_auth.serializers.things_for_workers_serializer.teacher_serializer import WorkerSalaryWaitedPaySerializer


class StaffViewsSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

    @action(detail=False, methods=['get'], url_path='my-attendance')
    def my_attendance(self, request):
        user = request.user
        if not hasattr(user, 'staff'):
            return Response({'detail': 'Вы не сотрудник.'}, status=403)

        attendances = WorkerAttendance.objects.filter(staff=user.staff)
        serializer = WorkerAttendanceSerializer(attendances, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='my-salary')
    def my_salary(self, request):
        user = request.user
        if not hasattr(user, 'staff'):
            return Response({'detail': 'Вы не сотрудник.'}, status=403)

        staff = user.staff
        paid_salary = staff.salary_pay
        waiting_salaries = staff.waiting_salaries.all()

        data = {
            "paid_salary": {
                "total_amount_payed": paid_salary.total_amount_payed,
                "datePayDay": paid_salary.datePayDay
            } if paid_salary else None,
            "waiting_salaries": WorkerSalaryWaitedPaySerializer(waiting_salaries, many=True).data
        }
        return Response(data)



class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]