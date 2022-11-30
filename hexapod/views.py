from django.shortcuts import render,redirect
from hexapod.vidwanquery import query as vq
from hexapod.vidwanprofilepage import author_profile,download

from hexapod.google_scholar import query as q
from hexapod.profile_page import author_profile as ap
from hexapod.profile_page import download as dn
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse, response
import time
# Create your views here.

def home(request):

    if request.method == "POST":
        search_query = request.POST.get('search')
        vq(search_query)
        q(search_query)
        lst=[]
        for i in vq.list:
            lst.append(i)
        for i in q.list:
            lst.append(i)
        # context = query.listnameaff
        auth_dict={'authdata':lst.copy()}
        print(auth_dict)
        home.context = auth_dict
        return redirect('/results')
        # return render(request, 'home.html')
    return render(request,"home.html")


def results(request):
    if request.method == "GET":
        context = home.context
        return render(request, 'results.html', context)
    
    if request.method == "POST":
        id = request.POST.get('id')
        expertid = home.context['authdata'][int(id)]['expertid']
        if expertid.isdigit():
            results.url = "https://vidwan.inflibnet.ac.in/profile/"+str(expertid)
            author_profile(results.url)
            results.authdatadict = author_profile.authorprofiledata
        else:
            ap(expertid)
            results.authdatadict=ap.authorprofiledata
        
        response = redirect('profile')
        return response


def profile(request):

    if request.method == "GET":
        time.sleep(12)
        try:
            context = results.authdatadict
            # return JsonResponse(context)
            return render(request,"profile.html",context)
        except:
            response = redirect('profile')
            return response
    if request.method == "POST":
        try:
            download()
        except:
            dn()
        # return render(request,"profile.html",context)
        response = redirect('profile')
        return response

    