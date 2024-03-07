from pydantic import BaseModel


class CatDocsComponent(BaseModel):
    url: str
    repo_path: str
    docs_path: str
    deployable_unit: str
    application: str
    system: str

    @property
    def name(self):
        return f'{self.system}.{self.application}.{self.deployable_unit}'