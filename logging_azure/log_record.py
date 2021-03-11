from typing import Optional
from requests import Response, Request
from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


@dataclass
class AzureLogRecord(DataClassJsonMixin):
    id: str
    level: str
    time: str
    message: str
    module: str
    file_name: str
    line_number: int
    thread_name: str
    process_name: str
    process_pid: int
    func_name: str

    log_request: Optional[Request] = None
    log_response: Optional[Response] = None

    def __hash__(self):
        return hash(self.id)
