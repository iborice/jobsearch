from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import PosteSerializer, CategorieSerializer, VilleSerializer
from .models import Poste, Annonce, Categorie, Forme, Ville
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PosteViewSet(viewsets.ModelViewSet):
    queryset = Poste.objects.all().order_by('intitule')
    serializer_class = PosteSerializer

class VilleViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer

class JobsView(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myapi/list_jobs.html'

    def get(self, request):
        queryset = Poste.objects.all().order_by('date')
        categories = Categorie.objects.filter()
        paginator = Paginator(queryset, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return Response({"page_obj":page_obj,"categories":categories})
    
    def post(self,request):
        keywords = self.request.data.get("search1")
        city = self.request.data.get("search2")
        categorie = self.request.data.get("categorie")
        #cat = Categorie.objects.filter(intitule=categorie)[:1].get()

        if categorie == "":
            categories = Categorie.objects.filter()
            cat = None
        else:
            categories = Categorie.objects.filter(intitule__contains=categorie)
            cat = Categorie.objects.filter(id=int(categorie))[:1].get()
        if keywords == "" or city == "":
            if city == "":
                queryset = Poste.objects.filter(categories__in=categories,intitule=keywords).order_by('date')
            else:
                villes = Ville.objects.filter(intitule=city)
                queryset = Poste.objects.filter(categories__in=categories,villes__in=villes).order_by('date')          
        else:
            villes = Ville.objects.filter(intitule=city)
            queryset = Poste.objects.filter(categories__in=categories,intitule=keywords,villes__in=villes).order_by('date')
        all_categories = Categorie.objects.filter()
        paginator = Paginator(queryset, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return Response({"page_obj":page_obj,'keywords':keywords,'city':city,'cat':cat,"categories":all_categories})

class JobDetailsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myapi/job_details.html'
    def get(self,request,*arg, **kwargs):
        queryset = get_object_or_404(Poste,id=self.kwargs['pk'])
        return Response({"job":queryset})

class AboutView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myapi/about.html'
    def get(self,request,*arg, **kwargs):
        return Response({})

class LicenceView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myapi/licence.html'
    def get(self,request,*arg, **kwargs):
        return Response({})

class TermsView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myapi/terms_conditions.html'
    def get(self,request,*arg, **kwargs):
        return Response({})

class ContactView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'myapi/contact.html'
    def get(self,request,*arg, **kwargs):
        return Response({})

# Create your views here.
