from .serializers import ScholarshipSerializer,ScholarshipListSerializer
from scholarships.models import Scholarship
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
import datetime
from ..forms import ScholarshipFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator


class api_filter_scholarship(generics.ListAPIView):
    queryset = Scholarship.objects.all().filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
    serializer_class = ScholarshipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScholarshipFilter 
    

@api_view(['GET',])
def api_detail_scholarship(request,slug):
    try:
        sch = Scholarship.objects.get(slug=slug)
    except Scholarship.DoesNotExist :
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(sch)
    return Response(serializer.data)


@api_view(['GET',])
def api_state_list_scholarship(request,state):
    try:
        sch = Scholarship.objects.all()
        qs = sch.filter(state__name__icontains=state).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, 18)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    return Response(serializer.data)
 

@api_view(['GET',])
def api_class_list_scholarship(request,sclass):
    try:
        sch = Scholarship.objects.all()
        qs = sch.filter(sclass__name__icontains=sclass).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, 18)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    return Response(serializer.data) 
 

@api_view(['GET',])
def api_type_list_scholarship(request,stype):
    try:
        sch = Scholarship.objects.all()
        qs = sch.filter(stype__icontains=stype).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, 18)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    return Response(serializer.data)


@api_view(['GET',])
def api_list_active_scholarship(request):
    try:
        qs = Scholarship.objects.all().filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, 18)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    return Response(serializer.data)


@api_view(['GET',])
def api_list_inactive_scholarship(request):
    try:
        qs = Scholarship.objects.all().exclude(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-deadline')
        paginator = Paginator(qs, 18)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    return Response(serializer.data) 


@api_view(['GET',])
def api_category_list_scholarship(request,category):
    try:
        sch = Scholarship.objects.all()
        qs = sch.filter(category__icontains=category).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, 18)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    return Response(serializer.data) 