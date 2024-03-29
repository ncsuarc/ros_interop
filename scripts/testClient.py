from __future__ import print_function

import sys
from urllib.request import Request
import rospy
from ros_interop.srv import Team,ODLC,ODLCRequest,Mission,MissionRequest, TelemetrySrv, TelemetrySrvRequest, ODLCs,ODLCsRequest,Image,ImageRequest
from ros_interop.msg import *
from geographic_msgs.msg import GeoPoint
from pathlib import Path

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
        #TODO Fix Alphanumeric ODLC
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

def map_image_client():
    rospy.wait_for_service('map_image')
    try:
        map_service = rospy.ServiceProxy('map_image',Image)
        req = map_service(ImageRequest(id = 1,request_type = RequestType(RequestType.PUT),image_data = Path('/home/kssaboo/catkin_ws/imageABCD3.png').read_bytes() ))
        print('hi')
        #req = map_service(ImageRequest(id = 1, request_type = RequestType(RequestType.DELETE)))
        resp = map_service(ImageRequest(id = 1,request_type = RequestType(RequestType.GET)))
        with open('/home/kssaboo/catkin_ws/imageABCD2.png','wb') as f:
            f.write((resp.image_data))
        return None
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
def odlc_image_client():
    rospy.wait_for_service('odlc_image')
    try:
        map_service = rospy.ServiceProxy('odlc_image',Image)
        req = map_service(ImageRequest(id = 100,request_type = RequestType(RequestType.PUT),image_data = Path('/home/kssaboo/catkin_ws/imageABCD3.png').read_bytes() ))
        print('hi')
        #req = map_service(ImageRequest(id = 1, request_type = RequestType(RequestType.DELETE)))
        resp = map_service(ImageRequest(id = 100,request_type = RequestType(RequestType.GET)))
        with open('/home/kssaboo/catkin_ws/imageABCD4.png','wb') as f:
            f.write((resp.image_data))
        return None
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
def telemetry_client():
    rospy.wait_for_service('telemetry')
    try:
        telemetry_service = rospy.ServiceProxy('telemetry',TelemetrySrv)
        telemetry_obj = telemetry(GeoPoint(35,38,45),45)
        resp = telemetry_service(TelemetrySrvRequest(request_type = RequestType(RequestType.POST), telemetry_request = telemetry_obj))
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def odlcs_client():
    rospy.wait_for_service('odlcs')
    try:
        odlcs_service = rospy.ServiceProxy('odlcs', ODLCs )
        resp = odlcs_service(ODLCsRequest(request_type = RequestType(RequestType.GET), mission_id = 1))
        return resp
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    print(odlc_image_client())