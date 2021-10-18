from __future__ import print_function

import sys
import rospy
from ros_interop.srv import Team

def get_teams_client():
    rospy.wait_for_service('getTeams')
    try:
        getTeams = rospy.ServiceProxy('getTeams', Team)
        resp1 = getTeams()
        return resp1
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    print(get_teams_client())