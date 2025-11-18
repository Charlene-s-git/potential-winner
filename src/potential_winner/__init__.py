"""potential-winner package."""

__version__ = '0.1.0'

from .voting import (
    plurality_winner,
    plurality_counts,
    borda_count_winner,
    borda_count_scores,
    get_potential_winners,
)

__all__ = [
    'plurality_winner',
    'plurality_counts',
    'borda_count_winner',
    'borda_count_scores',
    'get_potential_winners',
]
