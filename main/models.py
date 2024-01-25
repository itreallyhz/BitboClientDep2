from django.db import models

# Create your models here.

class ResidentInformation(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=100, null=True)
    age = models.IntegerField(default=1)
    birthday = models.DateField(null=True)
    sex = models.CharField(max_length=30, null=True)
    civil_status = models.CharField(max_length=30, null=True)

    #married
    spouse_name = models.CharField(max_length=100, null=True)
    number_of_children= models.IntegerField(null=True)
    names_of_children= models.CharField(max_length=1000, null=True)
   
    #widowed
    cause_of_death = models.CharField(max_length=1000, null=True)

    #Region
    region = models.CharField(max_length=30, null=True)
    province = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    resident_barangay = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    email_address = models.EmailField(max_length=100, null=True)
    occupation = models.CharField(max_length=100, null=True) 
    #employed
    company = models.CharField(max_length=100, null=True)
    date_hired = models.DateField(null=True)
    position = models.CharField(max_length=100, null=True)
    job = models.CharField(max_length=100, null=True)
    #student
    education_level = models.CharField(max_length=100, null=True)
    elem_grade_level = models.CharField(max_length=100, null=True)
    hs_grade_level = models.CharField(max_length=100, null=True)
    shs_strand = models.CharField(max_length=100, null=True)
    #college
    college_year = models.CharField(max_length=100, null=True)
    college_course = models.CharField(max_length=100, null=True)
    college_school = models.CharField(max_length=100, null=True)
    college_school_type = models.CharField(max_length=100, null=True)
    
    birth_order = models.CharField(max_length=100, null=True)
    is_indigenous = models.CharField(max_length=3, null=True)
    #IndigenousYes
    type_of_ethnicity = models.CharField(max_length=3, null=True)

    is_registered_voter = models.CharField(max_length=3, null=True)
    #RegisteredYes
    voting_precint = models.CharField(max_length=3, null=True)
    valid_id = models.CharField(max_length=100, null=True)

    #Family Background
    m_first_name = models.CharField(max_length=100, null=True)
    m_middle_name = models.CharField(max_length=100, null=True)
    m_last_name = models.CharField(max_length=100, null=True)
    m_suffix = models.CharField(max_length=100, null=True)
    f_first_name = models.CharField(max_length=100, null=True)
    f_middle_name = models.CharField(max_length=100, null=True)
    f_last_name = models.CharField(max_length=100, null=True)
    f_suffix = models.CharField(max_length=100, null=True)

    #Household Information Form
    household_name = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    hh_barangay = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=100, null= True)
    type_of_residence = models.CharField(max_length=100, null= True)

    #Emergency Contact Information
    emergency_contact_name = models.CharField(max_length=100, null=True)
    relationship = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)

    def __str__(self):
       return self.first_name + ' ' + self.middle_name + ' ' + self.last_name 
