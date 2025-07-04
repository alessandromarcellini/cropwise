from google.cloud import firestore
from google.oauth2 import service_account

class FirestoreClient:
    def __init__(self, project_id=None, credentials_path=None):
        if credentials_path:
            credentials = service_account.Credentials.from_service_account_file(credentials_path)
        else:
            credentials = None
        self.db = firestore.Client(project=project_id, credentials=credentials)

    def upload_item(self, collection_name, item: dict):
        """
        Uploads a metrics dictionary to the specified collection/document.
        If document_id exists, it will be overwritten.
        """
        doc_ref = self.db.collection(collection_name).document()
        doc_ref.set(item)
