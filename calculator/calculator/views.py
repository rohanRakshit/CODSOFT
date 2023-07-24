from django.shortcuts import render

def fun1(request):
    expr = ''
    if request.method == 'POST':
        expr = request.POST.get('screen', '')
        value = request.POST.get('num', '')
        opr = request.POST.get('operation', '')
        clear = request.POST.get('allclear', '')
        equals = request.POST.get('equals', '')

        if clear:
            expr = ''
            print("REFRESH")
        elif value:
            expr += value
            print(expr)
        elif opr:
            expr += ' ' + opr + ' '
            print(expr)
        elif equals:
                try:
                    result = str(eval(expr))
                    print(result)
                except:
                    result = 'Error'
                expr = result

    return render(request, 'calc2.html', {'expression': expr})
