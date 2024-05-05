from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import stud_login,student_info,activity
from django.core.files import File
                                           
@csrf_exempt
def login_system(request):
    cont={ 'flag':''}
    if len(request.POST)==2:
        a,b=request.POST.items()
        if(a[0]=="usr"):
            try:
                id=(int(a[1]),)
            except:
                cont['flag']="username or password invalid"
                return render(request,'login.html',cont)
            
            pwd=(b[1],)
            if id in stud_login.objects.values_list('username') and pwd in stud_login.objects.values_list('password'):
                acts=list(activity.objects.filter(std_id=int(a[1]),status='1').values())
                stud=student_info.objects.get(regno=int(a[1]))
                if(len(acts)>0):
                    sum=0
                    for i in range(len(acts)):
                        sum+=acts[i]['act_points']
                    stud.total_points=sum
                    
                else:
                    stud.total_points=0
                stud.save()

                context={'stud':student_info.objects.get(regno=int(a[1])),}
                return render(request,'student.html',context)
            else:
                cont['flag']="username or password invalid"
                return render(request,'login.html',cont)
            
        elif(b[0]=='opcode'):
            context={'stud':student_info.objects.get(regno=int(a[1]))}
            if(b[1]=='request'):
                return render(request,'index.html',context)
            elif(b[1]=='home'):
                acts=list(activity.objects.filter(std_id=int(a[1]),status='1').values())
                stud=student_info.objects.get(regno=int(a[1]))
                if(len(acts)>0):
                    sum=0
                    for i in range(len(acts)):
                        sum+=acts[i]['act_points']
                    
                    stud.total_points=sum
                else:
                    stud.total_points=0
                stud.save()

                context={'stud':student_info.objects.get(regno=int(a[1])),}
                return render(request,'student.html',context)
            elif(b[1]=='view'):
                marked_acts=activity.objects.filter(std_id=int(a[1]),status='1')
                context={'stud':student_info.objects.get(regno=int(a[1])),'acts':marked_acts}
                return render(request,"view_Act.html",context)
            elif(b[1]=='notify'):
                marked_acts=activity.objects.filter(std_id=int(a[1]),status='1')
                reject=activity.objects.filter(std_id=int(a[1]),status='2')
                pending=activity.objects.filter(std_id=int(a[1]),status='0')
                context={'stud':student_info.objects.get(regno=int(a[1])),'acts':marked_acts,'reject':reject,'pending':pending}
                return render(request,"notify.html",context)
            elif(b[1]=='logout'):
                cont={'flag':''}
                return render(request,'login.html',cont)
            elif(b[1]=='pwd_change'):
                cont={'flag':'','stud':student_info.objects.get(regno=int(a[1]))}
                return render(request,'pwd_change.html',cont)
        elif(a[0]=='activity'):
            act=activity()
            std_obj=student_info.objects.get(regno=int(b[1]))
            act.std_id=std_obj
            act.act_name=a[1]
            act.status='0'
            f=dict(request.FILES.items())
            act.proof=f['file']
            act.std_name=student_info.objects.filter(regno=int(b[1])).values()[0]['name']
            act.tut_id=student_info.objects.filter(regno=int(b[1])).values()[0]['tut_id']
            act.save()
            context={'stud':student_info.objects.get(regno=int(b[1]))}
            return render(request,'index.html',context)
    elif(len(request.POST)==3):
        a,b,c=request.POST.items()
        stud=student_info.objects.get(regno=int(c[1]))
        stud_user=stud_login.objects.get(username=int(c[1]))
        if(a[1]==b[1] and len(a[1])<=20 and len(b[1])<=20 and len(a[1])>=4 and len(b[1])>=4):
            flag='password changed'
            stud_user.password=a[1]
            stud_user.save()
        else:
            flag="retry"
        context={'flag':flag,'stud':stud}
        return render(request,"pwd_change.html",context)
    else:
        return render(request,'login.html',cont)
    


