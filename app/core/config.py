from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings using Pydantic.
    """

    TITLE: str
    API_V1_STR: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_IN_DAYS: int = 7

    DATABASE_URL: str
    CORS_ORIGINS: list[str] = ["http://localhost", "http://localhost:3000"]
    CLOUDINARY_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str
    DEFAULT_PROFILE_PIC: str

    class Config:
        env_file = ".env"
        case_sensitive = True


# Instantiate the settings object
settings = Settings()
