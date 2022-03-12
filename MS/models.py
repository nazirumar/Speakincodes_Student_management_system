
from django import forms
from django.db import models
from django.forms import ModelForm, TextInput, EmailInput

# Create your models here.
from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User  
  
class SignupForm(UserCreationForm):  
    email = forms.EmailField(max_length=200)  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2') 
      

origin=(
(('Abia'),'Abia'), 
(('Adamawa'), 'Adamawa'),
 (('Akwa-Ibom'),'Akwa-Ibom'),
 (( 'Anambra'),  'Anambra'), 
((  'Bauchi'),'Bauchi'), 
 (( 'Bayelsa'),  'Bayelsa'), 
 (('Benue'),  'Benue'), 
 (( 'Borno'), 'Borno'),
  ( ('Cross-river'), 'cross-river'),
 ( (  'Delta'),    'Delta'), 
  ((  'Ebonyi'),   'Ebonyi'),
((     'Edo'),'Edo'),
 (  (   'Ekiti'),    'Ekiti'),
    ((   'Enugu'),    'Enugu'), 
    ((   'Gombe'),    'Gombe'),
   ((     'Imo'),      'Imo'),
    (  (  'Jigawa'),   'Jigawa'),
       ((  'Kaduna'),   'Kaduna'),
      ((    'Kano'),     'Kano'), 
        ( ( 'Katsina'),  'Katsina'), 
       ((   'Kebbi'),    'Kebbi'),
       ( (   'Kogi'),     'Kogi'), 
        ((   'Kwara'),    'Kwara'),
         ((   'Lagos'),    'Lagos'),
            ( ('Nasarawa'), 'Nasarawa'),
           ( (  'Niger'),    'Niger'), 
          (   ( 'Ogun'),     'Ogun'),
           (   ( 'Ondo'),     'Ondo'),
            (   ( 'Osun'),     'Osun'), 
           (     ('Oyo'),      'Oyo'),
                ( ('Plateau'),  'Plateau'),
                (  ('Rivers'),   'Rivers'),
                 (  ('Sokoto'),   'Sokoto'),
                  (  ('Taraba'),   'Taraba'),
                 (    ('Yobe'),     'Yobe'),
                     ( ('Zamfara'),  'Zamfara'),
                    (   ('Abuja'),    'Abuja'),
                       )
    





class OLevel(models.Model):
    Nschool=models.CharField(max_length=100)
    Exnumber =models.CharField(max_length=200)
    Extype=models.CharField(max_length=10)
    Year=models.PositiveIntegerField()






gender =(
    (('1'), 'Male'),
    (('2'), 'FeMale'),

)


class BioUpdate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="new_spending", null=True)   
    origin=models.CharField(max_length=100, choices=origin, default='FCT')
    localGov=models.CharField(max_length=100, choices=gender)
    gender=models.CharField(max_length=10, choices=gender, default='male')
    Date= models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    img = models.ImageField(upload_to = "Profile/")

    def __str__(self):
        return self.origin

class O_Level(models.Model):
    exam_type =(
      ('CSE',  'CSE'),
      ( 'WAEC', 'WAEC'),
     ('NECO',   'NECO'),
      ( 'NABT',   'NABT'),
     ('TCII',  'TCII'),
     ('NSE',   'NSE'),
      ('TTC',      'TTC'),
      ('SISC',     'SISC')
      )
       


    SUBJECT=(
  ("AGRICULTURE","AGRICULTURE"),
	 ("ANIMAL HUSBANDRY","ANIMAL HUSBANDRY"),
	 ("ACCOUNTING","ACCOUNTING"),
      ("APPLIED ELECTRICITY","APPLIED ELECTRICITY"),
	 ("ARABIC","ARABIC"),
	 ("AUTO MECHANICS","AUTO MECHANICS"),
	 ("BASIC ELECTRICITY","BASIC ELECTRICITY"),
	 ("BIOLOGY","BIOLOGY"),
	 ("BOOK KEEPING","BOOK KEEPING"),
	 ("BUILDING/ENGINEERING DRAWING","BUILDING/ENGINEERING DRAWING"),
	 ("CARPENTRY &amp; JOINERY","CARPENTRY &amp; JOINERY"),
	 ("CATERING CRAFT","CATERING CRAFT"),
	 ("CHEMISTRY","CHEMISTRY"),
	 ("CHRISTIAN RELIGIOUS KNOWLEDGE","CHRISTIAN RELIGIOUS KNOWLEDGE"),
	 ("CIVIC EDUCATION","CIVIC EDUCATION"),
	 ("CLOTHING AND TEXTILE","CLOTHING AND TEXTILE"),
 ("	COMMERCE","COMMERCE"),
	 ("COMMUNICATION SKILLS","COMMUNICATION SKILLS"),
	 ("COMPUTER SCIENCE","COMPUTER SCIENCE"),
	 ("COMPUTER SCIENCE TYPING","COMPUTER SCIENCE TYPING"),
	 ("COMPUTER STUDIES","COMPUTER STUDIES"),
	 ("DATA PROCESSING","DATA PROCESSING"),
	 ("ECONOMICS","ECONOMICS"),
	 ("ELECTRICAL INSTALLATION &amp; MAINT. WORKS","ELECTRICAL INSTALLATION &amp; MAINT. WORKS"),
	 ("ELECTRONICS WORKS","ELECTRONICS WORKS"),
	 ("ENGLISH LANGUAGE","ENGLISH LANGUAGE"),
	 ("FABRICATION &amp; WELDING","FABRICATION &amp; WELDING"),
	 ("FINANCIAL ACCOUNTING","FINANCIAL ACCOUNTING"),
	 ("FISHERY","FISHERY"),
	 ("FOOD AND NUTRITION","FOOD AND NUTRITION"),
	 ("FRENCH","FRENCH"),
	 ("FURTHER MATHEMATICS","FURTHER MATHEMATICS"),
	 ("GEOGRAPHY","GEOGRAPHY"),
	 ("GOVERNMENT","GOVERNMENT"),
 ("	HAUSA LANGUAGE","HAUSA LANGUAGE"),
	 ("HISTORY","HISTORY"),
 ("	HOME MANAGEMENT","HOME MANAGEMENT"),
 ("	IGBO LANGUAGE","IGBO LANGUAGE"),
	 ("INFORMATION &amp; COMMUNICATIONS TECHNOLOGY","INFORMATION &amp; COMMUNICATIONS TECHNOLOGY"),
	 ("ISLAMIC HISTORY","ISLAMIC HISTORY"),
	 ("ISLAMIC RELIGIOUS KNOWLEDGE","ISLAMIC RELIGIOUS KNOWLEDGE"),
	 ("LITERATURE-IN ENGLISH","LITERATURE-IN ENGLISH"),
 ("	MARKETING","MARKETING"),
 ("	MATHEMATICS","MATHEMATICS"),
	 ("METAL WORK","METAL WORK"),
	 ("MOTOR VEHICLE MECHANICS WORKS","MOTOR VEHICLE MECHANICS WORKS"),
 ("	MUSIC","MUSIC"),
	 ("OFFICE PRACTICE","OFFICE PRACTICE"),
	 ("OFFICE ROUTINE &amp; GOVT. REGULATION","OFFICE ROUTINE &amp; GOVT. REGULATION"),
 ("	ONE MAJOR NIGERIAN LANGUAGE","ONE MAJOR NIGERIAN LANGUAGE"),
 ("	PHYSICAL EDUCATION","PHYSICAL EDUCATION"),
 ("	PHYSICS","PHYSICS"),
 ("	SOCIAL STUDIES","SOCIAL STUDIES"),
 ("	TECHNICAL DRAWING","TECHNICAL DRAWING"),
 ("	TYPEWRITING ","TYPEWRITING "),
 ("	VISUAL","VISUAL"),
 ("	WOOD WORK","WOOD WORK"),
 ("	YORUBA LANGUAGE","YORUBA LANGUAGE"),
    )

    grade=(
        ("A","A"),
      ("B","B"),
        ("C","C"), 
          ("D","D"), 
      ("E","E"), 
      ("F","F"),
      ("P","P"),)
    Name_School =models.CharField(max_length=100)
    Examination_No=models.CharField(max_length=100)
    Examination_type=models.CharField( max_length=100, choices=exam_type)
    Year =models.CharField(max_length=100)
    Subject =models.CharField(max_length=100, choices=SUBJECT)
    grade =models.CharField(max_length=100, choices=grade)



class Pincode(models.Model):
  pincode= models.CharField(max_length=100)
  serialNumber= models.CharField(max_length=100)