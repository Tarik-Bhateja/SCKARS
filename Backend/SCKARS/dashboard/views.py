from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
import json,requests

api_key = '9D827COS37E9EX2F'


def unlock(request,api_key, field_value):
    url = f'https://api.thingspeak.com/update?api_key={api_key}&field1={field_value}'
    
    response = requests.post(url)
    
    if response.status_code == 200:
        print('Data sent successfully to ThingSpeak')
        
    else:
        print('Failed to send data to ThingSpeak')

def control_device(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            action = data.get('action')
            

            if action=="ON":
            #  switch on Red LED
             print("Laal Ae Poora Thela Laal Ae")
             field_value = 1
             unlock(request,api_key, field_value)
            #  return HttpResponse("HELLO")
             
             

             
              

            
            # Here, you can add the logic to control your Raspberry Pi device based on the action
            # For example, turn on/off a light

            # Dummy response for demonstration
            response_data = {'success': True, 'message': f'Device has been {action}'}
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


# Create your views here.

def dashboard(request):  
    return render(request,'qrScanner.html')
