import rospy
from ros_interop.msg import *
from ros_interop.srv import ImageResponse

class MapImageManager():
    def __init__(self,interop_client) -> None:
        self.interop_client = interop_client
        pass
    def router(self,req):
        type = req.request_type.request_type
        if type == RequestType.GET: 
            return self.get_image(req)
        elif type == RequestType.PUT:
            return self.put_image(req)
        elif type == RequestType.DELETE:
            return self.delete_image(req)
        else:
            return None
    def get_image(self,req):
        id = req.id
        image = self.interop_client.get_map_image(id)
        response = ImageResponse()
        response.id = id
        response.image_data = image
        return response
    def put_image(self,req):
        id = req.id
        image_data = req.image_data
        self.interop_client.put_map_image(id,image_data)
        return ImageResponse(id = id)
    def delete_image(self,req):
        id = req.id
        self.interop_client.delete_map_image(id)
        return ImageResponse(id = id)