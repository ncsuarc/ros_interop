import rospy
from ros_interop.srv import MissionResponse
from ros_interop.msg import * 
from geographic_msgs.msg import GeoPoint

class MissionManager():

    def __init__(self,interop_client) -> None:
        self.interop_client = interop_client

    def router(self,req):
        type = req.request_type.request_type
        if type == RequestType.GET:
            return self.get_mission(req)
        else:
            return None
    def get_mission(self,req):
        mission_data = self.interop_client.get_mission(req.mission_id)
        mission_info = mission()
        mission_info.id = mission_data['id']
        mission_info.lost_comms_pos = GeoPoint(latitude = mission_data['lostCommsPos']['latitude'],longitude = mission_data['lostCommsPos']['longitude'])
        mission_info.fly_zones = []
        for fly_zone in mission_data['flyZones']:
            flyZone = FlyZone()
            flyZone.altitude_min = fly_zone['altitudeMin']
            flyZone.altitude_max = fly_zone['altitudeMax']
            flyZone.boundary_points = []
            for boundary_point in fly_zone['boundaryPoints']:
                boundaryPoint = GeoPoint(latitude = boundary_point['latitude'], longitude = boundary_point['longitude'])
                flyZone.boundary_points.append(boundaryPoint)
            mission_info.fly_zones.append(flyZone)
        mission_info.waypoints = []
        for waypoint in mission_data['waypoints']:
            waypointObj = GeoPoint(waypoint['latitude'],waypoint['longitude'],waypoint['altitude'])
            mission_info.waypoints.append(waypointObj)
        mission_info.search_grid_points = []
        for search_grid_point in mission_data['searchGridPoints']:
            searchGridPoint = GeoPoint(latitude = search_grid_point['latitude'],longitude = search_grid_point['longitude'])
            mission_info.search_grid_points.append(searchGridPoint)
        mission_info.off_axis_odlc_pos = GeoPoint(latitude = mission_data['offAxisOdlcPos']['latitude'],longitude =mission_data['offAxisOdlcPos']['longitude'])
        mission_info.emergent_last_known_pos = GeoPoint(latitude = mission_data['emergentLastKnownPos']['latitude'], longitude = mission_data['emergentLastKnownPos']['longitude'])
        mission_info.air_drop_boundary_points = []
        for air_drop_boundary_point in mission_data['airDropBoundaryPoints']:
            airDropBoundaryPoint = GeoPoint(latitude = air_drop_boundary_point['latitude'],longitude = air_drop_boundary_point['longitude'])
            mission_info.air_drop_boundary_points.append(airDropBoundaryPoint)
        mission_info.air_drop_pos = GeoPoint(latitude = mission_data['airDropPos']['latitude'],longitude = mission_data['airDropPos']['longitude'])
        mission_info.ugv_drive_pos = GeoPoint(latitude = mission_data['ugvDrivePos']['latitude'], longitude = mission_data['ugvDrivePos']['longitude'])
        mission_info.stationary_obstacles = []
        for stationary_obstacle in mission_data['stationaryObstacles']:
            stationaryObstacle = StationaryObstacle(stationary_obstacle['latitude'],stationary_obstacle['longitude'],stationary_obstacle['radius'],stationary_obstacle['height'])
            mission_info.stationary_obstacles.append(stationaryObstacle)
        response = MissionResponse(mission_info)
        return response