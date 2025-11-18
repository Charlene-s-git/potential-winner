# potential-winner

A Python package for computing potential winners in voting systems under various voting rules.

## Installation

To install the package, run:

```bash
pip install -e .
```

Or install from requirements:

```bash
pip install -r requirements.txt
```

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/Charlene-s-git/potential-winner.git
cd potential-winner
```

2. Install in development mode:
```bash
pip install -e .
```

3. Run tests:
```bash
pytest tests/
```

## Usage

### Plurality Voting (First-Past-The-Post)

Determine the winner based on who receives the most votes:

```python
from potential_winner import plurality_winner, plurality_counts

# Simple plurality voting
votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]
winner = plurality_winner(votes)
print(f"Winner: {winner}")  # Output: Winner: Alice

# Get vote counts for all candidates
counts = plurality_counts(votes)
print(counts)  # Output: {'Alice': 3, 'Bob': 2, 'Charlie': 1}
```

### Borda Count Voting

Determine the winner using ranked preference voting:

```python
from potential_winner import borda_count_winner, borda_count_scores

# Borda count with ranked preferences
preferences = [
    ["Alice", "Bob", "Charlie"],    # Voter 1's ranking
    ["Alice", "Charlie", "Bob"],    # Voter 2's ranking
    ["Bob", "Alice", "Charlie"],    # Voter 3's ranking
]

winner = borda_count_winner(preferences)
print(f"Winner: {winner}")  # Output: Winner: Alice

# Get Borda count scores for all candidates
scores = borda_count_scores(preferences)
print(scores)  # Output: {'Alice': 5, 'Bob': 3, 'Charlie': 1}
```

### Generic Interface

Use the generic `get_potential_winners` function with different methods:

```python
from potential_winner import get_potential_winners

votes = ["Alice", "Bob", "Alice", "Charlie"]

# Using plurality method (default)
winner = get_potential_winners(votes, method="plurality")
print(f"Winner: {winner}")

# Default method is plurality
winner = get_potential_winners(votes)
print(f"Winner: {winner}")
```

## Supported Voting Methods

- **Plurality (First-Past-The-Post)**: The candidate with the most votes wins
- **Borda Count**: Candidates receive points based on their ranking position, and the candidate with the most points wins

## License

See LICENSE file for details.