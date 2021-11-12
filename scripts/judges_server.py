import rospy
from ros_interop.srv import Team,TeamResponse,Odlc,OdlcResponse
from ros_interop.msg import * 
from ros_interop.teams_manager import TeamsManager
from ros_interop.odlc_manager import ODLCManager


def judges_server():
    rospy.init_node('judges_server')
    teamsObj = TeamsManager()
    s2 = rospy.Service('teams',Team,teamsObj.router)
    odlcObj = ODLCManager()
    s = rospy.Service('odlc', Odlc, odlcObj.router)
    rospy.spin()

if __name__ == '__main__':
    judges_server()
    