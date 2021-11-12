import rospy
from ros_interop.msg import *
from ros_interop.srv import *
class ODLCManager():
    def __init__(self) -> None:
        pass
    def router(self,req):
        type = req.type
        if type == "GET":
            return self.get_target(req)
        elif type == "POST":
            return self.post_target(req)
        else:
            return None
    def get_target(self,req):
        targetId = req.mission
        print("Get Target Called")
        msg1 = OdlcResponse()
        msg = singleOdlc()
        msg.mission = targetId
        msg.type = odlc_type(True,False)
        msg.latitude = 43.356
        msg.longitude = 54.653
        msg.orientation = odlc_orientation(2)
        msg.shape = odlc_shape(1)
        msg.alphanumeric = "Hello world"
        msg.shape_color = color(1)
        msg.alphanumeric_color = color(2)
        msg.description = "HelloPt2"
        msg.autonomous  = False
        msg1.target_info = msg
        return msg1
    def post_target(self,req):
        print("target posted")
        return None