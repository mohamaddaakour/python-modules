#!/usr/bin/env python3
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List
from enum import Enum

class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"

class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True

class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        if not any(m.rank in [Rank.commander, Rank.captain] for m in self.crew):
            raise ValueError("Need Commander or Captain")
        if self.duration_days > 365:
            exp_ratio = sum(1 for m in self.crew if m.years_experience >= 5) / len(self.crew)
            if exp_ratio < 0.5:
                raise ValueError(f"Long missions need 50% experienced crew")
        if any(not m.is_active for m in self.crew):
            raise ValueError("All crew must be active")
        return self

print("Space Mission Validation\n" + "="*70)

# Valid mission
mission = SpaceMission(mission_id="M2024_MARS", mission_name="Mars Colony",
    destination="Mars", launch_date="2024-06-15T09:00:00", duration_days=900,
    budget_millions=2500.0, crew=[
        CrewMember(member_id="CM001", name="Sarah Connor", rank=Rank.commander,
                   age=45, specialization="Command", years_experience=15),
        CrewMember(member_id="CM002", name="John Smith", rank=Rank.lieutenant,
                   age=38, specialization="Navigation", years_experience=10)
    ])
print(f"\nValid: {mission.mission_name} - {len(mission.crew)} crew - {mission.duration_days} days")

# Invalid mission
try:
    bad = SpaceMission(mission_id="M2024_BAD", mission_name="Test", destination="Moon",
        launch_date="2024-08-01T10:00:00", duration_days=180, budget_millions=800.0,
        crew=[CrewMember(member_id="CM003", name="Bob", rank=Rank.officer,
                         age=30, specialization="Research", years_experience=5)])
except ValidationError as e:
    print(f"\nValidation error: {e.errors()[0]['msg']}")
