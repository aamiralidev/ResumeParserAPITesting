from pathlib import Path
from pprint import pprint
import os 

from affinda import AffindaAPI, TokenCredential
from affinda.models import WorkspaceCreate, CollectionCreate


class Affinda:
    def __init__(self) -> None:

        token = os.environ.get('AFFINDA_API_KEY')
        file_pth = Path("PATH_TO_DOCUMENT.pdf")

        credential = TokenCredential(token=token)
        client = AffindaAPI(credential=credential)

        # First get the organisation, by default your first one will have free credits
        my_organisation = client.get_all_organizations()[0]

        # And within that organisation, create a workspace, for example for Recruitment:
        workspace_body = WorkspaceCreate(
            organization=my_organisation.identifier,
            name="My Workspace",
        )
        recruitment_workspace = client.create_workspace(body=workspace_body)

        # Finally, create a collection that will contain our uploaded documents, for example resumes, by selecting the
        # appropriate extractor
        collection_body = CollectionCreate(
            name="Resumes", workspace=recruitment_workspace.identifier, extractor="resume"
        )
        resume_collection = client.create_collection(collection_body)
        self.client = client
        self.resume_collection = resume_collection

    def parse(self, filepath):
        # Now we can upload a resume for parsing
        with open(filepath, "rb") as f:
            resume = self.client.create_document(file=f, file_name=filepath.split('/')[-1], collection=self.resume_collection.identifier)
        return resume.as_dict()