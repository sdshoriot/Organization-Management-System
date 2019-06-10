from django.shortcuts import render


def sineup(request):
    return render(request, 'theme/account/sine-up.html')


def login(request):
    return render(request, 'theme/account/sine-in.html')


def accounts(request):
	return render(request, 'theme/account/result.html')    