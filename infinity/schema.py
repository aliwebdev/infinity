import graphene

from hours.schema import HoursQuery
from hours.mutations import HoursMutation


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
