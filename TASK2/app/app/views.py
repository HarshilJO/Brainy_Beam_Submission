from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import DataFrameEntry
import json

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def data_frame(request):
    if request.method == 'POST':
        try:
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)
            if len(df.columns) != 4:
                return JsonResponse({'error': 'CSV must have exactly 4 columns'}, status=400)
            df.columns = ['column1', 'column2', 'column3', 'date_field']
            # df['date_field'] = pd.to_datetime(df['date_field'])            
            for _, row in df.iterrows():
                DataFrameEntry.objects.create(
                    column1=row['column1'],
                    column2=row['column2'],
                    column3=row['column3'],
                    date_field=row['date_field']
                )
            return JsonResponse({'data': df.to_dict(orient='records')})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

