from __future__ import print_function

import sys
import rospy
from ros_interop.srv import Team,ODLC,ODLCRequest
from ros_interop.msg import *

def teams_client():
    rospy.wait_for_service('teams')
    try:
        teams = rospy.ServiceProxy('teams', Team)
        resp1 = teams(request_type = RequestType(RequestType.GET))
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def ODLC_client():
    rospy.wait_for_service('odlc')
    try:
        odlcServer = rospy.ServiceProxy('odlc', ODLC)
        msg1 = ODLCRequest()
        msg = singleODLC()
        msg.mission = 1
        msg.latitude = 43.356
        msg.longitude = 54.653
        msg.type = odlc_type(odlc_type.EMERGENT)
        msg.orientation = odlc_orientation(odlc_orientation.N)
        msg.shape = odlc_shape(odlc_shape.STAR)
        #msg.alphanumeric = ""
        msg.shape_color = Color(Color.RED)
        msg.alphanumeric_color = Color(Color.BLACK)
        msg.description = "HelloPt2"
        msg.autonomous  = False
        msg1.post_target_info = msg
        request = ODLCRequest(0,RequestType(RequestType.POST),msg)
        resp1 = odlcServer(request)
        response = odlcServer(ODLCRequest(42,RequestType(RequestType.GET),singleODLC()))
        return response
    
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    


def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    print(ODLC_client())