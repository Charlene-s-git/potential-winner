"""Tests for voting module."""

import pytest
from potential_winner.voting import (
    plurality_winner,
    plurality_counts,
    borda_count_winner,
    borda_count_scores,
    get_potential_winners,
)


class TestPluralityVoting:
    """Test plurality voting methods."""
    
    def test_plurality_winner_simple(self):
        """Test plurality winner with clear majority."""
        votes = ["Alice", "Bob", "Alice", "Alice", "Charlie"]
        assert plurality_winner(votes) == "Alice"
    
    def test_plurality_winner_tie_returns_one(self):
        """Test that plurality winner returns one winner even in a tie."""
        votes = ["Alice", "Bob", "Alice", "Bob"]
        winner = plurality_winner(votes)
        assert winner in ["Alice", "Bob"]
    
    def test_plurality_winner_single_vote(self):
        """Test plurality winner with single vote."""
        votes = ["Alice"]
        assert plurality_winner(votes) == "Alice"
    
    def test_plurality_winner_empty_raises(self):
        """Test that empty votes raises ValueError."""
        with pytest.raises(ValueError, match="Votes list cannot be empty"):
            plurality_winner([])
    
    def test_plurality_counts(self):
        """Test vote counting."""
        votes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
        counts = plurality_counts(votes)
        assert counts == {"Alice": 3, "Bob": 2, "Charlie": 1}
    
    def test_plurality_counts_empty(self):
        """Test vote counting with empty list."""
        assert plurality_counts([]) == {}


class TestBordaCount:
    """Test Borda count voting methods."""
    
    def test_borda_count_winner_simple(self):
        """Test Borda count with clear winner."""
        preferences = [
            ["Alice", "Bob", "Charlie"],
            ["Alice", "Charlie", "Bob"],
            ["Bob", "Alice", "Charlie"],
        ]
        # Alice: (2 + 2 + 1) = 5
        # Bob: (1 + 0 + 2) = 3
        # Charlie: (0 + 1 + 0) = 1
        assert borda_count_winner(preferences) == "Alice"
    
    def test_borda_count_winner_different_order(self):
        """Test Borda count with different preference orders."""
        preferences = [
            ["Charlie", "Bob", "Alice"],
            ["Charlie", "Alice", "Bob"],
            ["Charlie", "Bob", "Alice"],
        ]
        # Charlie gets most first-place votes
        assert borda_count_winner(preferences) == "Charlie"
    
    def test_borda_count_single_preference(self):
        """Test Borda count with single preference list."""
        preferences = [["Alice", "Bob", "Charlie"]]
        assert borda_count_winner(preferences) == "Alice"
    
    def test_borda_count_empty_raises(self):
        """Test that empty preferences raises ValueError."""
        with pytest.raises(ValueError, match="Preferences list cannot be empty"):
            borda_count_winner([])
    
    def test_borda_count_scores(self):
        """Test Borda count score calculation."""
        preferences = [
            ["Alice", "Bob", "Charlie"],
            ["Bob", "Alice", "Charlie"],
        ]
        scores = borda_count_scores(preferences)
        # Alice: (2 + 1) = 3
        # Bob: (1 + 2) = 3
        # Charlie: (0 + 0) = 0
        assert scores == {"Alice": 3, "Bob": 3, "Charlie": 0}
    
    def test_borda_count_scores_empty(self):
        """Test Borda count scores with empty list."""
        assert borda_count_scores([]) == {}


class TestGetPotentialWinners:
    """Test the main get_potential_winners function."""
    
    def test_get_potential_winners_plurality(self):
        """Test get_potential_winners with plurality method."""
        votes = ["Alice", "Bob", "Alice", "Charlie"]
        assert get_potential_winners(votes, method="plurality") == "Alice"
    
    def test_get_potential_winners_default_method(self):
        """Test that default method is plurality."""
        votes = ["Alice", "Bob", "Alice"]
        assert get_potential_winners(votes) == "Alice"
    
    def test_get_potential_winners_unsupported_method(self):
        """Test that unsupported method raises ValueError."""
        votes = ["Alice", "Bob"]
        with pytest.raises(ValueError, match="Unsupported voting method"):
            get_potential_winners(votes, method="invalid")
    
    def test_get_potential_winners_empty_raises(self):
        """Test that empty votes raises ValueError."""
        with pytest.raises(ValueError, match="Votes list cannot be empty"):
            get_potential_winners([])
