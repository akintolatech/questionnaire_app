from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Teacher, Question, Response, Participant, QuestionCategory

def app_landing(request):
    return render(request, "questionnaire/landing.html")

def success(request):
    return render(request, "questionnaire/success.html")

def questionnaire_view(request):
    teachers = Teacher.objects.all()
    questions = Question.objects.all()
    categories = QuestionCategory.objects.all()
    participants = Participant.objects.all()

    if request.method == "POST":
        participant_name = request.POST.get("participant_name")
        participant_phone = request.POST.get("participant_phone")

        if participant_name and participant_phone:
            participant, created = Participant.objects.get_or_create(
                name=participant_name, phone_number=participant_phone
            )

            if not created:  # If participant already exists
                messages.error(request, "A participant with this phone number already exists.")
                return redirect("questionnaire")  # Redirect back to the form

            for teacher in teachers:
                for question in questions:
                    response_key = f"response_{teacher.id}_{question.id}"
                    response_value = request.POST.get(response_key)

                    if response_value:
                        Response.objects.create(
                            participant=participant,  # Associate response with participant
                            teacher=teacher,
                            question=question,
                            response=response_value
                        )
            messages.success(request, "Your responses have been successfully submitted.")
            return redirect("success")  # Redirect on success

    return render(
        request,
        "questionnaire/questionnaire.html",
        {
            "teachers": teachers,
            "questions": questions,
            "categories": categories,
            "participants": participants,
        },
    )





















# from django.shortcuts import render, redirect
# from .models import Teacher, Question, Response, Participant, QuestionCategory
#
#
#
# def app_landing(request):
#     return render(
#         request,
#         "questionnaire/landing.html",
#     )
#
#
# def success(request):
#     return render(
#         request,
#         "questionnaire/success.html",
#     )
#
#
# def questionnaire_view(request):
#     teachers = Teacher.objects.all()
#     questions = Question.objects.all()
#     categories = QuestionCategory.objects.all()  # Fixed: Should get categories, not questions
#     participants = Participant.objects.all()  # Fetch all participants
#
#     if request.method == "POST":
#         participant_name = request.POST.get("participant_name")
#         participant_phone = request.POST.get("participant_phone")
#
#
#         if participant_name and participant_phone:
#             participant, _ = Participant.objects.get_or_create(name=participant_name, phone_number=participant_phone)
#
#             for teacher in teachers:
#                 for question in questions:
#                     response_key = f"response_{teacher.id}_{question.id}"
#                     response_value = request.POST.get(response_key)
#
#                     if response_value:
#                         Response.objects.create(teacher=teacher, question=question, response=response_value)
#
#             return redirect("success")  # Redirect to success page
#
#     return render(
#         request,
#         "questionnaire/questionnaire.html",
#         {"teachers": teachers, "questions": questions, "categories": categories, "participants": participants},
#     )
