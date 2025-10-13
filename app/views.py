from django.http import FileResponse, HttpResponse
from app.genslo import main as main_func
import mimetypes
import os

def ejecutar_programa(request):
    if request.method == "POST":
        data = request.POST
        kml_path, txt_path = main_func(
            nombre_ad=data.get("nombre_ad"),
            pista=data.get("pista"),
            ancho_pista=data.get("ancho_pista"),
            lat_op=data.get("lat_op"),
            lon_op=data.get("lon_op"),
            elev_op=data.get("elev_op"),
            lat_ext=data.get("lat_ext"),
            lon_ext=data.get("lon_ext"),
            elev_ext=data.get("elev_ext"),
            tipo_aprox=data.get("tipo_aprox"),
            n_clave=data.get("n_clave"),
            ref_shi=data.get("ref_shi")
        )

        # Comprimir los archivos en un ZIP para descargar
        import zipfile
        zip_path = os.path.join(os.path.dirname(kml_path), f"{data.get('nombre_ad')}_archivos.zip")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(kml_path, os.path.basename(kml_path))
            zipf.write(txt_path, os.path.basename(txt_path))

        # Devolver el ZIP al navegador
        response = FileResponse(open(zip_path, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{data.get("nombre_ad")}_archivos.zip"'
        return response
    else:
        return HttpResponse("Método no permitido", status=405)
