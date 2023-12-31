from django.shortcuts import render, redirect, get_object_or_404
from poll.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question,Choice,Patient
import csv
from datetime import datetime


def index(request):
    return render(request,'poll/index.html')

@login_required
def special(request):
    return HttpResponse("you are logged in , nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'poll/registration.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request,'poll/login.html',{})



@login_required
def questions(request):

    all_questions = Question.objects.all()
    context = {
        'questions': all_questions
    }

    return render(request, 'poll/questions.html', context)


def submit_answers(request):

    if request.method == 'POST':
        print("aaaaaaaaa")
        IDENTITY = request.POST.get(f'IDENTITY')
        EDUCCATEGORY = request.POST.get(f'EDUCCATEGORY')
        EDUCPATIENT = request.POST.get(f'EDUCPATIENT')
        SEXPATIENT = request.POST.get(f'SEXPATIENT')
        AGEPATIENT = request.POST.get(f'AGEPATIENT')
        ECUCCARERCAT = request.POST.get(f'ECUCCARERCAT')
        EDUCCARER = request.POST.get(f'EDUCCARER')
        SEXCARER = request.POST.get(f'SEXCARER')
        AGECARER = request.POST.get(f'AGECARER')
        RELATIONSHIPCARER = request.POST.get(f'RELATIONSHIPCARER')
        LIVESIN = request.POST.get(f'LIVESIN')
        kentro = request.POST.get(f'kentro')
        date = request.POST.get(f'date')
        NPI = request.POST.get(f'NPI')
        STAGE = request.POST.get(f'STAGE')
        IADL = request.POST.get(f'IADL')
        MMSE = request.POST.get(f'MMSE')

        patient = Patient(
        DOCTOR = request.user,
        IDENTITY = IDENTITY,
        EDUCCATEGORY = EDUCCATEGORY,
        EDUCPATIENT = EDUCPATIENT,
        SEXPATIENT = SEXPATIENT,
        AGEPATIENT = AGEPATIENT,
        ECUCCARERCAT = ECUCCARERCAT,
        EDUCCARER = EDUCCARER,
        SEXCARER = SEXCARER,
        AGECARER = AGECARER,
        RELATIONSHIPCARER = RELATIONSHIPCARER,
        LIVESIN = LIVESIN,
        kentro = kentro,
        date = date,
        NPI	= NPI,
        STAGE = STAGE,
        IADL = IADL,
        MMSE = MMSE,
        )
        patient.save()

        #doctor=request.user
        #patients = Patient.objects.filter(DOCTOR=doctor)


        questions = Question.objects.all()
        #Choice.objects.filter(user=request.user).delete()

        for question in questions:
            first_answer = request.POST.get(f'first_answer_{question.id}')
            second_answer = request.POST.get(f'second_answer_{question.id}')
            notes = request.POST.get(f'notes_{question.id}')  # Λάβετε την απάντηση για κάθε ερώτηση
            #print(first_answer)
            #print(question.id)



            if first_answer:
                choice = Choice(
                    question=question,
                    user=request.user,
                    patient=patient,
                    first_answer=first_answer,
                    second_answer=second_answer,
                    notes=notes
                )
                choice.save()
                print('saved')

        #return redirect('questions')  # Μεταφορά του χρήστη πίσω στη σελίδα ερωτήσεων

    return render(request, 'poll/submit_answers.html')



@login_required
def user_answers(request):
    user_choices = Choice.objects.filter(user=request.user)

    context = {
        'user_choices': user_choices
    }

    return render(request, 'poll/user_answers.html', context)


def create_patient(request):
    print("bhkame")
    if request.method == 'POST':
        print('einai post')
        IDENTITY = request.POST.get(f'IDENTITY')
        EDUCCATEGORY = request.POST.get(f'EDUCCATEGORY')
        EDUCPATIENT = request.POST.get(f'EDUCPATIENT')
        SEXPATIENT = request.POST.get(f'SEXPATIENT')
        AGEPATIENT = request.POST.get(f'AGEPATIENT')
        ECUCCARERCAT = request.POST.get(f'ECUCCARERCAT')
        EDUCCARER = request.POST.get(f'EDUCCARER')
        SEXCARER = request.POST.get(f'SEXCARER')
        AGECARER = request.POST.get(f'AGECARER')
        RELATIONSHIPCARER = request.POST.get(f'RELATIONSHIPCARER')
        LIVESIN = request.POST.get(f'LIVESIN')
        kentro = request.POST.get(f'kentro')
        date = request.POST.get('date')
        NPI = request.POST.get(f'NPI')
        STAGE = request.POST.get(f'STAGE')
        IADL = request.POST.get(f'IADL')
        MMSE = request.POST.get(f'MMSE')

        patient = Patient(
        IDENTITY = IDENTITY,
        EDUCCATEGORY = EDUCCATEGORY,
        EDUCPATIENT = EDUCPATIENT,
        SEXPATIENT = SEXPATIENT,
        AGEPATIENT = AGEPATIENT,
        ECUCCARERCAT = ECUCCARERCAT,
        EDUCCARER = EDUCCARER,
        SEXCARER = SEXCARER,
        AGECARER = AGECARER,
        RELATIONSHIPCARER = RELATIONSHIPCARER,
        LIVESIN = LIVESIN,
        kentro = kentro,
        date = date,
        NPI	= NPI,
        STAGE = STAGE,
        IADL = IADL,
        MMSE = MMSE,
        )
        patient.save()

        print('success save')

        all_questions = Question.objects.all()
        context = {
            'questions': all_questions
        }

        return render(request, 'poll/questions.html', context)


    return render(request, 'poll/patient.html')

@login_required
def saved_patients(request):
    all_patients = Patient.objects.filter(DOCTOR=request.user)
    context = {
        'patients': all_patients
    }

    return render(request, 'poll/saved_patients.html', context)


def patient_choices(request):
    patient_id = request.GET.get('id', None)

    if patient_id is not None:
        try:
            patient = Patient.objects.get(id=patient_id)
            patient_choices = Choice.objects.filter(patient=patient)

            context = {
                'patient': patient,
                'patient_choices': patient_choices
            }

            return render(request, 'poll/patient_choices.html', context)
        except Patient.DoesNotExist:
            # Εάν ο ασθενής δεν βρεθεί, μπορείτε να χειριστείτε το λάθος εδώ.
            return render(request, 'poll/saved_patients.html')

    return render(request, 'poll/patient_choices.html')



def del_patient(request):
    patient_id = request.GET.get('id', None)

    if patient_id is not None:
        patient = Patient.objects.get(id=patient_id)
        patient_choices = Choice.objects.filter(patient=patient)

        patient.delete()
        patient_choices.delete()

        all_patients = Patient.objects.filter(DOCTOR=request.user)
        context = {
            'patients': all_patients
        }

        return render(request, 'poll/saved_patients.html', context)

    return render(request, 'poll/saved_patients.html')






def demo(request):
    return render(request,'poll/demo.html')


def search_patients(request):
    search_query = request.GET.get('IDENTITY', '')
    patients = Patient.objects.filter(IDENTITY=search_query)

    return render(request, 'poll/saved_patients.html',{'patients':patients})





def download_patient_choices_csv(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    patient_choices = Choice.objects.filter(patient=patient)

    # Ορίζουμε το όνομα του αρχείου CSV
    csv_filename = f'patient_{patient.id}_choices.csv'

    # Δημιουργία αρχείου CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{csv_filename}"'

    # Δημιουργία του writer για την εγγραφή στο αρχείο CSV
    csv_writer = csv.writer(response)
    csv_writer.writerow(['Question', 'First Answer', 'Second Answer', 'Notes'])

    # Εγγραφή των δεδομένων του ασθενούς και των επιλογών του στο αρχείο CSV
    for choice in patient_choices:

        csv_writer.writerow([
            choice.question.question_text[:3],
            choice.first_answer,
            choice.second_answer,
            choice.notes,
        ])

    return response

def download_all(request):
    patients = Patient.objects.filter(DOCTOR=request.user)


    csv_filename = 'all_patients'

    responce = HttpResponse(content_type='text/csv')
    responce['Content-Disposition'] = f'attachment; filename="{csv_filename}"'

    csv_writer = csv.writer(responce)
    header_row = ['Identity',
    'Category of Education',
    'Education of Patient',
    'Sex of Patient',
    'Age of Patient',
    'Carer category of education',
    'Education of Carer',
    'Sex of Carer',
    'Age of Carer',
    'Relationship between patient and caregiver',
    'LIVES IN',
    'kentro',
    'date',
    'NPI',
    'STAGE',
    'IADL',
    'MMSE']

    questions = Question.objects.all()
    for q in questions:
        header_row.extend([f'{q.question_text[:3]} - First Answer', f'- Second Answer', f'- Notes'])
    csv_writer.writerow(header_row)



    for patient in patients:
        patient_choices = Choice.objects.filter(patient=patient)

        row = [patient.IDENTITY,
        patient.EDUCCATEGORY,
        patient.EDUCPATIENT,
        patient.SEXPATIENT,
        patient.AGEPATIENT,
        patient.ECUCCARERCAT,
        patient.EDUCCARER,
        patient.SEXCARER,
        patient.AGECARER,
        patient.RELATIONSHIPCARER,
        patient.LIVESIN,
        patient.kentro,
        patient.date,
        patient.NPI,
        patient.STAGE,
        patient.IADL,
        patient.MMSE]

        for q in questions:
            choice = patient_choices.filter(question=q).first()
            if choice:
                row.extend([choice.first_answer, choice.second_answer, choice.notes])
            else:
                row.extend(['', '', ''])
        csv_writer.writerow(row)


    return responce
