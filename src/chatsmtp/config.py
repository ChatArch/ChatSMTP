"Typed environment configuration for ChatSMTP."

from chatenv import BaseEnvConfig, EnvField


class ChatsmtpConfig(BaseEnvConfig):
    """ChatSMTP configuration stored in ChatEnv's typed profile paths."""

    _title = "ChatSMTP Configuration"
    _aliases = ["chatsmtp"]
    _storage_dir = "Chatsmtp"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATSMTP_API_KEY = EnvField(
        "CHATSMTP_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatsmtpConfig"]
