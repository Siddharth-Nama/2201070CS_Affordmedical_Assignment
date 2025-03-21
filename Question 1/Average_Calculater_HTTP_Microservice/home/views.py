from django.shortcuts import render
import random
import requests
from rest_framework.views import APIView
from rest_framework.response import Response

BASE_URL = "http://20.244.56.144/test"
API_TYPES = ["primes", "fibo", "even", "rand"]

class CalculateAverageAPIView(APIView):
    def get(self, request):
        selected_api = random.choice(API_TYPES)

        try:
            response = requests.get(f"{BASE_URL}/{selected_api}")
            data = response.json()
            numbers = data.get("numbers", [])

            def flatten(lst):
                result = []
                for item in lst:
                    if isinstance(item, list):
                        result.extend(flatten(item))
                    elif isinstance(item, int):
                        result.append(item)
                return result
            
            flat_numbers = flatten(numbers)

            windowPrevState = []
            windowCurrState = []
            WindowSize = 10

            for i in range(len(flat_numbers)):
                if i < WindowSize:
                    windowCurrState.append(flat_numbers[i])
                else:
                    windowPrevState = windowCurrState[:]
                    windowCurrState = windowCurrState[1:]
                    windowCurrState.append(flat_numbers[i])

            avg = sum(windowCurrState) / len(windowCurrState) if windowCurrState else 0

            return Response({
                "windowPrevState": windowPrevState,
                "windowCurrState": windowCurrState,
                "numbers": flat_numbers,
                "avg": round(avg, 2),
             })

        except Exception as e:
            return Response({"error": str(e), "selected_api": selected_api}, status=500)
