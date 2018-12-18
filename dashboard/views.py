from django.shortcuts import render


def dashboard(request):
	return render(request, 'dashboard/dashboard.html')


def home(request):
	return render(request, 'dashboard/dash_home.html')


def teacher(request):
	return render(request, 'dashboard/teacher.html')


def students(request):
	return render(request, 'dashboard/students.html')


def sayekh(request):
	return render(request, 'dashboard/sayekh.html')


def stuff(request):
	return render(request, 'dashboard/stuff.html')


def history(request):
	return render(request, 'dashboard/history.html')


def gallery(request):
	return render(request, 'dashboard/gallery.html')


def amgallery(request):
	return render(request, 'dashboard/amgallery.html')


def authority(request):
	return render(request, 'dashboard/authority.html')


def mtmhistory(request):
	return render(request, 'dashboard/mtmhistory.html')


def notice(request):
	return render(request, 'dashboard/notice.html')


def rules(request):
	return render(request, 'dashboard/rules.html')


def members(request):
	return render(request, 'dashboard/members.html')


def feedback(request):
	return render(request, 'dashboard/feedback.html')


def mullfound(request):
	return render(request, 'dashboard/mullfound.html')


def kollanfound(request):
	return render(request, 'dashboard/kollanfound.html')