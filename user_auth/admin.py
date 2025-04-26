from django.contrib import admin
from .models import *


admin.site.register([StudyDay,  User,  Teacher,  CourseDuration,  StudentPay,  PyedForWorker,
                     Student,  PositionLevel,   WorkDay,  WorkerSalaryPayed,  WorkerAttendance,
                     WorkerSalaryWaitedPay,  Course,  Staff,  Department,  Attendance,CourseLevel, AttendanceRecord,
                     Parents,  GroupHomework,  StudentHomework,  Mentor,  Group,  Lesson,  Room , ])
