from django.db import models
from django.contrib import auth
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# from django.contrib.auth import get_user_model
# User = get_user_model()

from django.contrib.auth.models import User
# Create your models here.
from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class State(models.Model):
        """
        Model representing US States
        """
        name = models.CharField(max_length=50, help_text="Enter a State")


        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name


class Country(models.Model):
        """
        Model representing countries
        """
        name = models.CharField(max_length=100, help_text="Enter a Country")


        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Ethnicity(models.Model):
        """
        Model representing ethnicity
        """
        name = models.CharField(max_length=100, help_text="Enter an Ethnicity")


        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Test(models.Model):
        """
        Model representing a test in Lab
        """
        name = models.CharField(max_length=50, help_text="Enter a lab test")


        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name


class Day(models.Model):
        """
        Model representing a day in program
        """
        name = models.CharField(max_length=50, help_text="Enter a day #(e.g. Day 0, Day 83)")


        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Referrer(models.Model):
        """
        Model representing a referrer (Eg. Doctor, Google, Ad, Etc.)
        """
        name = models.CharField(max_length=50, help_text="Enter a referrer(e.g. Doctor No, Dr. A, Google, Ad)")


        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Insurance(models.Model):
        """
        Model representing a insurance agency (Eg. AIG, None, Etc.)
        """
        name = models.CharField(max_length=50, help_text="Enter an Insurance / Health Plan")


        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Drug(models.Model):
        """
        Model representing a Drug
        """
        name = models.CharField(max_length=100, help_text="Enter a Drug name")

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Allergen(models.Model):
        """
        Model representing an Allergen
        """
        name = models.CharField(max_length=100, help_text="Enter an Allergen")

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Illness(models.Model):
        """
        Model representing an Illness
        """
        name = models.CharField(max_length=50, help_text="Enter an illness")

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Plan(models.Model):
        """
        Model representing a Meal Plan
        """
        name = models.CharField(max_length=50, help_text="Enter a Meal Plan (Eg. 2MR 2FM, 4MR, etc)")

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Exercise(models.Model):
        """
        Model representing an Exercise Plan
        """
        name = models.CharField(max_length=100, help_text="Enter an Exercise Plan (Eg. Resistance, HIIT,etc)")

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name

class Programtype(models.Model):
        """
        Model representing an Transform Program Eg. Transcend, Enlighten, Balance
        """
        name = models.CharField(max_length=100, help_text="Enter an Exercise Plan (Eg. Resistance, HIIT,etc)")

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name


class Branch(models.Model):
        """
        Model representing a transform branch office
        """
        name = models.CharField(max_length=150, help_text="Enter a branch office name", verbose_name="Branch Name")

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name


class Checklistitems(models.Model):
        """
        Model representing items in a check List
        """
        name = models.CharField(max_length=100, help_text="Enter a check list item (Eg. Initials, Medication, Vitamins)")

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            return self.name


class Initial(models.Model):
        """
        Model representing an Initial Visit
        """
        first_name = models.CharField(max_length=30, help_text="Enter an initial patient first name")
        last_name = models.CharField(max_length=50, blank=True, help_text="Enter an initial patient last name")
        middle_name = models.CharField(max_length=30, blank=True, help_text="Enter an initial patient middle name")
        date_of_birth = models.DateField()
        phone = models.CharField(max_length=100, help_text="Enter a mobile number")
        height = models.FloatField(blank=False,null=False, help_text="Enter height in inches")
        weight = models.FloatField(blank=False,null=False, help_text="Enter weight in pounds")
        bmi = models.FloatField(blank=False,null=False,verbose_name="BMI")
        date_initial = models.DateField(verbose_name="Date of Initial Visit",default=timezone.now)
        GENDER_TYPE = (
            ('m', 'Male'),
            ('f', 'Female'),
            ('o', 'Other'),
        )
        gender = models.CharField(max_length=1, choices=GENDER_TYPE, blank=True, default='f', help_text='Gender')

        bp_systolic_lie = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Systolic BP while lying down",verbose_name="BP Systolic - Lying Down")
        bp_diastolic_lie = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Diastolic BP while lying down", verbose_name="BP Diastolic - Lying Down")
        hr_lie = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Heart rate while lying down",verbose_name="Pulse - Lying Down")
        o2_lie = models.PositiveIntegerField(blank=False, null=False, help_text="Enter O2 while lying down",verbose_name="O2 - Lying Down")

        bp_systolic_sit = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Systolic BP while sitting",verbose_name="BP Systolic - Sitting")
        bp_diastolic_sit = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Diastolic BP while sitting",verbose_name="BP Diastolic - Sitting")
        hr_sit = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Heart rate while sitting",verbose_name="Pulse - Sitting")
        o2_sit = models.PositiveIntegerField(blank=False, null=False, help_text="Enter O2 while sitting",verbose_name="O2 - Sitting")

        bp_systolic_stand = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Systolic BP while standing",verbose_name="BP Systolic - Standing")
        bp_diastolic_stand = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Diastolic BP while standing",verbose_name="BP Diastolic - Standing")
        hr_stand = models.PositiveIntegerField(blank=False,null=False, help_text="Enter Heart rate while sitting",verbose_name="Pulse - Standing")
        o2_stand = models.PositiveIntegerField(blank=False, null=False, help_text="Enter O2 while sitting",verbose_name="O2 - Standing")

        referrer = models.ForeignKey(Referrer, on_delete=models.SET_NULL, null=True,help_text='Select a referrer for this patient')
        notes = models.TextField(blank=True, null=True)
        accepted = models.BooleanField(default=False)

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            # return self.name
            return "{0} {1} - dob: {2}".format(self.first_name,self.last_name, self.date_of_birth)

        def get_absolute_url(self):
            """
            Returns the url to access a detail record for this patient.
            """
            return reverse('patients:initial-details', args=[str(self.id)])

        def my_age(self):
            """
            Returns the age of the patient
            """
            today = date.today()
            my_year = self.date_of_birth.year
            my_month = self.date_of_birth.month
            my_day = self.date_of_birth.day
            # return (today - self.date_of_birth).years
            return today.year - my_year - ((today.month, my_day) < (my_month, my_day))



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    preferred_name = models.CharField(max_length=100, help_text="Enter a preferred name to use",verbose_name='Preferred Name')
    first_name = models.CharField(max_length=30, help_text="Enter patient first name",verbose_name='First Name')
    last_name = models.CharField(max_length=50, null=True,blank=True, help_text="Enter patient last name",verbose_name='Last Name')
    middle_name = models.CharField(max_length=30, null=True,blank=True, help_text="Enter patient middle name",verbose_name='Middle Name')
    date_of_birth = models.DateField(null=True, blank=True)
    date_join = models.DateField(null=True, blank=True, default=timezone.now,verbose_name='Date Joined')
    # date_of_birth = models.DateField()
    notes = models.TextField(blank=True, null=True, help_text='Enter any notes on patient here',verbose_name='Enter Notes')
    phone = models.CharField(max_length=100, help_text="Enter a mobile number",verbose_name='Mobile Number')
    height = models.FloatField(blank=True,null=True, help_text="Enter height in inches", verbose_name='Height in inches')
    insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, help_text='Select an insurance for this patient',verbose_name='Select Insurance',related_name='profile_insurance')
    initial = models.OneToOneField(Initial, on_delete=models.SET_NULL,help_text='Select an initial patient',blank=True, null=True,verbose_name="Select Initial Patient")
    # initial = models.ForeignKey(Initial, on_delete=models.SET_NULL, related_name='initial_name',null=True,blank=True)
    profile_pic = models.FileField(upload_to='profile_pics',blank=True,verbose_name="Profile Picture")

    GENDER_TYPE = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('o', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_TYPE, blank=True, default='f', help_text='Gender')
    ethnicity = models.ForeignKey(Ethnicity,on_delete=models.SET_NULL, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True, help_text='Enter Street Address')
    address2 = models.CharField(max_length=100, blank=True, null=True, help_text='Enter Additional Address Here')
    state = models.ForeignKey(State,on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country,on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch,on_delete=models.SET_NULL, null=True, verbose_name="Branch Name")
    program = models.ForeignKey(Programtype,on_delete=models.SET_NULL, null=True, verbose_name="Transform Program")
    appointment = models.DateTimeField(null=True,blank=True,verbose_name='Next Appointment',default=timezone.now)
    #smart_goals = models.TextField(blank=True, null=True, help_text='Enter smart goals here')
    #messages = models.TextField(blank=True, null=True, help_text='Enter any messages to patient here')
    #address

    class Meta:
        ordering = ["first_name"]
        permissions = (("can_view_records", "View Patient List"),)


    def __str__(self):
        return "{0} {1} : {2}".format(self.first_name,self.last_name,self.date_of_birth)

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this patient.
        """
        return reverse('patients:profile-details', args=[str(self.id)])

    def my_age(self):
        """
        Returns the age of the patient
        """
        today = date.today()
        my_year = self.date_of_birth.year
        my_month = self.date_of_birth.month
        my_day = self.date_of_birth.day
        # return (today - self.date_of_birth).years
        return today.year - my_year - ((today.month, my_day) < (my_month, my_day))

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# class UserProfileInfo(models.Model):
#
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='usr')
#
#     preferred_name = models.CharField(max_length=100, help_text="Enter a preferred name to use")
#     date_of_birth = models.DateField(null=True, blank=True)
#     # date_of_birth = models.DateField()
#     notes = models.TextField(blank=True, null=True, help_text='Enter any notes on patient here')
#     phone = models.CharField(max_length=100, help_text="Enter a mobile number")
#     height = models.FloatField(blank=False,null=False, help_text="Enter height in inches")
#     insurance = models.ManyToManyField(Insurance, help_text='Select an insurance for this patient')
#     initial = models.OneToOneField(Initial, on_delete=models.SET_NULL,help_text='Select an initial patient',blank=True, null=True,verbose_name="Select Initial Patient")
#     # initial = models.ForeignKey(Initial, on_delete=models.SET_NULL, related_name='initial_name',null=True,blank=True)
#     profile_pic = models.FileField(upload_to='profile_pics',blank=True,verbose_name="Profile Picture")
#
#     GENDER_TYPE = (
#         ('m', 'Male'),
#         ('f', 'Female'),
#         ('o', 'Other'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_TYPE, blank=True, default='f', help_text='Gender')
#     ethnicity = models.ForeignKey(Ethnicity,on_delete=models.SET_NULL, null=True)
#     address1 = models.CharField(max_length=100, blank=True, null=True, help_text='Enter Street Address')
#     address2 = models.CharField(max_length=100, blank=True, null=True, help_text='Enter Additional Address Here')
#     state = models.ForeignKey(State,on_delete=models.SET_NULL, null=True)
#     country = models.ForeignKey(Country,on_delete=models.SET_NULL, null=True)
#     branch = models.ForeignKey(Branch,on_delete=models.SET_NULL, null=True, verbose_name="Branch Name")
#
#     #smart_goals = models.TextField(blank=True, null=True, help_text='Enter smart goals here')
#     #messages = models.TextField(blank=True, null=True, help_text='Enter any messages to patient here')
#     #address
#
#     class Meta:
#         ordering = ["user"]
#         permissions = (("can_view_records", "View Patient List"),)
#
#
#     def __str__(self):
#         return "{0} {1} : {2}".format(self.user.first_name,self.user.last_name,self.date_of_birth)
#
#     def get_absolute_url(self):
#         """
#         Returns the url to access a detail record for this patient.
#         """
#         return reverse('patients:info-details', args=[str(self.id)])
#




# class Info(auth.models.User,auth.models.PermissionsMixin):
# # class Info(models.Model):
#
#     name = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='info_name',null=True,blank=True)
#     # name = models.OneToOneField(User, on_delete=models.SET_NULL,help_text='Select a user',null=True,blank=True)
#     preferred_name = models.CharField(max_length=100, help_text="Enter a preferred name to use")
#     date_of_birth = models.DateField(null=True, blank=True)
#     # date_of_birth = models.DateField()
#     notes = models.TextField(blank=True, null=True, help_text='Enter any notes on patient here')
#     phone = models.CharField(max_length=100, help_text="Enter a mobile number")
#     height = models.FloatField(blank=False,null=False, help_text="Enter height in inches")
#     insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL,null=True,help_text='Select an insurance for this patient')
#     initial = models.OneToOneField(Initial, on_delete=models.SET_NULL,help_text='Select an initial patient',blank=True, null=True,verbose_name="Select Initial Patient")
#     # initial = models.ForeignKey(Initial, on_delete=models.SET_NULL, related_name='initial_name',null=True,blank=True)
#     profile_pic = models.FileField(upload_to='profile_pics',blank=True,verbose_name="Profile Picture")
#
#     GENDER_TYPE = (
#         ('m', 'Male'),
#         ('f', 'Female'),
#         ('o', 'Other'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_TYPE, blank=True, default='f', help_text='Gender')
#     ethnicity = models.ForeignKey(Ethnicity,on_delete=models.SET_NULL, null=True)
#     address1 = models.CharField(max_length=100, blank=True, null=True, help_text='Enter Street Address')
#     address2 = models.CharField(max_length=100, blank=True, null=True, help_text='Enter Additional Address Here')
#     state = models.ForeignKey(State,on_delete=models.SET_NULL, null=True)
#     country = models.ForeignKey(Country,on_delete=models.SET_NULL, null=True)
#     branch = models.ForeignKey(Branch,on_delete=models.SET_NULL, null=True, verbose_name="Branch Name")
#
#     #smart_goals = models.TextField(blank=True, null=True, help_text='Enter smart goals here')
#     #messages = models.TextField(blank=True, null=True, help_text='Enter any messages to patient here')
#     #address
#
#     class Meta:
#         ordering = ["first_name"]
#         permissions = (("can_view_records", "View Patient List"),)
#
#
#     def __str__(self):
#         return "{0} {1} : {2}".format(self.first_name,self.last_name,self.date_of_birth)
#
#     def get_absolute_url(self):
#         """
#         Returns the url to access a detail record for this patient.
#         """
#         return reverse('patients:info-details', args=[str(self.id)])
#

class Biometric(models.Model):

    # user = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='biometrics',null=True,blank=True)
    # user = models.ForeignKey(Info, on_delete=models.SET_NULL,related_name='biometrics',null=True,blank=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL,related_name='biometrics',null=True,blank=True)
    height = models.FloatField(blank=False, help_text='Enter height in inches',null=True)
    weight = models.FloatField(blank=False, help_text='Enter weight in lbs',null=True)
    bmi = models.FloatField(blank=False, null=True,help_text='Enter BMI')
    neck_girth = models.FloatField(blank=True, null=True,help_text='Enter Neck Girth')
    inches_sn = models.FloatField(blank=True, null=True,help_text='Enter Inches from SN')
    umbilicus_girth = models.FloatField(blank=True, null=True,help_text='Enter Umbilicus Girth')
    hip_girth = models.FloatField(blank=True, null=True,help_text='Enter Hip Girth')
    inches_umbilicus = models.FloatField(blank=True, null=True,help_text='Enter Inches from Umbilicus')
    body_composition = models.FloatField(blank=True, null=True,help_text='Enter Body Composition')
    body_fat = models.IntegerField(blank=True, null=True, help_text='Enter % Body Fat')
    vat = models.FloatField(blank=True, null=True,help_text='Enter VAT',verbose_name="VAT")
    lean_mass = models.FloatField(blank=True, null=True,help_text='Enter Lean Mass')
    bp_systolic = models.PositiveIntegerField(blank=False,null=True,help_text='Enter BP(Systolic)',verbose_name="BP Systolic")
    bp_diastolic = models.PositiveIntegerField(blank=False, null=True,help_text='Enter BP(Diastolic)',verbose_name="BP Diastolic")
    pulse = models.PositiveIntegerField(blank=False,null=True,help_text='Enter Pulse Rate')
    o2 = models.PositiveIntegerField(blank=False,null=True, help_text='Enter O2')

    image_bodyscan = models.FileField(null=True,blank=True)
    image_front = models.FileField(null=True,blank=True)
    image_side = models.FileField(null=True,blank=True)


    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True,verbose_name="Select Day")

    date_biometric = models.DateTimeField(null=True, blank=True,verbose_name="Date of Biometric",default=timezone.now)

    BIO_STATUS = (
        ('u', 'Underweight'),
        ('n', 'Normal'),
        ('o', 'Overweight'),
        ('x', 'Obesity I'),
        ('y', 'Obesity II'),
        ('z', 'Obesity III'),
    )

    status = models.CharField(max_length=1, choices=BIO_STATUS, blank=True, default='o', help_text='Risk Level')

    def __str__(self):
        return "{0} ({1}lbs) [{2}]".format(self.user,self.weight,self.date_biometric)

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this patient.
        """
        return reverse('patients:biometric-details', args=[str(self.id)])

class Checklist(models.Model):
        """
        Model representing a check List
        """
        # name = models.ForeignKey(Info, on_delete=models.SET_NULL,related_name='checklist_name',null=True,blank=True)
        name = models.ForeignKey(Profile, on_delete=models.SET_NULL,related_name='checklist_name',null=True,blank=True)
        # checklist = models.ManyToManyField(Checklistitems, help_text='Select a check list item(s) for this patient')
        weight = models.BooleanField(default=False, verbose_name='Weigh In')
        dexa = models.BooleanField(default=False, verbose_name='Dexa')
        conditions = models.BooleanField(default=False, verbose_name='Ask about any pre-existing conditions')
        allergies = models.BooleanField(default=False,verbose_name='Ask about Allergies')
        medications = models.BooleanField(default=False, verbose_name='Ask about current Medications')
        supplements = models.BooleanField(default=False,verbose_name='Ask about current vitamin/mineral supplementation')
        logging = models.BooleanField(default=False,verbose_name='Discuss Importance of Logging')
        date_checklist = models.DateField(default=timezone.now,verbose_name='Date of Checklist')

        def __str__(self):
            """
            String for representing the Model object (in Admin site etc.)
            """
            # return self.name
            return "{0} : ".format(self.name)

        def get_absolute_url(self):
            """
            Returns the url to access a detail record for this patient.
            """
            return reverse('patients:checklist-details', args=[str(self.id)])

class Lab(models.Model):
    """
    Model representing a specific lab
    """
    # user = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='labs',null=True,blank=True)
    # user = models.ForeignKey(Info, on_delete=models.SET_NULL,related_name='labs',null=True,blank=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL,related_name='labs',null=True,blank=True)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL,null=True,help_text='Select a test for this patient',verbose_name='Select Test')
    value = models.CharField(max_length=100,blank=True, null=True, help_text='Enter test result',verbose_name='Test Result')
    date_lab = models.DateTimeField(null=True, blank=True,default=timezone.now,verbose_name='Date of Lab')


    @property
    def is_overdue(self):
        if self.date_lab and  date.today() > self.date_lab:
            return True
        return False

    class Meta:
        ordering = ["date_lab"]
        permissions = (("can_mark_checked", "Set lab as checked"),)


    def __str__(self):
        """
        String for representing the Model object
        """
    #    return '{0} ({1})'.format(self.id,self.book.title)

        return 'Name:{0} Date:{1} Test:{2} Value:{3}'.format(self.user,self.date_lab, self.test, self.value)


class Medication(models.Model):

    user = models.ForeignKey(Initial, on_delete=models.SET_NULL,related_name='medications',null=True,blank=True)
    drug = models.ForeignKey(Drug, on_delete=models.SET_NULL,null=True,help_text='Select a drug for this patient',verbose_name='Select Drug')
    dose = models.FloatField(blank=False, help_text='Enter dosage',null=True,verbose_name='Dosage')
    frequency = models.PositiveIntegerField(blank=False, null=True,help_text='Enter frequency of medication use per day',verbose_name='Frequency of use per day')
    date_start = models.DateField(blank=True,null=True,help_text='Enter date medication started',verbose_name='Date Medication Started')
    date_end = models.DateField(blank=True,null=True,help_text='Enter date medication discontinued',verbose_name='Date Medication Ended')

    date_medication = models.DateField(default=timezone.now,verbose_name='Med Record Date')

    def __str__(self):
        return "{0} : {1} - date| {2})".format(self.drug,self.user, self.date_medication)




class Allergy(models.Model):

    user = models.ForeignKey(Initial, on_delete=models.SET_NULL,related_name='allergies',null=True,blank=True)
    allergen = models.ForeignKey(Allergen, on_delete=models.SET_NULL, null=True,help_text='Select an Allergen for this patient',verbose_name='Select Allergen')
    date_allergy = models.DateField(default=timezone.now,verbose_name='Date of Record')
    notes = models.TextField(blank=True,null=True)

    def __str__(self):
        return "{0} : {1} - date| {2})".format(self.allergen,self.user, self.date_allergy)




class Diagnose(models.Model):

    user = models.ForeignKey(Initial, on_delete=models.SET_NULL,related_name='diagnoses',null=True,blank=True)
    illness = models.ForeignKey(Illness, on_delete=models.SET_NULL,null=True,help_text='Select an illness for this patient',verbose_name='Select Illness')
    date_diagnose = models.DateField(null=True,blank=True, verbose_name='Date of Diagnosis', default=timezone.now)
    notes = models.TextField(blank=True,null=True,verbose_name='Notes')

    def __str__(self):
        return "{0} : {1} - date| {2})".format(self.user,self.illness, self.date_diagnose)



class Meal(models.Model):

    # user = models.ForeignKey(Info, on_delete=models.SET_NULL,related_name='meals',null=True,blank=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL,related_name='meals',null=True,blank=True)
    plan = models.ForeignKey(Plan,on_delete=models.SET_NULL, null=True,verbose_name='Select Meal Plan')
    date_meal = models.DateField(default=timezone.now,verbose_name='Date of Meal Plan')

    def __str__(self):
        return "{0} : {1} - plan| {2})".format(self.user,self.date_meal, self.plan)



class Week(models.Model):

    # user = models.ForeignKey(Info, on_delete=models.SET_NULL,related_name='weeks',null=True,blank=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL,related_name='weeks',null=True,blank=True)
    number = models.PositiveIntegerField(default=0,null=True,blank=True,help_text='Enter Week Number',verbose_name="Week Number")
    weight = models.FloatField(blank=True,null=True,help_text='Enter weight in lbs')
    delta = models.FloatField(blank=True, null=True, help_text='Enter weekly weight change (Delta)',verbose_name='Delta Weight Change')
    sigma = models.FloatField(blank=True, null=True, help_text='Enter total weight change (Sigma)',verbose_name='Total Weight Change')
    bp_systolic = models.PositiveIntegerField(blank=True, null=True, help_text='Enter Systolic Blood Pressure',verbose_name='BP Systolic')
    bp_diastolic = models.PositiveIntegerField(blank=True, null=True, help_text='Enter Diastolic Blood Pressure',verbose_name='BP Diastolic')
    pulse = models.PositiveIntegerField(blank=True, null=True, help_text='Enter Pulse',verbose_name='Pulse Rate')
    o2 = models.PositiveIntegerField(blank=True, null=True, help_text='Enter O2',verbose_name='O2')
    date_menstruation = models.DateField(blank=True, null=True, help_text='Enter last menstruation if applicable',verbose_name='Last Menstruation (if applicable)')
    date_week = models.DateField(default=timezone.now,verbose_name='Date of Record')

    eating_off = models.BooleanField(default=False, help_text='Eating off?',verbose_name='Eating Off?')
    eating_off_notes = models.CharField(max_length=100,verbose_name="Notes on Eating Off",blank=True,null=True)
    broth = models.PositiveIntegerField(blank=True, null=True, help_text='Enter number of broths per day',verbose_name='Broths per day')
    fluid = models.FloatField(blank=True, null=True, help_text='Enter fluid ounces per day',verbose_name='Fluid Ounces per day')
    constipation = models.BooleanField(default=False, help_text='Constipation?',verbose_name='Constipation?')
    constipation_notes = models.CharField(max_length=100,verbose_name="Notes on Constipation",blank=True,null=True)
    diarrhea = models.BooleanField(default=False, help_text='Diarrhea?',verbose_name='Diarrhea?')
    diarrhea_notes = models.CharField(max_length=100,verbose_name="Notes on Diarrhea",blank=True,null=True)
    ab_discomfort = models.BooleanField(default=False, help_text='Ab Discomfort?',verbose_name='Abdominal Discomfort?')
    ab_discomfort_notes = models.CharField(max_length=100,verbose_name="Notes on Ab Discomfort",blank=True,null=True)
    gas_bloating = models.BooleanField(default=False, help_text='Gas/Bloating?',verbose_name='Gas/Bloating?')
    gas_bloating_notes = models.CharField(max_length=100,verbose_name="Notes on Gas/Bloating",blank=True,null=True)
    nausea = models.BooleanField(default=False, help_text='Nausea?',verbose_name='Nausea?')
    nausea_notes = models.CharField(max_length=100,verbose_name="Notes on Nausea",blank=True,null=True)
    vomiting = models.BooleanField(default=False, help_text='Vomiting?',verbose_name='Vomiting?')
    vomiting_notes = models.CharField(max_length=100,verbose_name="Notes on Vomiting",blank=True,null=True)
    dizziness = models.BooleanField(default=False, help_text='Dizziness?',verbose_name='Dizziness?')
    dizziness_notes = models.CharField(max_length=100,verbose_name="Notes on Dizziness",blank=True,null=True)
    headache = models.BooleanField(default=False, help_text='Headache?',verbose_name='Headache?')
    headache_notes = models.CharField(max_length=100,verbose_name="Notes on Headache",blank=True,null=True)

    QUALITY = (
        ('3', 'Excellent'),
        ('2', 'Good'),
        ('1', 'Fair'),
        ('0', 'Poor'),
    )
    sleep = models.CharField(max_length=1, choices=QUALITY, blank=True, default='g', help_text='Choose Sleep Quality',verbose_name='Select Sleep Quality')

    LEVEL = (
        ('3', 'High'),
        ('2', 'Medium'),
        ('1', 'Mild'),
        ('0', 'None'),
    )
    stress = models.CharField(max_length=1, choices=LEVEL, blank=True, default='m', help_text='Choose Stress Level',verbose_name='Stress Level')
    fatigue = models.BooleanField(default=False, help_text='New Fatigue?')
    fatigue_notes = models.CharField(max_length=100,verbose_name="Notes on Fatigue",blank=True,null=True)
    medication = models.BooleanField(default=False, help_text='Change in medication?(if yes, use med list)',verbose_name='Change in medication?')
    steps = models.PositiveIntegerField(blank=True, null=True, help_text='Enter number of steps',verbose_name='Number of Steps')
    exercise = models.ForeignKey(Exercise, on_delete=models.SET_NULL,null=True,help_text='Select exercise for this patient',verbose_name='Exercises for patient')
    concerns = models.TextField(blank=True,null=True, help_text='Enter any concerns',verbose_name='Enter any Concerns')
    commentary = models.TextField(blank=True,null=True, help_text='Commentaries/Orders',verbose_name='Commentaries/Orders')

    def __str__(self):
        return "{0} : week| - {1} - date| {2})".format(self.user,self.number, self.date_week)

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this patient.
        """
        return reverse('patients:week-detail', args=[str(self.id)])
