from rest_framework.routers import DefaultRouter
from .views import GenreSet, ActorSet, DirectorySet, MovieSet, CommentSet

router = DefaultRouter()

router.register('genres', GenreSet)
router.register('actors', ActorSet)
router.register('directory', DirectorySet)
router.register('movies', MovieSet)
router.register('comments', CommentSet)

urlpatterns = router.urls

