"""Tests for voting functions."""

import pytest
from potential_winner.voting import (
    plurality_winner,
    borda_count_winner,
    get_potential_winners,
)


class TestPluralityWinner:
    """Tests for plurality_winner function."""
    
    def test_plurality_winner_simple(self):
        """Test simple plurality winner with clear winner."""
        votes = ["Alice", "Bob", "Alice", "Charlie", "Alice"]
        result = plurality_winner(votes)
        assert result == ["Alice"]
    
    def test_plurality_winner_tie_returns_one(self):
        """Test plurality winner with a tie returns all tied winners."""
        votes = ["Alice", "Bob", "Alice", "Bob"]
        result = plurality_winner(votes)
        assert set(result) == {"Alice", "Bob"}
        assert len(result) == 2
    
    def test_plurality_winner_three_way_tie(self):
        """Test plurality winner with three-way tie."""
        votes = ["Alice", "Bob", "Charlie"]
        result = plurality_winner(votes)
        assert set(result) == {"Alice", "Bob", "Charlie"}
        assert len(result) == 3
    
    def test_plurality_winner_empty(self):
        """Test plurality winner with empty votes."""
        votes = []
        result = plurality_winner(votes)
        assert result == []


class TestBordaCountWinner:
    """Tests for borda_count_winner function."""
    
    def test_borda_count_simple(self):
        """Test simple Borda count with clear winner."""
        preferences = [
            ["Alice", "Bob", "Charlie"],
            ["Alice", "Charlie", "Bob"],
            ["Bob", "Alice", "Charlie"],
        ]
        result = borda_count_winner(preferences)
        assert result == ["Alice"]
    
    def test_borda_count_tie(self):
        """Test Borda count with a tie."""
        preferences = [
            ["Alice", "Bob"],
            ["Bob", "Alice"],
        ]
        result = borda_count_winner(preferences)
        assert set(result) == {"Alice", "Bob"}
        assert len(result) == 2
    
    def test_borda_count_empty(self):
        """Test Borda count with empty preferences."""
        preferences = []
        result = borda_count_winner(preferences)
        assert result == []


class TestGetPotentialWinners:
    """Tests for get_potential_winners function."""
    
    def test_get_potential_winners_plurality(self):
        """Test get_potential_winners with plurality method."""
        votes = ["Alice", "Bob", "Alice", "Charlie", "Alice"]
        result = get_potential_winners(votes, method="plurality")
        assert result == ["Alice"]
    
    def test_get_potential_winners_plurality_tie(self):
        """Test get_potential_winners with plurality method and tie."""
        votes = ["Alice", "Bob", "Alice", "Bob"]
        result = get_potential_winners(votes, method="plurality")
        assert set(result) == {"Alice", "Bob"}
        assert len(result) == 2
    
    def test_get_potential_winners_borda(self):
        """Test get_potential_winners with Borda count method."""
        preferences = [
            ["Alice", "Bob", "Charlie"],
            ["Alice", "Charlie", "Bob"],
            ["Bob", "Alice", "Charlie"],
        ]
        result = get_potential_winners(preferences, method="borda")
        assert result == ["Alice"]
    
    def test_get_potential_winners_borda_tie(self):
        """Test get_potential_winners with Borda method and tie."""
        preferences = [
            ["Alice", "Bob"],
            ["Bob", "Alice"],
        ]
        result = get_potential_winners(preferences, method="borda")
        assert set(result) == {"Alice", "Bob"}
        assert len(result) == 2
    
    def test_get_potential_winners_invalid_method(self):
        """Test get_potential_winners with invalid method."""
        votes = ["Alice", "Bob"]
        with pytest.raises(ValueError, match="Unsupported voting method"):
            get_potential_winners(votes, method="invalid")
    
    def test_get_potential_winners_default_method(self):
        """Test get_potential_winners with default method (plurality)."""
        votes = ["Alice", "Bob", "Alice"]
        result = get_potential_winners(votes)
        assert result == ["Alice"]
