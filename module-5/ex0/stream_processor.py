from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        numbers: List[float] = list(map(float, data))
        total = sum(numbers)
        avg = total / len(numbers)
        return f"Processed {len(numbers)} numeric values, sum={total}, avg={avg}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(isinstance(x, (int, float)) for x in data)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        text: str = data
        chars = len(text)
        words = len(text.split())
        return f"Processed text: {chars} characters, {words} words"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log entry")

        level, message = data.split(":", 1)
        return f"[{level}] {level} level detected:{message}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data


def main() -> None:
    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]

    inputs = [
        [1, 2, 3],
        "Hello Nexus",
        "INFO:System ready",
    ]

    for processor, data in zip(processors, inputs):
        result = processor.process(data)
        print(processor.format_output(result))


if __name__ == "__main__":
    main()
