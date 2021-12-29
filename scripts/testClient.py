from __future__ import print_function

import sys
import rospy
from ros_interop.srv import Team,ODLC,ODLCRequest,Mission,MissionRequest
from ros_interop.msg import *

def teams_client():
    rospy.wait_for_service('teams')
    try:
        teams = rospy.ServiceProxy('teams', Team)
        resp1 = teams(request_type = RequestType(RequestType.GET))
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def odlc_client():
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
        resp2 = odlcServer(ODLCRequest(id = 67,request_type =  RequestType(RequestType.GET)))
        odlcPut = singleODLC()
        odlcPut.latitude = 87
        msg2 = ODLCRequest(67, RequestType(RequestType.PUT),odlcPut)
        resp2 = odlcServer(msg2)
        response = odlcServer(ODLCRequest(67,RequestType(RequestType.GET),singleODLC()))
        print(resp1.id-1)
        #response = odlcServer(ODLCRequest(resp1.id-1,RequestType(RequestType.DELETE),singleODLC()))
        return response
    
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    
def mission_client():
    rospy.wait_for_service('mission')
    try:
        mission_service = rospy.ServiceProxy('mission',Mission)
        resp = mission_service(MissionRequest(mission_id = 1,request_type = RequestType(RequestType.GET)))
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    print(mission_client())