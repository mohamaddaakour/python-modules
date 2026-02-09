from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


# abstract class
class DataStream(ABC):
    # constructor
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str,int,float]]:
        return {"stream_id": self.stream_id, "processed_count": self.processed_count}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print(f"\nInitializing Sensor Stream...\nStream ID: {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count = len(data_batch)
            temp_readings = [x['temp'] for x in data_batch if isinstance(x, dict) and 'temp' in x]
            avg_temp = sum(temp_readings)/len(temp_readings) if temp_readings else 0
            return f"Sensor analysis: {self.processed_count} readings processed, avg temp: {avg_temp:.1f}°C"
        except Exception as e:
            return f"Sensor processing error: {e}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return [d for d in data_batch if isinstance(d, dict) and d.get('alert', False)]
        return data_batch


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print(f"\nInitializing Transaction Stream...\nStream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count = len(data_batch)
            net_flow = sum([x['amount'] if x['type']=='buy' else -x['amount']
                            for x in data_batch if isinstance(x, dict) and 'type' in x and 'amount' in x])
            return f"Transaction analysis: {self.processed_count} operations, net flow: {net_flow:+} units"
        except Exception as e:
            return f"Transaction processing error: {e}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            return [d for d in data_batch if isinstance(d, dict) and d.get('amount',0) > 100]
        return data_batch

class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        print(f"\nInitializing Event Stream...\nStream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            self.processed_count = len(data_batch)
            error_count = sum(1 for e in data_batch if isinstance(e,str) and e.lower() == "error")
            return f"Event analysis: {self.processed_count} events, {error_count} error(s) detected"
        except Exception as e:
            return f"Event processing error: {e}"

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == "critical":
            return [e for e in data_batch if isinstance(e,str) and e.lower() in ("error","critical")]
        return data_batch


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def process_all(self, batches: List[List[Any]]) -> None:
        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")

        print("")

        for i, (stream, batch) in enumerate(zip(self.streams, batches), start=1):
            result = stream.process_batch(batch)
            print(f"Batch {i} Results:\n- {result}")

    def filter_streams(self, criteria: Optional[str] = None) -> None:
        print(f"Stream filtering active: {criteria} data only")
        for stream in self.streams:
            filtered = stream.filter_data([], criteria)
            print(f"Filtered results: {len(filtered)} items for {stream.stream_id}")

def main() -> None:
    # create instances
    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    sensor_batch = [{'temp':22.5,'humidity':65,'pressure':1013},
                    {'temp':23.0,'humidity':60,'pressure':1012},
                    {'temp':22.5,'humidity':64,'pressure':1011}]
    transaction_batch = [{'type':'buy','amount':100},
                         {'type':'sell','amount':150},
                         {'type':'buy','amount':75}]
    event_batch = ["login", "error", "logout"]

    print(f"Processing sensor batch: {sensor_batch}")
    print(sensor_stream.process_batch(sensor_batch))

    print(f"Processing transaction batch: {transaction_batch}")
    print(transaction_stream.process_batch(transaction_batch))

    print(f"Processing event batch: {event_batch}")
    print(event_stream.process_batch(event_batch))

    processor = StreamProcessor([sensor_stream, transaction_stream, event_stream])
    processor.process_all([sensor_batch, transaction_batch, event_batch])
    processor.filter_streams("High-priority")

    print("")

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("")

    main()
