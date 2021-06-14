import datetime
from copy import deepcopy
from logging import StreamHandler, LogRecord
from .service_provider import provide
from .log_service import AzureLogService
from .utils import setlocale


class AzureLogServiceHandler(StreamHandler):
    _RFC1123DATE_WITH_MICRO = "%a, %d %b %Y %H:%M:%S.%f GMT"

    def __init__(self):
        self._log_service: AzureLogService = provide(AzureLogService)
        super().__init__()

    def emit(self, record: LogRecord) -> None:
        message = self.format(record)
        with setlocale("C"):
            rfc1123date = datetime.datetime.utcnow().strftime(self._RFC1123DATE_WITH_MICRO)
        record_data = dict()
        if hasattr(record, "custom_record_data") and isinstance(record.custom_record_data, dict):
            record_data = deepcopy(record.custom_record_data)
        record_data.update(dict(
            level=record.levelname,
            message=message,
            time=rfc1123date,
            module=record.module,
            file_name=record.filename,
            line_number=record.lineno,
            thread_name=record.threadName,
            process_name=record.processName,
            process_pid=record.process,
            func_name=record.funcName,
        ))
        self._log_service.add_record(record_data)
