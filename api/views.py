
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import searializers
from api.models import Firmware
from api.searializers import FirmwareSearializer

# Create your views here.
@api_view(["GET"])
def homeView(request):
    api_urls = {
        "add firmware post to sammobiles db" : "/add-post",
    }
    return Response(api_urls)

@api_view(["POST"])
def addFileLink(request):
    try:
       # print(request.data)
        serializer = FirmwareSearializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status" : "success"},status = 200)
        else:
             return Response({"status" : "failed"},status = 400)
    except:
        return Response({"status" : "server-failure"},status = 400)

@api_view(["GET"])
def getFirmwareLins(request):
    firmwares = Firmware.objects.all()
    searializer= FirmwareSearializer(firmwares,many=True)
    return Response(searializer.data)