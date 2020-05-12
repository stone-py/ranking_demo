from Ranking import models
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.shortcuts import render

def upload(request):
    if request.method == 'POST':
        client_name = request.POST.get('client')
        rank = request.POST.get('rank')
        try:
            if models.ClientMark.objects.filter(client=client_name).exists():
                models.ClientMark.objects.filter(client=client_name).update(rank=rank)
                message='更新成功'
            else:
                models.ClientMark.objects.create(client=client_name,rank=rank)
                message='上传成功'
            success=True
        except:
            success=False
            message='提交失败'
        return HttpResponse(json.dumps({'success':success,'info':message}), content_type="application/json")
    else:
        return render(request, 'upload.html')

    # return HttpResponse('404')
def select_ranking(request):
    if request.method == 'GET':
        try:
            client_name = request.POST.get('client')
            pagemin = request.POST.get('min')
            pagemax = request.POST.get('max')
            mainlist = models.ClientMark.objects.all().order_by('rank')[pagemin:pagemax]
            client = client_name
            return HttpResponse(json.dumps({'datalist':mainlist,'own':client}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({'success':False,'info':'参数错误'}), content_type="application/json")