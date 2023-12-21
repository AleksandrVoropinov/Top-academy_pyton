from django.shortcuts import render

<<<<<<< HEAD
def multiplication_table(request):
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return render(request, 'multiplication_table.html', {'table': table})

=======
>>>>>>> origin/main
# Create your views here.
