from .serializers import LoanSerializer,LoanListSerializer
from loans.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
import datetime
from ..forms import LoanFilter
from django_filters import rest_framework as filters
from django.core.paginator import Paginator
from .fieldSerializers import *

#Pagination Setting
PAGE_SIZE = 18


class api_filter_loan(generics.ListAPIView):
    queryset = Loan.objects.all().order_by('-updated_on')
    serializer_class = LoanSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LoanFilter 
    pagination_class = PageNumberPagination
    

""" @api_view(['GET',])
def api_detail_loan(request,slug):
    try:
        sch = Loan.objects.get(slug=slug)
    except Loan.DoesNotExist :
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = LoanSerializer(sch)
    context = {
        
        "results" : serializer.data
    }
    return Response(context) """




@api_view(['GET',])
def api_list_active_loan(request):
    try:
        qs = Loan.objects.all().order_by('-updated_on')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Loan.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = LoanSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context)


@api_view(['GET',])
def api_search_loan(request):
    try:
        q = request.GET.get('q')
        sch = Loan.objects.all()
        if sort:
            qs = sch.filter(title__icontains=q).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('-updated_on')
        else:
            qs = sch.filter(title__icontains=q).filter(deadline__gte = datetime.datetime.now().strftime("%Y-%m-%d") ).order_by('deadline')
        paginator = Paginator(qs, PAGE_SIZE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    except Loan.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    serializer = LoanListSerializer(page_obj,many = True)
    context = {
        "count" : qs.count(),
        "results" : serializer.data
    }
    return Response(context) 

@api_view(['GET'])
def form_fields(request):
    state = StateSerializer(State.objects.all(),many = True)
    district = DistrictSerializer(district.objects.all(),many = True)
    religion = ReligionSerializer(Religion.objects.all(),many = True)
    LoanAmt = LoanAmtSerializer(LoanAmt.objects.all(),many=True)
    country = CountrySerializer(Country.objects.all(),many = True)
    category = CategorySerializer(Category.objects.all(),many = True)

    data = {
        'state':state.data,
        'district':district.data,
        'religion':religion.data,
        'LoanAmt':LoanAmt.data,
        'country':country.data,
        'category':category.data
    }

    return Response(data)

    


