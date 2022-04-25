from interop_clients import InteropClient

interop_client = InteropClient("http://localhost:8000","testuser","testpass")
print(interop_client.get_teams())