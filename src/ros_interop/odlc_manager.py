import rospy
from ros_interop.msg import *
from ros_interop.srv import ODLCResponse

class ODLCManager():
    def __init__(self,interop_client) -> None:
        self.interop_client = interop_client
        pass
    def router_ODLC(self,req):
        type = req.request_type.request_type
        if type == RequestType.GET:
            return self.get_target(req)
        elif type == RequestType.POST:
            return self.post_target(req)
        else:
            return None
    def router_ODLCs(self,req):
        pass
    def get_target(self,req):
        target_id = req.mission
        print("Get Target Called")
        if self.interop_client:
            return self.interop_client.get_odlc(target_id)
        msg1 = ODLCResponse()
        msg = singleODLC()
        msg.mission = target_id
        msg.type = odlc_type(True)
        msg.latitude = 43.356
        msg.longitude = 54.653
        msg.orientation = odlc_orientation(2)
        msg.shape = odlc_shape(odlc_shape.STAR)
        msg.alphanumeric = "Hello world"
        msg.shape_color = Color(Color.RED)
        msg.alphanumeric_color = Color(Color.BLACK)
        msg.description = "HelloPt2"
        msg.autonomous  = False
        msg1.target_info = msg
        return msg1
    def post_target(self,req):
        print("target posted")
        return None