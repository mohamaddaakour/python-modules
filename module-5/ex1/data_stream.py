from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        return f"Sensor data: {len(data_batch)} readings processed"


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        net = sum(data_batch)
        return f"Transaction data: net flow {net}"


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        self.processed_count += len(data_batch)
        errors = sum(1 for e in data_batch if e == "error")
        return f"Event data: {errors} errors detected"


class StreamProcessor:
    def process(self, stream: DataStream, data: List[Any]) -> str:
        return stream.process_batch(data)


def main() -> None:
    streams: List[DataStream] = [
        SensorStream("S1"),
        TransactionStream("T1"),
        EventStream("E1"),
    ]

    batches = [
        [22.5, 23.1],
        [100, -50, 25],
        ["login", "error", "logout"],
    ]

    processor = StreamProcessor()

    for stream, batch in zip(streams, batches):
        print(processor.process(stream, batch))
        print(stream.get_stats())


if __name__ == "__main__":
    main()
