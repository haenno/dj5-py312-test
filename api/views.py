import logging
import json

from django.http import HttpResponse

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def tick(request):
    message = "tock"
    data = {"status": 200, "message": message}
    logging.info(data)
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json", status=200)
