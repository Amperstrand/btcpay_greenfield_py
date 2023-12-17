import openapi_client
from openapi_client.api.health_api import HealthApi
from openapi_client.rest import ApiException
from pprint import pprint

# Configure the host to your server
configuration = openapi_client.Configuration(
    host = "https://https://signet.demo.btcpayserver.org/"
)

# Create an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the HealthApi class
    api_instance = HealthApi(api_client)
    
    try:
        # Call the health check method
        response = api_instance.health_get_health()
        pprint(response)
    except ApiException as e:
        print("Exception when calling HealthApi->health_get_health: %s\n" % e)
