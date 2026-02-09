from abc import ABC, abstractmethod
from typing import Any, List, Optional

# to use abstract method we have to inherit from ABC
class DataProcessor(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("Initializing Numeric Processor...")

    def validate(self, data: Any) -> bool:
        # to check if all the elements in the list are int or float
        if isinstance(data, list) and all(isinstance(x, (int, float)) for x in data):
            print("Validation: Numeric data verified")
            return True
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")

            total = sum(data)
            count = len(data)
            avg = total / count if count > 0 else 0

            return f"Processed {count} numeric values, sum={total}, avg={avg}"

        except Exception as e:
            return f"Numeric processing error: {e}"


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("Initializing Text Processor...")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            print("Validation: Text data verified")
            return True
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            char_count = len(data)
            word_count = len(data.split())

            return f"Processed text: {char_count} characters, {word_count} words"

        except Exception as e:
            return f"Text processing error: {e}"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("Initializing Log Processor...")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) and ":" in data:
            print("Validation: Log entry verified")
            return True
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")

            level, message = data.split(":", 1)
            level = level.strip().upper()
            message = message.strip()

            return f"[{level}] {level} level detected: {message}"

        except Exception as e:
            return f"Log processing error: {e}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("")

    # create an instance of NummericProcessor
    num_processor = NumericProcessor()

    print("Processing data:", [1, 2, 3, 4, 5])
    result = num_processor.process([1, 2, 3, 4, 5])
    print(num_processor.format_output(result))

    print("")

    # create an instance of TextProcessor
    text_processor = TextProcessor()

    print('Processing data: "Hello Nexus World"')
    result = text_processor.process("Hello Nexus World")
    print(text_processor.format_output(result))

    print("")

    # create an instance of LogProcessor
    log_processor = LogProcessor()

    print('Processing data: "ERROR: Connection timeout"')
    result = log_processor.process("ERROR: Connection timeout")
    print(log_processor.format_output(result))

    print("")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_samples: List[Any] = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    for i, (processor, data) in enumerate(zip(processors, data_samples), start=1):
        result = processor.process(data)
        print(f"Result {i}: {result}")

    print("")

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
