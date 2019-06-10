from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Shaykh, Teacher, Student, Stuff, History


# shaykh_page_view
def shaykh(request):
	shaykhs = Shaykh.objects.all()
	ctx = {'shaykhs': shaykhs}
	return render(request, 'theme/arabic/shaykh.html', ctx)


# shaykh_detail_page_view
def shaykh_detail(request, pk):
	shaykh = get_object_or_404(Shaykh, pk=pk)
	ctx = {'shaykh': shaykh}
	return render(request, 'theme/arabic/shaykh_detail.html', ctx)


# teacher_page_view
def teacher(request):
	teachers = Teacher.objects.all()
	ctx = {'teachers': teachers}
	return render(request, 'theme/arabic/teacher.html', ctx)


# teacher_detail_page_view
def teacher_detail(request, pk):
	teacher = get_object_or_404(Teacher, pk=pk)
	ctx = {'teacher': teacher}
	return render(request, 'theme/arabic/teacher_detail.html', ctx)


def student(request):
	return render(request, 'theme/arabic/student.html')


# stuff_page_view
def stuff(request):
	stuffs = Stuff.objects.all()
	ctx = {'stuffs': stuffs}
	return render(request, 'theme/arabic/stuff.html', ctx)


# history_page_view
def history(request):
	historys = History.objects.all()
	ctx = {'historys': historys}
	return render(request, 'theme/arabic/history.html', ctx)