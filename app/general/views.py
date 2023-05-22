from django.http import HttpResponse
from .settings import server_name, mods_folder, date
import zipfile
import os
import io

def download(request):
  zip_filename = f'{server_name}_mods_{date}.zip'
  buffer = io.BytesIO()
  with zipfile.ZipFile(buffer, 'w') as zip_file:
      for root, _, files in os.walk(mods_folder):
          for file in files:
              file_path = os.path.join(root, file)
              zip_file.write(file_path, os.path.relpath(file_path, mods_folder))
  buffer.seek(0)
  response = HttpResponse(buffer, content_type='application/zip')
  response['Content-Disposition'] = 'attachment; filename="{0}"'.format(zip_filename)
  return response
