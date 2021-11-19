import rospy
from ros_interop.srv import TeamResponse
from ros_interop.msg import * 
from geographic_msgs.msg import GeoPoint

class TeamsManager():

    def __init__(self,interop_client) -> None:
        self.interop_client = interop_client
        pass

    def router(self,req):
        type = req.request_type.request_type
        if type == RequestType.GET:
            return self.get_teams()
        else:
            return None
    def get_teams(self):
        print("Get Teams Called")
        teams = []
        msg = TeamStatus()
        id = TeamID()
        id.id = 1
        id.username = 'hello'
        id.name = 'pack'
        id.university = "ncsu"
        msg.Team = id
        msg.in_air = False
        msg.telemetry = Telemetry(GeoPoint(0,0,0),0)
        teams = TeamResponse()
        teams.team_list = []
        teams.team_list.append(msg)
        teams.team_list.append(msg)
        return teams