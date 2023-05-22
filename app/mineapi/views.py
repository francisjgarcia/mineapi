from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .settings import server_host, server_port
from mcstatus import JavaServer
import json
import hashlib

def status(request):
  try:
    conn = JavaServer.lookup(f'{server_host}:{server_port}')
    try:
      conn.ping()
    except:
      data = { 'status': 'Offline' }
      return JsonResponse(data, status=200)
    else:
      data = { 'status': 'Online' }
      return JsonResponse(data, status=200)
  except:
    response = { 'error': 'Internal Server Error' }
    return JsonResponse(response, status=500)

def players(request):
  try:
    conn = JavaServer.lookup(f'{server_host}:{server_port}')
    try:
      conn.ping()
      status = conn.status()
    except:
      data = { 'players_online': 0, 'players_max': 0 }
      return JsonResponse(data, status=200)
    else:
      data = { 'players_online': status.players.online, 'players_max': status.players.max }
      return JsonResponse(data, status=200)
  except:
    response = { 'error': 'Internal Server Error' }
    return JsonResponse(response, status=500)

@csrf_exempt
def whitelist(request):
  try:
    if request.method == 'POST':
      if not request.body:
        response = { 'error': 'No se proporcionaron datos JSON en la solicitud.' }
        return JsonResponse(response, status=400)

      try:
          data = json.loads(request.body.decode('utf-8'))
      except json.JSONDecodeError:
          response = { 'error': 'Los datos JSON en la solicitud no son válidos.' }
          return JsonResponse(response, status=400)

      data = json.loads(request.body.decode('utf-8'))

      if "username" not in data:
          response = { 'error': 'El campo "username" no está definido.' }
          return JsonResponse(response, status=400)

      username = data["username"]

      def addUuidStripes(string):
          string_striped = (
              string[:8] + '-' +
              string[8:12] + '-' +
              string[12:16] + '-' +
              string[16:20] + '-' +
              string[20:]
          )
          return string_striped

      def constructOfflinePlayerUuid(username):
          string = "OfflinePlayer:" + username
          hash = hashlib.md5(string.encode('utf-8')).digest()
          byte_array = [byte for byte in hash]
          byte_array[6] = hash[6] & 0x0f | 0x30
          byte_array[8] = hash[8] & 0x3f | 0x80
          return addUuidStripes(bytes(byte_array).hex())

      data = { 'user': username, 'uuid': constructOfflinePlayerUuid(username) }
      return JsonResponse(data, status=200)
    else:
      response = { 'error': 'Bad Request' }
      return JsonResponse(response, status=400)
  except:
    response = { 'error': 'Internal Server Error' }
    return JsonResponse(response, status=500)
