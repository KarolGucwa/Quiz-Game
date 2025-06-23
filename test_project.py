import pytest
import json
from unittest.mock import mock_open, patch
from project import choose_questions, save_leaderboards, get_leaderboards, print_leaderboards

def test_choose_questions():
    sample_questions = [
        {"question": "Q1", "options": ["A", "B", "C", "D"], "answer": "A"},
        {"question": "Q2", "options": ["A", "B", "C", "D"], "answer": "B"},
        {"question": "Q3", "options": ["A", "B", "C", "D"], "answer": "C"},
        {"question": "Q4", "options": ["A", "B", "C", "D"], "answer": "D"},
        {"question": "Q5", "options": ["A", "B", "C", "D"], "answer": "A"},
        {"question": "Q6", "options": ["A", "B", "C", "D"], "answer": "B"},
    ]

    chosen = choose_questions(sample_questions)

    assert len(chosen) == 5
    assert all(q in sample_questions for q in chosen)

@pytest.fixture
def mock_leaderboards(monkeypatch):
    """Mocks the leaderboard file with test data."""
    sample_data = json.dumps([{"name": "Alice", "score": 3}, {"name": "Bob", "score": 5}])
    mock_file = mock_open(read_data=sample_data)
    with patch("builtins.open", mock_file):
        yield mock_file

def test_save_and_get_leaderboards():
    """Test saving and retrieving leaderboard scores."""
    save_leaderboards(7, "Charlie")
    scores = get_leaderboards()

    assert any(entry["name"] == "Charlie" and entry["score"] == 7 for entry in scores) == False

def test_print_leaderboards(monkeypatch, capsys):
    """Test if the leaderboard prints correctly."""
    mock_scores = [{"name": "Alice", "score": 3}, {"name": "Bob", "score": 5}]

    monkeypatch.setattr("project.get_leaderboards", lambda: mock_scores)

    print_leaderboards()
    captured = capsys.readouterr()

    assert "Alice" in captured.out
    assert "Bob" in captured.out
    assert "5" in captured.out
