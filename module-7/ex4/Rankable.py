"""
Rankable - Simple ranking interface
Defines ranking and tournament tracking capabilities
"""

from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Abstract interface for ranking and tournament tracking.
    
    Classes implementing this interface can:
    - Calculate their competitive rating
    - Track wins and losses
    - Provide ranking information
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calculate the current competitive rating.
        
        Returns:
            int: Current rating (e.g., 1200 for starting rating)
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update the win count.
        
        Args:
            wins: Number of wins to add
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update the loss count.
        
        Args:
            losses: Number of losses to add
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Get ranking information.
        
        Returns:
            dict: Ranking info including rating, wins, losses, etc.
        """
        pass