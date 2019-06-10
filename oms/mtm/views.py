from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Authority, Member, Rule, History


# authority_page_view
def authority(request):
	authoritys = Authority.objects.all()
	ctx = {'authoritys': authoritys}
	return render(request, 'theme/mtm/authority.html', ctx)


# authority_detail_page_view
def authority_detail(request, pk):
	authority = get_object_or_404(Authority, pk=pk)
	ctx = {'authority': authority}
	return render(request, 'theme/mtm/authority_detail.html', ctx)


# vision_forty-one_page_view
def vission(request):
	return render(request, 'theme/mtm/vision.html')


# mtm_members_page_view
def member(request):
	members = Member.objects.all()
	ctx = {'members': members}
	return render(request, 'theme/mtm/member.html', ctx)


# second_account_page_view
def second(request):
	return render(request, 'theme/mtm/second.html',)


def award(request):
	return render(request, 'theme/mtm/award.html')


# rule_page_view
def rule(request):
	rules = Rule.objects.all().order_by('-date')[:4]
	ctx = {'rules': rules}
	return render(request, 'theme/mtm/rule.html', ctx)


# mtmhistory_page_view
def mtmhistory(request):
	historys = History.objects.all()
	ctx = {'historys': historys}
	return render(request, 'theme/mtm/history.html', ctx)