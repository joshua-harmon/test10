from .models import Job, Category
from .serializers import CategorySerializer, JobDetailSerializer, JobSerializer
from .forms import JobForm

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
  
class MyJobsView(APIView):
  authentication_classes = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  def get(self, request):
    jobs = Job.objects.filter(created_by=request.user)  
    serializer = JobDetailSerializer(jobs, many=True)
    
    return Response(serializer.data)


class CreateJobView(APIView):
  authentication_classes = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticated]
  
  def post(self, request):
    form = JobForm(request.data)
    
    if form.is_valid():
      job = form.save(commit=False)
      job.created_by = request.user
      job.save()
      return Response({'status', 'created'})
    else:
      return Response({'status': 'errors', 'errors': form.errors})
    
  def put(self, request, pk):
    job_for_update = Job.objects.get(pk=pk)
    form = JobForm(request.data, instance=job_for_update)
    form.save()
    return Response(data={'status': 'updated'})
  
  
  def delete(self, request, pk):
    job_for_delete = Job.objects.get(pk=pk)
    job_for_delete.delete()
    
    return Response(data={'status': 'deleted'}, status=200)
  
  
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
  
  