from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings class to load environment variables.
    """

    docusign_account_id: str
    docusign_auth_token: str
    docusign_integration_key: str
    database_path: str
    docusign_base_path: str = "https://demo.docusign.net/restapi"
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'



    # Initialize the settings
settings = Settings() # type: ignore

if __name__ == "__main__":
    print(f"Docusign Account ID: {settings.docusign_account_id}")
    print(f"Docusign Auth Token: {settings.docusign_auth_token}")
    print(f"Docusign Integration Key: {settings.docusign_integration_key}")
    print(f"Database Path: {settings.database_path}")
    print(f"Docusign Base Path: {settings.docusign_base_path}")