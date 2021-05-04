from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views import View
from .services.equations.router import EquationDataService

# Create your views here.

class LinearEquationAPI(APIView):

    

    def post(self, request):
        data = {
            "message" : 'fail',
            "data" : []
        }
        req_data = request.data

        if 'equation' in request.data:
            equation_router = EquationDataService(req_data)
            equation_router.get_function_service()
            output = equation_router.solve_function()
            
            if output['result'].lower() == 'success':
                data['data'] = output['points']
                data['message'] = output['result']

        return JsonResponse(data)

class LinearEquationView(View):
    
    

    template_name = 'graph/draw.html'

    def get(self, request):

        return render(request, self.template_name)
