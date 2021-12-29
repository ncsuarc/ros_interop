import rospy
from ros_interop.srv import TelemetrySrvResponse
from ros_interop.msg import * 
from geographic_msgs.msg import GeoPoint

class TelemetryManager():

    def __init__(self,interop_client) -> None:
        self.interop_client = interop_client

    def router(self,req):
        type = req.request_type.request_type
        if type == RequestType.POST:
            return self.post_telemetery(req)
        else:
            return None
    def post_telemetery(self,req):
        telemetry_info = req.telemetry_request
        print(telemetry_info)
        telemetry_data = {}
        telemetry_data['latitude'] = telemetry_info.position.latitude
        telemetry_data['longitude'] = telemetry_info.position.longitude
        telemetry_data['altitude'] = telemetry_info.position.altitude
        telemetry_data['heading'] = telemetry_info.heading
        resp = self.interop_client.post_telemetry(telemetry_data)
        return TelemetrySrvResponse(telemetry_info)