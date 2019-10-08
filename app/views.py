from django.shortcuts import render
from django.conf import settings
import csv

def inflation_view(request):
    template_name = 'app/inflation.html'
    
    # чтение csv-файла и заполнение контекста
    table_data = []
    with open(settings.INFLATION_RUSSIA_CSV, encoding='utf8') as csvfile:
        table_reader = csv.reader(csvfile, delimiter=';')
        for row in table_reader:
            table_data.append(row)
    table_head = table_data[0]
    table_body = []
    for i in range(1, len(table_data)):
        table_body.append(table_data[i])

    context = {
        'table_head': table_head,
        'table_body': table_body,
        'table_data': table_data
        }
    return render(request, template_name,
                  context)