from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()


def __str__(self):
    return self.doctor.name + "--" + self.patient.name + " " + str(self.date1) + " " + str(self.time1)

