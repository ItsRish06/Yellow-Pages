from .serializers import ScholarshipSerializer,ScholarshipListSerializer
from scholarships.models import Scholarship
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import datetime
from ..forms import ScholarshipFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator

PAGE_SIZE = 18

class api_filter_scholarship(generics.ListAPIView):
    queryset = Scholarship.objects.all().filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
    serializer_class = ScholarshipListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScholarshipFilter 
    pagination_class = PageNumberPagination
    

@api_view(['GET',])
def api_detail_scholarship(request,slug):
    try:
        sch = Scholarship.objects.get(slug=slug)
    except Scholarship.DoesNotExist :
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipSerializer(sch)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)


@api_view(['GET',])
def api_state_list_scholarship(request,state):
    try:
        sort = request.GET.get('sort')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(state__name__icontains=state).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(state__name__icontains=state).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)
 

@api_view(['GET',])
def api_class_list_scholarship(request,sclass):
    try:
        sort = request.GET.get('sort')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(sclass__name__icontains=sclass).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(sclass__name__icontains=sclass).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 
 

@api_view(['GET',])
def api_type_list_scholarship(request,stype):
    try:
        sort = request.GET.get('sort')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(stype__icontains=stype).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(stype__icontains=stype).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)


@api_view(['GET',])
def api_list_active_scholarship(request):
    try:
        sort = request.GET.get('sort')
        if sort:
            qs = Scholarship.objects.all().filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = Scholarship.objects.all().filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)


@api_view(['GET',])
def api_list_inactive_scholarship(request):
    try:
        sort = request.GET.get('sort')
        if sort:
            qs = Scholarship.objects.all().exclude(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('updated_on')
        else:
            qs = Scholarship.objects.all().exclude(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 


@api_view(['GET',])
def api_category_list_scholarship(request,category):
    try:
        sort = request.GET.get('sort')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(category__icontains=category).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(category__icontains=category).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)


@api_view(['GET',])
def api_search_scholarship(request):
    try:
        sort = request.GET.get('sort')
        q = request.GET.get('q')
        sch = Scholarship.objects.all()
        if sort:
            qs = sch.filter(title__icontains=q).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(title__icontains=q).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Scholarship.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = ScholarshipListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 
