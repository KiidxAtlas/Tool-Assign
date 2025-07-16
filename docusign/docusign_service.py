import base64
from docusign_esign import Document, EnvelopesApi, EnvelopeDefinition, Signer, SignHere, Tabs
from docusign_esign.client.api_client import ApiClient
from config.config import Settings

# Load configuration
settings = Settings()  # type: ignore

# Initialize DocuSign API client
api_client = ApiClient()
api_client.set_base_path(settings.docusign_base_path)
api_client.set_default_header("Authorization", f"Bearer {settings.docusign_auth_token}")


# Create an instance of the Envelopes API
envelopes_api = EnvelopesApi(api_client)

# HTML content for the document
html_content = """
<html>
<body>
<h1>Order Acknowledgement</h1>
<p>Thank you for your order!</p>
<p>Best regards,</p>
<p>Your Company</p>
</body>
</html>
"""

def create_document():
    """ Creates a document in DocuSign"""
    document = Document(
        document_base64=base64.b64encode(bytes(html_content, "utf-8")).decode("ascii"),
        name="Order acknowledgement",
        file_extension="html",
        document_id="1"
    )
    return document

def create_envelope():
    """ Creates an envelope with the document and a signer"""
    document = create_document()
    
    # Create a signer
    signer = Signer(
        email="epung0716@gmail.com",
        name="John Doe",
        recipient_id="1",
        routing_order="1"
    )
    
    # Create a sign here tab
    sign_here = SignHere(
        anchor_string="**signature**",
        anchor_units="pixels",
        anchor_x_offset="20",
        anchor_y_offset="10"
    )
    
    # Add the sign here tab to the signer
    tabs = Tabs(sign_here_tabs=[sign_here])
    signer.tabs = tabs
    
    # Create the envelope definition
    envelope_definition = EnvelopeDefinition(
        email_subject="Please sign this document",
        documents=[document],
        recipients={"signers": [signer]},
        status="sent"  # Set to "created" to save as draft
    )
    
    return envelope_definition

def send_envelope():
    """ Sends the envelope to the signer"""
    envelope_definition = create_envelope()
    
    # Create and send the envelope
    try:
        envelope_summary = envelopes_api.create_envelope(config.docusign_account_id, envelope_definition=envelope_definition)
        print(f"Envelope created with ID: {envelope_summary.envelope_id}")
    except Exception as e:
        print(f"Error creating envelope: {e}")
        
if __name__ == "__main__":
    print(f"{config.get_docusign_auth_token}")
    send_envelope()
    print("Envelope sent successfully.")
