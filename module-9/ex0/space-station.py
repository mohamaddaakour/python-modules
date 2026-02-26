from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    # ... means this field is required
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    print("Space Station Data Validation")
    print("=" * 40)

    # Valid station
    try:
        # we create an instance
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2026-02-20T14:30:00",
        )

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(f"Status: {'Operational' if station.is_operational else 'Not Operational'}")

    except ValidationError as e:
        print("Validation failed:", e)

    print("=" * 40)

    # invalid case
    try:
        invalid_station = SpaceStation(
            station_id="BAD001",
            name="Overcrowded Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=70.0,
            last_maintenance=datetime.now(),
        )

    except ValidationError as e:
        print("Expected validation error:")
        print(e)


if __name__ == "__main__":
    main()