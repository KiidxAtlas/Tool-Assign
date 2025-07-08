import docusign_esign as docusign

def send_envelope(api_client, envelope_definition):
    """
    Sends an envelope using the DocuSign API.
    
    :param api_client: An instance of docusign.ApiClient configured with authentication.
    :param envelope_definition: The envelope definition to send.
    :return: The sent envelope's status.
    """
    envelopes_api = docusign.EnvelopesApi(api_client)
    results = envelopes_api.create_envelope(account_id=api_client.get_account_id(), envelope_definition=envelope_definition)
    return results.status

if __name__ == "__main__":
    # Example usage
    api_client = docusign.ApiClient()
    api_client.set_base_path("https://demo.docusign.net/restapi")