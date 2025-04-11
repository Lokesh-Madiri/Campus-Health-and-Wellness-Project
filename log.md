FEB - 21 : 
    timestamp 1:
        Homepage\urls : added links to the pages i created.

        Homepage\views : added the respected views to the urls.

        Project1\settings : 1.added the static file dir to search for.
        
                            2.added the templates file dir to search for.

        Project1\static : added static files and not linked up yet.

        Project1\templates : added the html files required.

    timestamp 2 :

        Project1\static : linked up with html and running.

        templates\Homepage : deleted the static loader for awesome font link (cdn)

        Project1 : executed the migrations and created a superuser for the database with the email mlplok
    
MAR 06 :
    timestamp 1:
        templates\Homepage1: changed the linking from html wise to django wise

        Project1 : added a new app for acccounts section

        accounts\views : connected login page.

        accounts\views : connected registration page.

    timestamp 2:
        Project1\settings : added the database and running.

        accounts\views|urls : changed respectively.

MAR 07 :
    timestamp1 :


MAR 15 :
    timestamp2 :
    view.py : changed the appname of the homepage

    login flow : completed and running

MAR 16:
    Timestamp1:
        views.py:
            Fixed issue where user role was not being saved correctly in the registration function.
            Change: Updated <select> option values in registration.html to match ROLE_CHOICES in models.py.
        registration.html:
            Change: Fixed <option value="default">Citizen</option> to <option value="Citizen">Citizen</option> so that the correct role is stored.
        userdashboard function (views.py):
            Change: Debugged user role retrieval and ensured UserProfile is correctly assigned.
            Change: Added print(f"User Profile Found: {user_profile.role}") for debugging and confirmed correct role assignment.
        login flow:
            Status: Completed and running successfully.
            Change: Fixed redirection after failed login by adding a popup message.
            Change: Ensured messages.error(request, "Login failed. Please try again.") displays correctly on homepage.html.
    Timestamp 2:
        
    
    Error Encountered: NoReverseMatch at /appointments/appointment/5/ for doctor_dashboard.
    Diagnosis: Django could not find doctor_dashboard because the correct namespace was missing.

    Changes Made:
    views.py (Appointments App)
        Change: Updated redirection inside appointment_detail function to use the correct namespace.
        Before: return redirect("doctor_dashboard")
        After: return redirect("accounts:doctordashboard")
    urls.py (Accounts App)
        Change: Verified that doctordashboard was correctly defined with:
        python
        path('doctordashboard/', views.doctor_dashboard, name='doctordashboard')
    urls.py (Main Project)
        Change: Ensured that the accounts app was correctly included with a namespace: