# from django.shortcuts import render
# from django.http import JsonResponse

from students.models import Student
from .serializers import StudentSerializers,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
# Create your views here

'''  FUNCTON BASED VIEWS '''

@api_view(["GET", "POST"])
def studentsViews(request):
    # Get the Data of All Students.
    if request.method =="GET":
        students = Student.objects.all()
        serializer= StudentSerializers(students, many= True)
        return Response (serializer.data, status= status.HTTP_200_OK)
    # Post the Data of All Students.
    elif request.method=="POST":
        serializer=StudentSerializers(data= request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        print(serializer.errors)
    return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#Here used some cared oprations on Students Data
@api_view(["GET","PUT","DELETE"])  
def studentsdataview(request,pk):
    # Get the Data of any particular Students Fom the DataBase
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
  
    if request.method=="GET":
       Serializer=StudentSerializers(student)
       return Response(Serializer.data,status=status.HTTP_200_OK)
    
     
       #Change any particular Student Data Fom the DataBase
    elif request.method =="PUT":
        Serializer=StudentSerializers(student,data=request.data)
        if Serializer.is_valid():
         Serializer.save()

         return Response(Serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        #Delete any particular Student Data Fom the DataBase
    elif request.method =="DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



'''  CLASS BASED VIEWS '''



class Employees(APIView): 
#we don't need any decurator here this APIVIEW can manage All cerad operations


    # Get the Data of All Employees.
    def get(self,request):
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # Post the Data of All Employees.

    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
    

    
class EmployeeDetail(APIView):

    #Here we Create the function help the to get the data from DataBase. if it found then it pass to next function if not so  say (Employee.DoesNotExist)
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        

# Get the Data of any particular Employee Fom the DataBase
    def get(self,request,pk):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

#Change any particular Employee Data Fom the DataBase
    def put(self,request,pk):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        


#delete any particular Employee Data Fom the DataBase
    def delete(self,request,pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    