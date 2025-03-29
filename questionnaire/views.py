from django.shortcuts import render, redirect
from .models import Teacher, Question, Response, Participant, QuestionCategory



def app_landing(request):
    return render(
        request,
        "questionnaire/landing.html",
    )


def questionnaire_view(request):
    teachers = Teacher.objects.all()
    questions = Question.objects.all()
    categories = QuestionCategory.objects.all()  # Fixed: Should get categories, not questions
    participants = Participant.objects.all()  # Fetch all participants

    if request.method == "POST":
        participant_name = request.POST.get("participant_name")
        participant_phone = request.POST.get("participant_phone")

        if participant_name and participant_phone:
            participant, _ = Participant.objects.get_or_create(name=participant_name, phone_number=participant_phone)

            for teacher in teachers:
                for question in questions:
                    response_key = f"response_{teacher.id}_{question.id}"
                    response_value = request.POST.get(response_key)

                    if response_value:
                        Response.objects.create(teacher=teacher, question=question, response=response_value)

            return redirect("success")  # Redirect to success page

    return render(
        request,
        "questionnaire/questionnaire.html",
        {"teachers": teachers, "questions": questions, "categories": categories, "participants": participants},
    )
