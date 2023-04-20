#ceate relationship one to many and one to one in sqlalchemy with graphql in flask
# create table
# create table users (id serial primary key, name varchar(50), email varchar(50));
# create table posts (id serial primary key, title varchar(50), body varchar(50), user_id integer);
# create user
# create user postgres with password 'postgres';
# install graphql flask postgresql
# pip install flask-graphql
# pip install graphene
# pip install graphene-sqlalchemy
# pip install flask-sqlalchemy
# pip install psycopg2
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
# create flask app
app = Flask(__name__)
# create database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/testpost'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# create table
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    def __repr__(self):
        return '<User %r>' % self.name
# create object of sql alchemy class
class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (relay.Node, )
# create query class
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserObject)
# create mutation class
class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()
    user = graphene.Field(lambda: UserObject)
    def mutate(self, info, name, email):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
# create schema
schema = graphene.Schema(query=Query, mutation=Mutation)
# create view
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
# run app
if __name__ == '__main__':
    app.run(debug=True)
# create table
