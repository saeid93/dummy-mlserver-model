# from pydantic import BaseModel, validator

# class MyModel(BaseModel):
#     value: int

#     @validator("value")
#     def validate_value(cls, value):
#         if value < 0:
#             raise ValueError("Value must be greater than or equal to 0")
#         return value

# my_instance = MyModel(value=10.1)

# print(my_instance.value)

# from pydantic import BaseModel, Field, ValidationError


# class User(BaseModel):
#     age: int = Field(default='twelve', validate_default=True)


# try:
#     user = User(age="1")
# except ValidationError as e:
#     print(e)
#     """
    # 1 validation error for User
#     age
#       Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='twelve', input_type=str]
#     """


# from mlserver.types import RequestInput

# a = RequestInput(
#     name = "dummy-input",
#     shape=[3,3],
#     datatype="INT32",
#     data=[1,2,3,4,5]
# )

# a.validate_type()
# def check(a: RequestInput):
#     a = 1

# check(a)

# from typing import Any, Callable, Set

# from pydantic import (
#     AliasChoices,
#     AmqpDsn,
#     BaseModel,
#     Field,
#     ImportString,
#     PostgresDsn,
#     RedisDsn,
# )

# from pydantic_settings import BaseSettings, SettingsConfigDict


# class SubModel(BaseModel):
#     foo: str = 'bar'
#     apple: int = 1


# class Settings(BaseSettings):
#     auth_key: str = Field(validation_alias='my_auth_key')

#     api_key: str = Field(alias='my_api_key')

#     redis_dsn: RedisDsn = Field(
#         'redis://user:pass@localhost:6379/1',
#         validation_alias=AliasChoices('service_redis_dsn', 'redis_url'),
#     )
#     pg_dsn: PostgresDsn = 'postgres://user:pass@localhost:5432/foobar'
#     amqp_dsn: AmqpDsn = 'amqp://user:pass@localhost:5672/'

#     special_function: ImportString[Callable[[Any], Any]] = 'math.cos'

#     # to override domains:
#     # export my_prefix_domains='["foo.com", "bar.com"]'
#     domains: Set[str] = set()

#     # to override more_settings:
#     # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
#     more_settings: SubModel = SubModel()

#     model_config = SettingsConfigDict(env_prefix='my_prefix_')


# print(Settings().model_dump())
# """
# {
#     'auth_key': 'xxx',
#     'api_key': 'xxx',
#     'redis_dsn': Url('redis://user:pass@localhost:6379/1'),
#     'pg_dsn': MultiHostUrl('postgres://user:pass@localhost:5432/foobar'),
#     'amqp_dsn': Url('amqp://user:pass@localhost:5672/'),
#     'special_function': math.cos,
#     'domains': set(),
#     'more_settings': {'foo': 'bar', 'apple': 1},
# }
# """

from mlserver.types import Datatype

a = Datatype("INT32")
print(a)
