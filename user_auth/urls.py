from django.urls import path,include
from rest_framework.routers import DefaultRouter

from user_auth.serializers.login_and_registration_serializer.logins_serializer import *

from user_auth.views_sets.views_login.login import *
from user_auth.views_sets.views_login.logout import *
from user_auth.views_sets.views_login.otp_view import *

from user_auth.views_sets.views_workers.workers import *
from user_auth.views_sets.view_sets_user.user_views_set import *
from user_auth.views_sets.views_group.group import *
from user_auth.views_sets.views_student.student import *
from user_auth.views_sets.views_course.course_views import *
from user_auth.views_sets.views_lesson.lesson import *
from user_auth.views_sets.views_workers.stafff import *
from user_auth.views_sets.views_sets_pay.for_worker import *
from user_auth.views_sets.views_sets_pay.for_student import *
from user_auth.views_sets.viewset_attendance.attendance import *


router = DefaultRouter()
router.register(r'student_hw_add',StudentAddHwViewSet)
router.register(r'attendance' ,AttendanceViewSet)
router.register(r'users', UserViewSet)
router.register(r'group_homework', GroupHomeworkViewSet)
router.register(r'student_homework', StudentHomeworkViewSet)
router.register(r'lessons', LessonViewsSet)
router.register(r'study_days', StudyDayViewSet)
router.register(r'course_durations', CourseDurationViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'parents', ParentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'mentors', MentorViewSet)
router.register(r'work_days', WorkDayViewSet)
router.register(r'position_levels', PositionLevelViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'payed_for_worker_salary', PayForWorkerViewSet)
router.register(r'worker_salary_waited_pay', WorkerSalaryWaitedPayViewSet)
router.register(r'staff', StaffViewsSet)
router.register(r'pay_for_student', PayStudentViewsSet)
router.register(r'course_level',CourseLevelViewSet)
router.register(r'worker_salary_payed',WorkerSalaryPayedViewSet)
router.register(r'worker_attendance',WorkerAttendanceViewSet)
router.register(r'room',RoomViewSet)


urlpatterns = [
    path('auth/request-otp/', RequestOTPView.as_view(), name='request_otp'),
    path('auth/change-password/', ConfirmOTPAndChangePasswordView.as_view(), name='change_password'),

    path('login/', LoginApi.as_view(), name='login'),
    path('logout/', LogoutApi.as_view(), name='logout'),
]



# Добавление маршрутов из DefaultRouter
urlpatterns += router.urls
