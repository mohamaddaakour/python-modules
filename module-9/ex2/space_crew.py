from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_rules(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        if not any(m.rank in {Rank.commander, Rank.captain} for m in self.crew):
            raise ValueError("Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced = sum(m.years_experience >= 5 for m in self.crew)
            if experienced < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew"
                )

        if not all(m.is_active for m in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    crew = [
        CrewMember(
            member_id="001",
            name="Sarah",
            rank="commander",
            age=40,
            specialization="Command",
            years_experience=10,
        )
    ]

    mission = SpaceMission(
        mission_id="M001",
        mission_name="Mars Mission",
        destination="Mars",
        launch_date="2025-01-01T00:00:00",
        duration_days=300,
        crew=crew,
        budget_millions=500.0,
    )

    print("Valid mission:")
    print(mission)

    print("=" * 40)

    try:
        SpaceMission(
            mission_id="X001",
            mission_name="Bad Mission",
            destination="Mars",
            launch_date="2025-01-01T00:00:00",
            duration_days=100,
            crew=crew,
            budget_millions=500.0,
        )
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()