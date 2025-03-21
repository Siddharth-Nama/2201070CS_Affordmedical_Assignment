from django.shortcuts import render
import random
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
BASE_URL = "http://20.244.56.144/test"
API_TYPES = ["primes","fibo","even","rand"]

class CalculateAverageAPIView(APIView):
    def get(self, request):
        selected_api = random.choice(API_TYPES)
        try:
            response = requests.get(f"{BASE_URL}/{selected_api}")
            data = response.json()
            numbers = data.get("numbers",[])
            windowPrevState = [],
            windowCurrState = [],
            WindowSize = 10

            flat_numbers = []
            for num in numbers:
                if isinstance(num,list):
                    flat_numbers.extend(num)
                else:
                    flat_numbers.append(num)
                
            
            for i in range(len(flat_numbers)):
                if i < WindowSize:
                    windowCurrState.append(flat_numbers[i])
                else:
                    windowPrevState = windowCurrState[:]
                    windowCurrState = windowCurrState[1:]
                    windowCurrState.append(flat_numbers[i])

            if windowCurrState:
                avg = sum(windowCurrState)/len(windowCurrState)
            else:
                avg = 0
            
            print(f"windowPrevState--------------:{windowPrevState}")
            print(f"windowCurrState---------------------:{windowCurrState}")
            print(f"numbers----------:{numbers}")
            print(f"avg----------:{avg}")
            print(f"selected_api------------:{selected_api}")

            return Response({
                "windowPrevState":windowPrevState,
                "windowCurrState":windowCurrState,
                "numbers":numbers,
                "avg":round(avg,2),
            })
        
        except Exception as e:
            return Response({
                "error":str(e),"selected_api":selected_api
            },status=500)