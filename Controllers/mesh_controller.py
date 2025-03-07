from Models.mesh_model import MeshModel


class MeshController:
    def __init__(self, model: MeshModel):
        self._model = model

    def compute(self):
        print("compute")