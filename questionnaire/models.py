from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length = 11)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

class Teacher(models.Model):
    name = models.CharField(max_length=255)
    # subject = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

class QuestionCategory(models.Model):
    category_text = models.CharField(max_length=33)

    def __str__(self):
        return self.category_text


class Question(models.Model):
    question_category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return f" {self.text[:50]} - {self.question_category}"  # Show a preview of the question

class Response(models.Model):
    SCALE_CHOICES = [
        ('SA', 'Strongly Agree'),
        ('A', 'Agree'),
        ('D', 'Disagree'),
        ('SD', 'Strongly Disagree'),
    ]
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=2, choices=SCALE_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.name}"
