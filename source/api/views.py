import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def calculate(request, operation):
    try:
        data = json.loads(request.body)
        a = data.get('A')
        b = data.get('B')

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return JsonResponse({'error': 'A and B must be numbers!'}, status=400)

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return JsonResponse({'error': 'Division by zero!'}, status=400)
            result = a / b

        return JsonResponse({'answer': result})

    except (json.JSONDecodeError, TypeError):
        return JsonResponse({'error': 'Invalid data!'}, status=400)


@csrf_exempt
@require_POST
def add(request):
    return calculate(request, 'add')


@csrf_exempt
@require_POST
def subtract(request):
    return calculate(request, 'subtract')


@csrf_exempt
@require_POST
def multiply(request):
    return calculate(request, 'multiply')


@csrf_exempt
@require_POST
def divide(request):
    return calculate(request, 'divide')