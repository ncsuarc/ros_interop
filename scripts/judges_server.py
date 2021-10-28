import rospy
from ros_interop.srv import Team,TeamResponse,Odlc,OdlcResponse
from ros_interop.msg import *


class Teams():

    def __init__(self) -> None:
        pass

    def router(self,req):
        type = req.type
        if type == "GET":
            return self.get_teams()
        else:
            return None
    def get_teams(self):
        print("Get Teams Called")
        teams = []
        msg = TeamStatus()
        id = TeamID()
        id.Id = Id()
        id.Id.Id = 1
        id.username = 'hello'
        id.name = 'pack'
        id.university = "ncsu"
        msg.Team = id
        msg.in_air = False
        teams = TeamResponse()
        teams.team_list = []
        teams.team_list.append(msg)
        teams.team_list.append(msg)
        return teams

class odlcs():
    def __init__(self) -> None:
        pass


    def router(self,req):
        type = req.type
        if type == "GET":
            return self.get_targets(req)
        else:
            return "didnt work"

    
    def get_targets(self,req):
        print("Get Targets Called")

class odlc():
    def __init__(self) -> None:
        pass
    def router(self,req):
        type = req.type
        if type == "GET":
            return self.get_target(req)
        else:
            return None
    def get_target(self,req):
        targetId = req.mission
        print("Get Target Called")
        msg1 = OdlcResponse()
        msg = singleOdlc()
        msg.mission = targetId
        msg.type = odlc_type(True,False)
        msg.latitude = 43.356
        msg.longitude = 54.653
        msg.orientation = odlc_orientation(2)
        msg.shape = odlc_shape(1)
        msg.alphanumeric = "Hello world"
        msg.shape_color = color(1)
        msg.alphanumeric_color = color(2)
        msg.description = "HelloPt2"
        msg.autonomous  = False
        msg1.target_info = msg
        return msg1



def judges_server():
    rospy.init_node('judges_server')
    odlcObj = odlc()
    s = rospy.Service('odlc', Odlc, odlcObj.router)
    rospy.spin()

if __name__ == '__main__':
    judges_server()
    