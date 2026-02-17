#!/usr/bin/env python3
"""
Space Station Data Validation using Pydantic

Installation: pip install pydantic
"""

try:
    from pydantic import BaseModel, Field, ValidationError
    from datetime import datetime
    from typing import Optional

    class SpaceStation(BaseModel):
        """Model for validating space station data"""

        station_id: str = Field(..., min_length=3, max_length=10)
        name: str = Field(..., min_length=1, max_length=50)
        crew_size: int = Field(..., ge=1, le=20)
        power_level: float = Field(..., ge=0.0, le=100.0)
        oxygen_level: float = Field(..., ge=0.0, le=100.0)
        last_maintenance: datetime
        is_operational: bool = True
        notes: Optional[str] = Field(None, max_length=200)

    PYDANTIC_AVAILABLE = True

except ImportError:
    PYDANTIC_AVAILABLE = False


def main():
    """Demonstrate space station validation"""

    if not PYDANTIC_AVAILABLE:
        print("ERROR: pydantic is not installed!")
        print("Install it with: pip install pydantic\n")
        print("=" * 70)
        show_example_output()
        return

    print("Space Station Data Validation")
    print("=" * 70)

    # Create a valid space station
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-01-15T10:30:00",
            is_operational=True,
            notes="All systems nominal"
        )

        print("\nValid station created:")
        print(f"  ID: {station.station_id}")
        print(f"  Name: {station.name}")
        print(f"  Crew: {station.crew_size} people")
        print(f"  Power: {station.power_level}%")
        print(f"  Oxygen: {station.oxygen_level}%")
        print(f"  Last Maintenance: {station.last_maintenance}")
        print(f"  Status: {'Operational' if station.is_operational else 'Non-operational'}")
        if station.notes:
            print(f"  Notes: {station.notes}")

    except ValidationError as e:
        print(f"\nUnexpected validation error: {e}")

    # Attempt to create invalid station
    print("\n" + "=" * 70)
    print("\nAttempting to create invalid station (crew_size > 20)...")

    try:
        invalid_station = SpaceStation(
            station_id="BAD001",
            name="Invalid Station",
            crew_size=25,  # Too many crew!
            power_level=75.0,
            oxygen_level=88.0,
            last_maintenance="2024-01-15T10:30:00"
        )
    except ValidationError as e:
        print("\nExpected validation error:")
        for error in e.errors():
            print(f"  Field: {error['loc'][0]}")
            print(f"  Error: {error['msg']}")

    print("\n" + "=" * 70)


def show_example_output():
    """Show expected output when pydantic is available"""
    print("EXAMPLE OUTPUT (install pydantic to see real validation):\n")
    print("Space Station Data Validation")
    print("=" * 70)
    print("\nValid station created:")
    print("  ID: ISS001")
    print("  Name: International Space Station")
    print("  Crew: 6 people")
    print("  Power: 85.5%")
    print("  Oxygen: 92.3%")
    print("  Last Maintenance: 2024-01-15 10:30:00")
    print("  Status: Operational")
    print("  Notes: All systems nominal")
    print("\n" + "=" * 70)
    print("\nAttempting to create invalid station (crew_size > 20)...")
    print("\nExpected validation error:")
    print("  Error: Input should be less than or equal to 20")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
