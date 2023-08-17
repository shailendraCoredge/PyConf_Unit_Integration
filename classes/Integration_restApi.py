import uuid
import requests

ENDPOINT = "https://todo.pixegami.io"

# https://todo.pixegami.io/docs

class TaskUtility:

    @staticmethod
    def new_task_payload():
        user_id = f"test_user_{uuid.uuid4().hex}"
        content = f"test_content_{uuid.uuid4().hex}"
        return {
            "content":content,
            "user_id": user_id,
            "is_done":False,
        }

    @staticmethod
    def create(payload):
        return requests.put(ENDPOINT + "/create-task", json=payload)

    @staticmethod
    def update(payload):
        return requests.put(ENDPOINT + "/update-task", json=payload)

    @staticmethod
    def get(task_id):
        return requests.get(ENDPOINT + f"/get-task/{task_id}")

    @staticmethod
    def lists(user_id):
        return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

    @staticmethod
    def delete(task_id):
        return requests.delete(ENDPOINT + f"/delete-task/{task_id}")
