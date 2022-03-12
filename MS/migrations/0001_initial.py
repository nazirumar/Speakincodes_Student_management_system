# Generated by Django 3.2.12 on 2022-03-06 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BioUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('1', 'Male'), ('2', 'FeMale')], default='male', max_length=10)),
                ('Date', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('img', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='O_Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_School', models.CharField(max_length=100)),
                ('Examination_No', models.CharField(max_length=100)),
                ('Examination_type', models.CharField(choices=[('CSE', 'CSE'), ('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABT', 'NABT'), ('TCII', 'TCII'), ('NSE', 'NSE'), ('TTC', 'TTC'), ('SISC', 'SISC')], max_length=100)),
                ('Year', models.CharField(max_length=100)),
                ('Subject', models.CharField(choices=[('AGRICULTURE', 'AGRICULTURE'), ('ANIMAL HUSBANDRY', 'ANIMAL HUSBANDRY'), ('ACCOUNTING', 'ACCOUNTING'), ('APPLIED ELECTRICITY', 'APPLIED ELECTRICITY'), ('ARABIC', 'ARABIC'), ('AUTO MECHANICS', 'AUTO MECHANICS'), ('BASIC ELECTRICITY', 'BASIC ELECTRICITY'), ('BIOLOGY', 'BIOLOGY'), ('BOOK KEEPING', 'BOOK KEEPING'), ('BUILDING/ENGINEERING DRAWING', 'BUILDING/ENGINEERING DRAWING'), ('CARPENTRY &amp; JOINERY', 'CARPENTRY &amp; JOINERY'), ('CATERING CRAFT', 'CATERING CRAFT'), ('CHEMISTRY', 'CHEMISTRY'), ('CHRISTIAN RELIGIOUS KNOWLEDGE', 'CHRISTIAN RELIGIOUS KNOWLEDGE'), ('CIVIC EDUCATION', 'CIVIC EDUCATION'), ('CLOTHING AND TEXTILE', 'CLOTHING AND TEXTILE'), ('\tCOMMERCE', 'COMMERCE'), ('COMMUNICATION SKILLS', 'COMMUNICATION SKILLS'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'), ('COMPUTER SCIENCE TYPING', 'COMPUTER SCIENCE TYPING'), ('COMPUTER STUDIES', 'COMPUTER STUDIES'), ('DATA PROCESSING', 'DATA PROCESSING'), ('ECONOMICS', 'ECONOMICS'), ('ELECTRICAL INSTALLATION &amp; MAINT. WORKS', 'ELECTRICAL INSTALLATION &amp; MAINT. WORKS'), ('ELECTRONICS WORKS', 'ELECTRONICS WORKS'), ('ENGLISH LANGUAGE', 'ENGLISH LANGUAGE'), ('FABRICATION &amp; WELDING', 'FABRICATION &amp; WELDING'), ('FINANCIAL ACCOUNTING', 'FINANCIAL ACCOUNTING'), ('FISHERY', 'FISHERY'), ('FOOD AND NUTRITION', 'FOOD AND NUTRITION'), ('FRENCH', 'FRENCH'), ('FURTHER MATHEMATICS', 'FURTHER MATHEMATICS'), ('GEOGRAPHY', 'GEOGRAPHY'), ('GOVERNMENT', 'GOVERNMENT'), ('\tHAUSA LANGUAGE', 'HAUSA LANGUAGE'), ('HISTORY', 'HISTORY'), ('\tHOME MANAGEMENT', 'HOME MANAGEMENT'), ('\tIGBO LANGUAGE', 'IGBO LANGUAGE'), ('INFORMATION &amp; COMMUNICATIONS TECHNOLOGY', 'INFORMATION &amp; COMMUNICATIONS TECHNOLOGY'), ('ISLAMIC HISTORY', 'ISLAMIC HISTORY'), ('ISLAMIC RELIGIOUS KNOWLEDGE', 'ISLAMIC RELIGIOUS KNOWLEDGE'), ('LITERATURE-IN ENGLISH', 'LITERATURE-IN ENGLISH'), ('\tMARKETING', 'MARKETING'), ('\tMATHEMATICS', 'MATHEMATICS'), ('METAL WORK', 'METAL WORK'), ('MOTOR VEHICLE MECHANICS WORKS', 'MOTOR VEHICLE MECHANICS WORKS'), ('\tMUSIC', 'MUSIC'), ('OFFICE PRACTICE', 'OFFICE PRACTICE'), ('OFFICE ROUTINE &amp; GOVT. REGULATION', 'OFFICE ROUTINE &amp; GOVT. REGULATION'), ('\tONE MAJOR NIGERIAN LANGUAGE', 'ONE MAJOR NIGERIAN LANGUAGE'), ('\tPHYSICAL EDUCATION', 'PHYSICAL EDUCATION'), ('\tPHYSICS', 'PHYSICS'), ('\tSOCIAL STUDIES', 'SOCIAL STUDIES'), ('\tTECHNICAL DRAWING', 'TECHNICAL DRAWING'), ('\tTYPEWRITING ', 'TYPEWRITING '), ('\tVISUAL', 'VISUAL'), ('\tWOOD WORK', 'WOOD WORK'), ('\tYORUBA LANGUAGE', 'YORUBA LANGUAGE')], max_length=100)),
                ('grade', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('P', 'P')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nschool', models.CharField(max_length=100)),
                ('Exnumber', models.CharField(max_length=200)),
                ('Extype', models.CharField(max_length=10)),
                ('Year', models.PositiveIntegerField()),
            ],
        ),
    ]