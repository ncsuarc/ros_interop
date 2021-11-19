import rospy
from ros_interop.srv import Team,ODLC,ODLCs
from ros_interop.msg import * 
from ros_interop.teams_manager import TeamsManager
from ros_interop.odlc_manager import ODLCManager
from interop_clients import InteropClient


def judges_server(url:str, username:str, password:str):
    try:
        interop_client = InteropClient(url,username,password)
    except:
        interop_client = None
    rospy.init_node('judges_server')
    teams_obj = TeamsManager(interop_client)
    teams_service = rospy.Service('teams',Team,teams_obj.router)
    ODLC_obj = ODLCManager(interop_client)
    ODLC_service = rospy.Service('odlc', ODLC, ODLC_obj.router_ODLC)
    ODLCs_service = rospy.Service('odlcs',ODLCs, ODLC_obj.router_ODLCs)
    rospy.spin()

if __name__ == '__main__':
    judges_server('url','user','pwd')
    