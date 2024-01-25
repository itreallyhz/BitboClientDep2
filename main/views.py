from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ResidentInformation
from .serializers import ResidentInformationSerializer

# adminside
def login(request):
    return render(request, 'main/login.html')

def SignUp(request):
    return render(request, 'main/signup.html')
def services(request):
    return render(request, 'main/services.html')

def navbar(request):
    return render(request, 'main/navbar.html')

def navbar_index(request):
    return render(request, 'main/navbar_index.html')

def profiles(request):
    return render(request, 'main/profiles.html')

def officials(request):
    return render(request, 'main/officials.html')

def brgy_officials(request):
    return render(request, 'main/brgy_officials.html')

def forms(request):
    return render(request, 'main/forms.html')


def projects(request):
    return render(request, 'main/proj_prog.html')

def admin_forms(request):
    return render(request, 'main/admin_forms.html')

def gov_admin(request):
    return render(request, 'main/gov_admin.html')
def incident_logs(request):
    return render(request, 'main/incident_logs.html')

def clearance_permit(request):
    return render(request, 'main/clearance_permit.html')

def privacy_policy(request):
    return render(request, 'main/privacy_policy.html')

def doc_management(request):
    return render(request, 'main/doc_management.html')

def faqs(request):
    return render(request, 'main/faqs.html')

def view_proj(request):
    return render(request, 'main/view_proj.html')
def view_gov(request):
    return render(request, 'main/view_gov.html')
def personnel_forms(request):
    return render(request, 'main/personnel_forms.html')
def personnel(request):
    return render(request, 'main/personnel.html')
def add_clearances(request):
    return render(request, 'main/add_clearances.html')


def system_config(request):
    return render(request, 'main/system_config.html')
def terms_conditions(request):
    return render(request, 'main/terms_conditions.html')
def signup2(request):
    return render(request, 'main/signup2.html')
def add_incident(request):
    return render(request, 'main/add_incident.html')

#userside
def user_login(request):
    return render(request, 'user/user_login.html')
def user_home(request):
    return render(request, 'user/user_home.html')

def user_index(request):
    return render(request, 'user/user_index.html')
def user_proj_prog(request):
    return render(request, 'user/user_proj_prog.html')
def user_profiles(request):
    return render(request, 'user/user_profiles.html')
def user_clearance(request):
    return render(request, 'user/user_clearance.html')

def user_doc_management(request):
    return render(request, 'user/user_doc_management.html')
def user_officials(request):
    return render(request, 'user/user_officials.html')
def user_governance(request):
    return render(request, 'user/user_governance.html')






#Backend
@api_view(['GET'])
def GetAllResidents(request):
    get_residents = ResidentInformation.objects.all()
    serializer = ResidentInformationSerializer(get_residents, many=True)
    return Response(serializer.data)

#CREATE
#@api_view(['GET', 'POST'])
#def CreateNewResident(request):
#    data = request.data
#    serializer = ResidentInformationSerializer(data=data)
#    if serializer.is_valid():
#        serializer.save()
#        return Response({"Success":"The post was successfully created"}, status=201)
#    else:
#        return Response(serializer.errors, status=400)

#TRY API

@api_view(['GET', 'POST'])
def CreateNewResident(request):
    if request.method == 'POST':
        data = request.data
        serializer = ResidentInformationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # If it's an API request, return a JSON response
            if request.accepted_renderer.format == 'json':
                return Response({"Success": "The post was successfully created WOOT"}, status=status.HTTP_201_CREATED)
            # If it's an HTML form submission, you can redirect or render a success page
            else:
                # Replace the following line with the appropriate redirect or response
                return redirect('success_page')
        else:
            # Handle invalid data for both API and HTML submissions
            # If it's an API request, return a JSON response with errors
            if request.accepted_renderer.format == 'json':
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # If it's an HTML form submission, you can render an error page or return an appropriate response
            else:
                # Replace the following line with the appropriate error handling
                return render(request, 'error_page.html', {'errors': serializer.errors})
    # Handle GET requests
    return Response({"message": "This is a GET request."})
    
#DELETE
@api_view(['DELETE'])
def DeleteResident(request):
    resident_id = request.data.get('resident_id')
    try:
       resident = ResidentInformation.objects.get(id=resident_id)
       resident.delete()
       return Response({"Success":"The resident was successfully deleted"}, status=201)
    except ResidentInformation.DoesNotExist:
        return Response({"Error":"The resident does not exists."}, status=404)
    
#GET
@api_view(['GET'])
def GetResident(request):
    resident_id = request.data.get('resident_id')
    try:
       residentinformation = ResidentInformation.objects.get(id=resident_id)
       serializer = ResidentInformationSerializer(residentinformation)
       return Response(serializer.data)
    except ResidentInformation.DoesNotExist:
        return Response({"Error":"The resident does not exists."}, status=404)
    
#UPDATE
@api_view(['PUT'])
def UpdateResident(request):
    resident_id = request.data.get('resident_id')
    get_new_first_name = request.data.get('new_first_name')
    get_new_middle_name = request.data.get('new_middle_name')
    get_new_last_name = request.data.get('new_last_name')

    try:
        residentinformation = ResidentInformation.objects.get(id=resident_id)
        if get_new_first_name:
            residentinformation.first_name = get_new_first_name
        if get_new_middle_name:
            residentinformation.middle_name = get_new_middle_name
        if get_new_last_name:
            residentinformation.last_name = get_new_last_name
        
        residentinformation.save()
        return Response({"Success":"The resident was successfully updated."}, status=404)
    
    except ResidentInformation.DoesNotExist:
        return Response({"Error": "The resident does not exists"}, status=404)
    
