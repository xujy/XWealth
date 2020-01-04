import os
from plaid import Client
import pprint


# Available environments are 'sandbox', 'development', and 'production'.
client = Client(
	client_id=os.environ['PLAID_CLIENT_ID'],
	secret=os.environ['PLAID_SECRET'],
	public_key=os.environ['PLAID_PUBLIC_KEY'],
	environment=os.environ['PLAID_ENV']
)

auth_response = client.Auth.get(os.environ['ACCESS_TOKEN'])
pprint.pprint(auth_response)