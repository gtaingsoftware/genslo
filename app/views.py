from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app.genslo import main

@csrf_exempt
def ejecutar_programa(request):
    if request.method == "POST":
        datos = {
            "nombre_ad": request.POST["nombre_ad"],
            "pista": request.POST["pista"],
            "ancho_pista": request.POST["ancho_pista"],
            "lat_op_dms": request.POST["lat_op_dms"],
            "long_op_dms": request.POST["long_op_dms"],
            "elev_op": request.POST["elev_op"],
            "lat_ext_dms": request.POST["lat_ext_dms"],
            "long_ext_dms": request.POST["long_ext_dms"],
            "elev_ext": request.POST["elev_ext"],
            "tipo_aprox": request.POST["tipo_aprox"],
            "n_clave": request.POST["n_clave"],
            "ref_shi": request.POST["ref_shi"],
        }

        # Llamamos a tu función principal
        data_kml, data_txt = main(**datos)

        # Según el botón presionado:
        if "descargar_kml" in request.POST:
            response = HttpResponse(data_kml, content_type="application/vnd.google-earth.kml+xml")
            response["Content-Disposition"] = f'attachment; filename="{datos["nombre_ad"]}_{datos["pista"]}.kml"'
            return response

        elif "descargar_txt" in request.POST:
            response = HttpResponse(data_txt, content_type="text/plain")
            response["Content-Disposition"] = f'attachment; filename="{datos["nombre_ad"]}_informe.txt"'
            return response

    # Si es GET, renderizar el formulario
    return render(request, "generar.html")
