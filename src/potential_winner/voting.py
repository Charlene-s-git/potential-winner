"""Voting functions for determining winners under different voting rules."""

from typing import List, Dict
from collections import Counter


def plurality_winner(votes: List[str]) -> List[str]:
    """
    Determine the winner(s) using plurality voting.
    
    Returns all candidates tied for the most votes.
    
    Args:
        votes: A list of votes, where each vote is a candidate name.
        
    Returns:
        A list of candidate names who are tied for the most votes.
    """
    if not votes:
        return []
    
    vote_counts = Counter(votes)
    max_votes = max(vote_counts.values())
    
    # Return all candidates with the maximum number of votes
    return [candidate for candidate, count in vote_counts.items() if count == max_votes]


def borda_count_winner(preferences: List[List[str]]) -> List[str]:
    """
    Determine the winner(s) using Borda count.
    
    In Borda count, each position in a preference list receives points:
    - 1st place: n-1 points (where n is the number of candidates)
    - 2nd place: n-2 points
    - ...
    - Last place: 0 points
    
    Args:
        preferences: A list of preference lists, where each preference list
                    ranks candidates from most to least preferred.
                    
    Returns:
        A list of candidate names who are tied for the most points.
    """
    if not preferences:
        return []
    
    # Get all unique candidates
    all_candidates = set()
    for pref_list in preferences:
        all_candidates.update(pref_list)
    
    num_candidates = len(all_candidates)
    
    # Calculate Borda scores
    scores: Dict[str, int] = {candidate: 0 for candidate in all_candidates}
    
    for pref_list in preferences:
        for position, candidate in enumerate(pref_list):
            # Position 0 gets (n-1) points, position 1 gets (n-2) points, etc.
            points = num_candidates - position - 1
            scores[candidate] += points
    
    # Find the maximum score
    max_score = max(scores.values())
    
    # Return all candidates with the maximum score
    return [candidate for candidate, score in scores.items() if score == max_score]


def get_potential_winners(votes, method: str = "plurality") -> List[str]:
    """
    Get potential winners using the specified voting method.
    
    Args:
        votes: For plurality method, a list of votes (strings).
               For borda method, a list of preference lists (list of lists).
        method: The voting method to use. Either "plurality" or "borda".
        
    Returns:
        A list of potential winners based on the specified method.
        
    Raises:
        ValueError: If an unsupported method is specified.
    """
    if method == "plurality":
        return plurality_winner(votes)
    elif method == "borda":
        return borda_count_winner(votes)
    else:
        raise ValueError(f"Unsupported voting method: {method}")
