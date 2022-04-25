from ros_interop.mission_manager import MissionManager
from ros_interop.telemetry_manager import TelemetryManager
import rospy
from ros_interop.srv import Team,ODLC,ODLCs,Mission,TelemetrySrv,Image
from ros_interop.teams_manager import TeamsManager
from ros_interop.odlc_manager import ODLCManager
from ros_interop.map_image_manager import MapImageManager
from interop_clients import InteropClient


def judges_server(url:str, username:str, password:str):
    interop_client = InteropClient(url,username,password)
    rospy.init_node('judges_server')
    teams_obj = TeamsManager(interop_client)
    teams_service = rospy.Service('teams',Team,teams_obj.router)
    ODLC_obj = ODLCManager(interop_client)
    ODLC_service = rospy.Service('odlc', ODLC, ODLC_obj.router_ODLC)
    ODLCs_service = rospy.Service('odlcs',ODLCs, ODLC_obj.router_ODLCs)
    ODLC_image_service = rospy.Service('odlc_image',Image,ODLC_obj.router_ODLC_image)
    mission_obj = MissionManager(interop_client)
    mission_service = rospy.Service('mission',Mission,mission_obj.router)
    telemetry_obj = TelemetryManager(interop_client)
    telemetry_service = rospy.Service('telemetry', TelemetrySrv, telemetry_obj.router)
    map_image_obj = MapImageManager(interop_client)
    map_image_service = rospy.Service('map_image',Image,map_image_obj.router)
    rospy.spin()

if __name__ == '__main__':
    judges_server("http://localhost:8000","testuser","testpass")
    