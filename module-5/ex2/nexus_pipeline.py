from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Protocol
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []
        self.processed = 0

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        self.processed += 1
        return data

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data["processed"] = True
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        return f"Output: {data}"


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        return self.run(data)


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        return self.run(data)


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> str:
        return self.run(data)


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def register(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def execute_all(self, data: Any) -> None:
        for pipeline in self.pipelines:
            start = time.time()
            result = pipeline.process(data)
            elapsed = time.time() - start
            print(
                f"Pipeline {pipeline.pipeline_id} -> {result} "
                f"({elapsed:.4f}s)"
            )


def main() -> None:
    pipeline = JSONAdapter("P1")
    pipeline.add_stage(InputStage())
    pipeline.add_stage(TransformStage())
    pipeline.add_stage(OutputStage())

    manager = NexusManager()
    manager.register(pipeline)

    manager.execute_all({"sensor": "temp", "value": 23.5})


if __name__ == "__main__":
    main()
