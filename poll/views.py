from django.shortcuts import render, redirect
from poll.forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Question,Choice,Patient


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

        questions = Question.objects.all()
        Choice.objects.filter(user=request.user).delete()

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


def saved_patients(request):
    all_patients = Patient.objects.all()
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
            return render(request, 'poll/patient_not_found.html')

    return render(request, 'poll/patient_choices.html')
