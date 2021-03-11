import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AzureLogServiceConfiguration:
    customer_id: str
    shared_key: str
    default_log_type: str
    send_frequency: int
    single_request_timeout: int

    @staticmethod
    def build() -> "AzureLogServiceConfiguration":
        customer_id: str = os.getenv("AZURE_LOG_CUSTOMER_ID", "")
        shared_key: str = os.getenv("AZURE_LOG_SHARED_KEY", "")
        default_log_type: str = os.getenv("AZURE_LOG_DEFAULT_NAME", "")
        send_frequency: int = int(os.getenv("AZURE_LOG_SEND_FREQUENCY", 5))
        single_request_timeout: int = int(os.getenv("AZURE_LOG_SINGLE_REQUEST_TIMEOUT", 5))

        return AzureLogServiceConfiguration(
            customer_id=customer_id,
            shared_key=shared_key,
            default_log_type=default_log_type,
            send_frequency=send_frequency,
            single_request_timeout=single_request_timeout,
        )
