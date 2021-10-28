from __future__ import print_function

import sys
import rospy
from ros_interop.srv import Team,Odlc,OdlcRequest
from ros_interop.msg  import Id

def teams_client():
    rospy.wait_for_service('teams')
    try:
        teams = rospy.ServiceProxy('teams', Team)
        resp1 = teams(type = "GET")
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def odlc_client():
    rospy.wait_for_service('odlc')
    reqType = "GET"
    try:
        odlcServer = rospy.ServiceProxy('odlc', Odlc)
        request = OdlcRequest(Id(int(1)),"GET")
        resp1 = odlcServer(request)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    


def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    print(odlc_client())