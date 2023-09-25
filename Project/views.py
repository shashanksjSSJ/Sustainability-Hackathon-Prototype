from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def userLogin(request):
    return render(request, 'userLogin.html')

def lawyerLogin(request): 
    return render(request, 'LawyerLogin.html')

def DepartmentLogin(request): 
    return render(request, 'DepartmentLogin.html')

def Register(request): 
    return render(request, 'Register.html')

def Announcement(request): 
    return render(request, 'Announcement.html')

def UserHome(request): 
    return render(request, 'UserHome.html')

def findLawyer(request): 
    return render(request, 'findlawyers.html')

def calendar(request): 
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
    date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    return render(request, 'calendar.html', {'days': days, 'date': date})


def departmentHome(request): 
    return render(request, 'DepartmentHome.html')

def makeannouncements(request): 
    return render(request, 'makeAnnouncements.html')

def allotment(request): 
    return render(request, 'Alotment.html')

def allotmentcalendar(request): 
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
    date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    return render(request, 'AllotmentCalendar.html', {'days': days, 'date': date})

def updatecalendar(request):
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon']
    date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    return render(request, 'updateCalendar.html', {'days': days, 'date': date})

def lawyerhome(request):
    return render(request, 'lawyerhome.html')

def viewcase(request): 
    return render(request, 'viewcase.html')

def updatecase(request): 
    return render(request, 'updateclient.html')

def reallocate(request): 
    return render(request, 'reallocatetime.html')

def activecases(request): 
    return render(request, 'activecases.html')

def clientmessages(request): 
    return render(request, 'clientmessages.html')

def filecomplaint(request): 
    return render(request, 'filecomplaints.html')

def complaints(request): 
    return render(request, 'complaints.html')
