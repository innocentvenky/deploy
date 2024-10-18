from django.shortcuts import render
import datetime

# Create your views here.\
def demo(request):
    date=datetime.datetime.now()
    time=int(date.strftime("%H"))
    time=21
    msg="HII! very very "
    if time<12:
        msg+="Good morning"
    elif time<16:
        msg+="Good afternoon"
    elif time<20:
        msg+="Good evening"
    else:
        msg+="Good night"
    my_dict={"date":date,'time':time,"msg":msg}
    return render(request,'demo.html',context=my_dict)
    

