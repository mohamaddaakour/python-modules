#!/usr/bin/env python3
"""
Alien Contact Logs - Custom Validation with Pydantic

Installation: pip install pydantic
"""

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
    from datetime import datetime
    from typing import Optional
    from enum import Enum

    class ContactType(Enum):
        """Types of alien contact"""
        radio = "radio"
        visual = "visual"
        physical = "physical"
        telepathic = "telepathic"

    class AlienContact(BaseModel):
        """Model for validating alien contact reports"""

        contact_id: str = Field(..., min_length=5, max_length=15)
        timestamp: datetime
        location: str = Field(..., min_length=3, max_length=100)
        contact_type: ContactType
        signal_strength: float = Field(..., ge=0.0, le=10.0)
        duration_minutes: int = Field(..., ge=1, le=1440)
        witness_count: int = Field(..., ge=1, le=100)
        message_received: Optional[str] = Field(None, max_length=500)
        is_verified: bool = False

        @model_validator(mode='after')
        def validate_contact_rules(self):
            """Custom validation rules for alien contact reports"""

            # Rule 1: Contact ID must start with "AC"
            if not self.contact_id.startswith("AC"):
                raise ValueError("Contact ID must start with 'AC' (Alien Contact)")

            # Rule 2: Physical contact reports must be verified
            if self.contact_type == ContactType.physical and not self.is_verified:
                raise ValueError("Physical contact reports must be verified")

            # Rule 3: Telepathic contact requires at least 3 witnesses
            if self.contact_type == ContactType.telepathic and self.witness_count < 3:
                raise ValueError("Telepathic contact requires at least 3 witnesses")

            # Rule 4: Strong signals (> 7.0) should include received messages
            if self.signal_strength > 7.0 and not self.message_received:
                raise ValueError("Strong signals (>7.0) should include received messages")

            return self

    PYDANTIC_AVAILABLE = True

except ImportError:
    PYDANTIC_AVAILABLE = False


def main():
    """Demonstrate alien contact validation"""

    if not PYDANTIC_AVAILABLE:
        print("ERROR: pydantic is not installed!")
        print("Install it with: pip install pydantic\n")
        print("=" * 70)
        show_example_output()
        return

    print("Alien Contact Log Validation")
    print("=" * 70)

    # Test 1: Valid radio contact
    print("\nTest 1: Valid radio contact with message")
    try:
        contact1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp="2024-01-15T22:30:00",
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True
        )

        print("✓ Valid contact report:")
        print(f"  ID: {contact1.contact_id}")
        print(f"  Type: {contact1.contact_type.value}")
        print(f"  Location: {contact1.location}")
        print(f"  Signal: {contact1.signal_strength}/10")
        print(f"  Duration: {contact1.duration_minutes} minutes")
        print(f"  Witnesses: {contact1.witness_count}")
        print(f"  Message: '{contact1.message_received}'")
        print(f"  Verified: {contact1.is_verified}")

    except ValidationError as e:
        print(f"✗ Unexpected error: {e}")

    # Test 2: Invalid - Contact ID doesn't start with AC
    print("\n" + "=" * 70)
    print("\nTest 2: Invalid contact ID (doesn't start with 'AC')")
    try:
        contact2 = AlienContact(
            contact_id="UFO_2024_001",
            timestamp="2024-01-15T22:30:00",
            location="Roswell, New Mexico",
            contact_type=ContactType.visual,
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=10
        )
    except ValidationError as e:
        print("✓ Expected validation error:")
        for error in e.errors():
            print(f"  {error['msg']}")

    # Test 3: Invalid - Telepathic contact with too few witnesses
    print("\n" + "=" * 70)
    print("\nTest 3: Telepathic contact with insufficient witnesses")
    try:
        contact3 = AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-01-16T03:15:00",
            location="Sedona, Arizona",
            contact_type=ContactType.telepathic,
            signal_strength=6.0,
            duration_minutes=120,
            witness_count=2  # Too few!
        )
    except ValidationError as e:
        print("✓ Expected validation error:")
        for error in e.errors():
            print(f"  {error['msg']}")

    # Test 4: Invalid - Physical contact not verified
    print("\n" + "=" * 70)
    print("\nTest 4: Physical contact without verification")
    try:
        contact4 = AlienContact(
            contact_id="AC_2024_003",
            timestamp="2024-01-17T01:45:00",
            location="Phoenix Lights Zone",
            contact_type=ContactType.physical,
            signal_strength=9.0,
            duration_minutes=15,
            witness_count=1,
            message_received="They touched the ship",
            is_verified=False  # Not verified!
        )
    except ValidationError as e:
        print("✓ Expected validation error:")
        for error in e.errors():
            print(f"  {error['msg']}")

    # Test 5: Invalid - Strong signal without message
    print("\n" + "=" * 70)
    print("\nTest 5: Strong signal without received message")
    try:
        contact5 = AlienContact(
            contact_id="AC_2024_004",
            timestamp="2024-01-18T20:00:00",
            location="SETI Array, California",
            contact_type=ContactType.radio,
            signal_strength=9.5,  # Very strong!
            duration_minutes=60,
            witness_count=12,
            message_received=None  # No message!
        )
    except ValidationError as e:
        print("✓ Expected validation error:")
        for error in e.errors():
            print(f"  {error['msg']}")

    print("\n" + "=" * 70)


def show_example_output():
    """Show expected output when pydantic is available"""
    print("EXAMPLE OUTPUT (install pydantic to see real validation):\n")
    print("Alien Contact Log Validation")
    print("=" * 70)
    print("\nTest 1: Valid radio contact with message")
    print("✓ Valid contact report:")
    print("  ID: AC_2024_001")
    print("  Type: radio")
    print("  Location: Area 51, Nevada")
    print("  Signal: 8.5/10")
    print("  Duration: 45 minutes")
    print("  Witnesses: 5")
    print("  Message: 'Greetings from Zeta Reticuli'")
    print("  Verified: True")
    print("\n" + "=" * 70)
    print("\nTest 2: Invalid contact ID (doesn't start with 'AC')")
    print("✓ Expected validation error:")
    print("  Contact ID must start with 'AC' (Alien Contact)")
    print("\n" + "=" * 70)
    print("\nTest 3: Telepathic contact with insufficient witnesses")
    print("✓ Expected validation error:")
    print("  Telepathic contact requires at least 3 witnesses")
    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
