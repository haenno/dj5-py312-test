import logging
import json

from django.http import HttpResponse

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="./data/api.log",
)


def tick(request):
    # start processing the request with write to log
    logging.debug(request.headers)
    logging.debug(f"Path requested: '{request.path}'")

    # do the actual processing here
    pass

    # finish up, prepare response
    message = "tock"
    data = {"status": 200, "message": message}

    # close processing the request with another entry to log
    logging.debug(f"Now sending response: '{data}'")
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json", status=200)
