import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_github_skills_activity_exists_and_allows_signup():
    activity_name = "GitHub Skills"

    response = client.get("/activities")
    assert response.status_code == 200
    activities = response.json()
    assert activity_name in activities

    signup_response = client.post(
        f"/activities/{activity_name}/signup?email=teststudent@mergington.edu"
    )
    assert signup_response.status_code == 200
    assert signup_response.json()["message"] == (
        f"Signed up teststudent@mergington.edu for {activity_name}"
    )
