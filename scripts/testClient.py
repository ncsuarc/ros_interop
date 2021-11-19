from __future__ import print_function

import sys
import rospy
from ros_interop.srv import Team,ODLC,ODLCRequest
from ros_interop.msg import RequestType

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
        request = ODLCRequest(int(1),RequestType(RequestType.GET))
        resp1 = odlcServer(request)
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)
    


def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    print(teams_client())