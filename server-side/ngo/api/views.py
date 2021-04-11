from .serializers import NGOSerializer,NGOListSerializer
from ngo.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import datetime
from ..forms import NGOFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator
from .fieldSerializers import *

#Pagination Setting
PAGE_SIZE = 18


class api_filter_ngo(generics.ListAPIView):
    queryset = NGO.objects.all().order_by('-updated_on')
    serializer_class = NGOListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NGOFilter 
    pagination_class = PageNumberPagination
    

@api_view(['GET',])
def api_detail_ngo(request,slug):
    try:
        sch = NGO.objects.get(slug=slug)
    except NGO.DoesNotExist :
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = NGOSerializer(sch)
    context = {
        
        "results" : serializer.data
    }
    return Response(context)




@api_view(['GET',])
def api_list_active_ngo(request):
    try:
        qs = NGO.objects.all().order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except NGO.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = NGOListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)



@api_view(['GET',])
def api_search_ngo(request):
    try:
        q = request.GET.get('q')
        sch = NGO.objects.all()
        qs = sch.filter(title__icontains=q).order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except NGO.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = NGOListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 

@api_view(['GET'])
def form_fields(request):
    state = StateSerializer(State.objects.all(),many = True)
    religion = ReligionSerializer(Religion.objects.all(),many = True)
    country = CountrySerializer(Country.objects.all(),many = True)
    gender = GenderSerializer(Gender.objects.all(),many = True )
    stype = TypeSerializer(Type.objects.all(),many = True)
    category = CategorySerializer(Category.objects.all(),many = True)

    data = {
        'state':state.data,
        'religion':religion.data,
        'country':country.data,
        'gender':gender.data,
        'type':stype.data,
        'category':category.data
    }

    return Response(data)

    


