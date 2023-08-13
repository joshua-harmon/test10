from .models import Job, Category
from .serializers import CategorySerializer, JobDetailSerializer, JobSerializer

from rest_framework import status, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

class NewsetJobsView(APIView):
  def get(self, request, format=None):
    jobs = Job.objects.all()[0:4]
    serializer = JobSerializer(jobs, many=True)

    return Response(serializer.data)


class BrowseJobsView(APIView):
  def get(self, request, format=None):
    jobs = Job.objects.all()
    categories = request.GET.get('categories', '')
    query = request.GET.get('title', '')

    if categories:
      jobs = jobs.filter(category_id__in=categories.split(','))
    if query:
      jobs = jobs.filter(title__icontains=query)
    
    serializer = JobSerializer(jobs, many=True)


    return Response(serializer.data)
  
  
class JobsDetailView(APIView):
  def get(self, request, pk, format=None):
    job = Job.objects.get(pk=pk)
    serializer = JobDetailSerializer(job)

    return Response(serializer.data)
  
  
class CategoryView(APIView):
  def get(self, request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    
    return Response(serializer.data)