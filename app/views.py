# app_genslo/views.py
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def generar_kml(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)

    data = json.loads(request.body)
    contenido = f"""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>{data.get("nombre_ad", "Aeródromo")}</name>
    <Placemark><description>Archivo generado correctamente</description></Placemark>
  </Document>
</kml>"""

    response = HttpResponse(contenido, content_type="application/vnd.google-earth.kml+xml")
    response['Content-Disposition'] = 'attachment; filename="archivo.kml"'
    return response

def generar_txt(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Método no permitido"}, status=405)

    data = json.loads(request.body)
    contenido = "\n".join([f"{k}: {v}" for k, v in data.items()])
    response = HttpResponse(contenido, content_type="text/plain")
    response['Content-Disposition'] = 'attachment; filename="informe.txt"'
    return response
