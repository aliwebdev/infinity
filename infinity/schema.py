import graphene

from hours.query import Query as HoursQuery
from hours.mutations import Mutation as HoursMutation


class Mutation(
    HoursMutation,
    graphene.ObjectType,
):
    pass


class Query(
    HoursQuery,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
