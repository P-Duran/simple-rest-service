from decorators.repository_decorators import repository
from model.entities.surf_entity import SurfEntity
from repositories.base_repository import BaseRepository


@repository(SurfEntity)
class SurfClassesRepository(BaseRepository[SurfEntity]):
    pass
