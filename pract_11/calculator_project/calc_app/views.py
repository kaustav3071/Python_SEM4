from django.shortcuts import render

def calculator(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            operation = request.POST.get('operation')

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    result = "Cannot divide by zero"
                else:
                    result = num1 / num2
        except ValueError:
            result = "Please enter valid numbers"

    return render(request, 'calculator.html', {'result': result})