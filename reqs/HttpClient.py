import datetime
import logging

import requests

from reqs import IEntity
from reqs.IHttpClient import IHttpClient
from reqs.IRemovable import IRemovable

logging.basicConfig(
    # filename="/var/log/harbor_clean/output_" + (datetime.datetime.now()).strftime("%Y-%m-%d") + ".txt",
    filename="output_" + (datetime.datetime.now()).strftime("%Y-%m-%d") + ".txt",
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class HttpClient(IHttpClient):
    def __init__(self):
        pass

    def get_content(self, url: str, sort_field=None, reverse=False):
        try:
            response = requests.get(
                url,
                verify=False
            )
            if response.status_code == 200:
                # if sort_field:
                #     logger.info("Method: get_content; Content " + entity.get_entity()
                #                 + " was got successfully. With sort_field :" + sort_field)
                #     entity.content = sorted(response.json(), key=lambda k: k[sort_field], reverse=reverse)
                #     return entity
                # else:
                logger.info("Method: get_content; Content " + " was got successfully")
                return response
            else:
                logger.error("Method: get_content; Response status code : " + str(response.status_code) +
                             "; Reason : " + str(response.reason))
        except Exception as e:
            logger.error(e)

    def delete_content(self, entity: IRemovable, url: str):
        if entity.removable():
            try:
                response = requests.delete(
                    url,
                    verify=False
                )
                if response.status_code == 200:
                    logger.info("Method: delete_content; Type: " + entity.__module__ + " with name: " + entity.name +
                                " -was deleted successfully. Was used URL - " + url)
                else:
                    logger.error("Method: delete_content; Response status code : " + str(response.status_code) +
                                 "; Reason : " + str(response.reason))
            except Exception as e:
                logger.error(e)
        else:
            logger.error("Method: delete_content; Reason: Entity " + entity.__module__ + " is not removable!")
