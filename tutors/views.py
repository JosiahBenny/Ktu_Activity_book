from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import tutors_login,tutors_info
from student.models import student_info,activity
@csrf_exempt
def main(req):
    cont={'flag':''}
    if len(req.POST)==2:
        a,b=req.POST.items()
        if(a[0]=='usr'):
            try:
                usr=int(a[1])
                pwd=b[1]
            except:
                cont={'flag':'invalid username or password'}
                return render(req,'tut_login.html',cont)
            t1=(usr,);t2=(pwd,)
            if t1 in tutors_login.objects.values_list('username') and t2 in tutors_login.objects.values_list('password'):
                stud_list=student_info.objects.filter(tut_id=usr)
                tutor=tutors_info.objects.get(tut_id=usr)
                tutor.total_stud=len(stud_list)
                tutor.save()
                context={'tut':tutor}
                return render(req,'tutor.html',context)
            else:
                cont={'flag':'invalid username or password'}
                return render(req,'tut_login.html',cont)
        elif(a[0]=='id'):
            tutor=tutors_info.objects.get(tut_id=int(a[1]))
            if(b[1]=='home'):
                context={'tut':tutor}
                return render(req,'tutor.html',context)
            elif(b[1]=='mark'):
                act=activity.objects.filter(status='0',tut_id=int(a[1]))
                context={'tut':tutor,'act':act}
                return render(req,'mark.html',context)
            elif(b[1]=='logout'):
                cont={'flag':''}
                return render(req,"tut_login.html",cont)
            elif(b[1]=='view'):
                stud=student_info.objects.filter(tut_id=a[1])
                context={'tut':tutor,'stud':stud}
                return render(req,'view_stud.html',context)
            elif(b[0]=='activity'):
                act=activity.objects.get(id=int(b[1]))
                context={'tut':tutor,'act':act}
                return render(req,'check.html',context)
            elif(b[1]=='pwd_change'):
                cont={'flag':'','tut':tutors_info.objects.get(tut_id=int(a[1]))}
                return render(req,'pwd_change1.html',cont)
    elif len(req.POST)==4:
        a,b,c,d=req.POST.items()
        act=activity.objects.get(id=int(c[1]))
        act.status=a[1]
        try:
            num=int(b[1])
        except:
            num=0
        if(num<0 or num>80):
            act.act_points=0 
            act.status='2'
        else:
            act.act_points=num
        stud=student_info.objects.get(regno=act.std_id.regno)
        if(act.status=='1'):
            stud.total_points+=num
        elif(act.status=='2'):
            act.act_points=0
        act.save()
        stud.save()
        tutor=tutors_info.objects.get(tut_id=int(d[1]))
        context={'tut':tutor}
        return render(req,'tutor.html',context)
    elif(len(req.POST)==3):
        a,b,c=req.POST.items()
        tut=tutors_info.objects.get(tut_id=int(c[1]))
        tut_user=tutors_login.objects.get(username=int(c[1]))
        if(a[1]==b[1] and len(a[1])<=20 and len(b[1])<=20 and len(a[1])>=4 and len(b[1])>=4):
            flag='password changed'
            tut_user.password=a[1]
            tut_user.save()
        else:
            flag="retry"
        context={'flag':flag,'tut':tut}
        return render(req,"pwd_change1.html",context)
    
    else:
        return render(req,'tut_login.html',cont)