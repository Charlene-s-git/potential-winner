"""Voting system module for computing potential winners."""

from typing import List, Dict
from collections import Counter


def plurality_winner(votes: List[str]) -> str:
    """
    Determine the winner using plurality (first-past-the-post) voting.
    
    Args:
        votes: List of votes where each vote is a candidate name.
        
    Returns:
        The candidate with the most votes.
        
    Raises:
        ValueError: If votes list is empty.
    """
    if not votes:
        raise ValueError("Votes list cannot be empty")
    
    vote_counts = Counter(votes)
    winner, _ = vote_counts.most_common(1)[0]
    return winner


def plurality_counts(votes: List[str]) -> Dict[str, int]:
    """
    Get vote counts for all candidates.
    
    Args:
        votes: List of votes where each vote is a candidate name.
        
    Returns:
        Dictionary mapping candidate names to their vote counts.
    """
    return dict(Counter(votes))


def _calculate_borda_scores(preferences: List[List[str]]) -> Dict[str, int]:
    """
    Helper function to calculate Borda scores from preferences.
    
    Args:
        preferences: List of ranked preference lists.
        
    Returns:
        Dictionary mapping candidate names to their Borda count scores.
    """
    if not preferences:
        return {}
    
    # Get all unique candidates
    all_candidates = set()
    for pref in preferences:
        all_candidates.update(pref)
    
    num_candidates = len(all_candidates)
    
    # Calculate Borda scores
    scores: Dict[str, int] = {candidate: 0 for candidate in all_candidates}
    
    for pref in preferences:
        for position, candidate in enumerate(pref):
            points = num_candidates - position - 1
            scores[candidate] += points
    
    return scores


def borda_count_winner(preferences: List[List[str]]) -> str:
    """
    Determine the winner using Borda count voting.
    
    In Borda count, each position in a ranked ballot gives points:
    - First choice: n-1 points (where n is number of candidates)
    - Second choice: n-2 points
    - And so on...
    
    Args:
        preferences: List of ranked preference lists, where each preference
                    list contains candidates ordered from most to least preferred.
        
    Returns:
        The candidate with the highest Borda count.
        
    Raises:
        ValueError: If preferences list is empty.
    """
    if not preferences:
        raise ValueError("Preferences list cannot be empty")
    
    scores = _calculate_borda_scores(preferences)
    
    # Find winner (candidate with highest score)
    winner = max(scores.items(), key=lambda x: x[1])[0]
    return winner


def borda_count_scores(preferences: List[List[str]]) -> Dict[str, int]:
    """
    Get Borda count scores for all candidates.
    
    Args:
        preferences: List of ranked preference lists.
        
    Returns:
        Dictionary mapping candidate names to their Borda count scores.
    """
    return _calculate_borda_scores(preferences)


def get_potential_winners(votes: List[str], method: str = "plurality") -> str:
    """
    Determine the potential winner based on the specified voting method.
    
    Args:
        votes: List of votes. For plurality, each vote is a candidate name.
        method: Voting method to use. Currently only "plurality" is supported.
        
    Returns:
        The potential winner according to the specified method.
        
    Raises:
        ValueError: If method is not supported or votes is empty.
    """
    if not votes:
        raise ValueError("Votes list cannot be empty")
    
    if method == "plurality":
        return plurality_winner(votes)
    else:
        raise ValueError(f"Unsupported voting method: {method}")
