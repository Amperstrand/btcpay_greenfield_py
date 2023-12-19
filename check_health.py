from btcpay_greenfield_py import configuration
from btcpay_greenfield_py import api_client

from btcpay_greenfield_py.api.health_api import HealthApi
from btcpay_greenfield_py.rest import ApiException
from pprint import pprint

# Configure the host to your server
config = configuration.Configuration(
    host = "https://signet.demo.btcpayserver.org"
)

# Create an instance of the API client
with api_client.ApiClient(config) as api_client_instance:
    # Create an instance of the HealthApi class
    api_instance = HealthApi(api_client_instance)
    
    try:
        # Call the health check method
        response = api_instance.health_get_health()
        pprint(response)
    except ApiException as e:
        print("Exception when calling HealthApi->health_get_health: %s\n" % e)
