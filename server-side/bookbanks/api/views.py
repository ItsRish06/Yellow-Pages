from .serializers import BookbankSerializer
from bookbanks.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import datetime
from ..forms import BookbankFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator
from .fieldSerializers import *

#Pagination Setting
PAGE_SIZE = 18


class api_filter_bookbank(generics.ListAPIView):
    queryset = Bookbank.objects.all().order_by('-updated_on')
    serializer_class = BookbankSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookbankFilter 
    pagination_class = PageNumberPagination
    

@api_view(['GET',])
def api_detail_bookbank(request,slug):
    try:
        sch = Bookbank.objects.get(slug=slug)
    except Bookbank.DoesNotExist :
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = BookbankSerializer(sch)
    context = {
        
        "results" : serializer.data
    }
    return Response(context)



@api_view(['GET',])
def api_list_active_bookbank(request):
    try:
        qs = Bookbank.objects.all().order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Bookbank.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = BookbankSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)




@api_view(['GET',])
def api_search_bookbank(request):
    try:
        q = request.GET.get('q')
        sch = Bookbank.objects.all()
        qs = sch.filter(title__icontains=q).order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Bookbank.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = BookbankSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 

@api_view(['GET'])
def form_fields(request):
    state = StateSerializer(State.objects.all(),many = True)
    district = DistrictSerializer(District.objects.all(),many = True)
    books = BookSerializer(Books.objects.all(),many = True)

    data = {
        'state':state.data,
        'district':district.data,
        'books':books.data,
    }

    return Response(data)

    


