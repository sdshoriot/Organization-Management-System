from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Notice


# notice_page_view
def notice(request):
	notices = Notice.objects.all().order_by('-date')[:4]
	ctx = {'notices': notices}
	return render(request, 'theme/notice/notice.html', ctx)


# notice_details_page_view
def notice_details(request, pk):
	notice = get_object_or_404(Notice, pk=pk)
	ctx = {'notice': notice}
	return render(request, 'theme/notice/notice-details.html', ctx)