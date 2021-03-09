from graphene_django import DjangoObjectType
import graphene
from apps.users.models import User as UserModel
from apps.decks.models import Deck as DeckModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Deck(DjangoObjectType):
    class Meta:
        model = DeckModel

class Query(graphene.ObjectType):
    users = graphene.List(User)
    decks = graphene.List(Deck)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_decks(self, info):
        return DeckModel.objects.all()

schema = graphene.Schema(query=Query)
