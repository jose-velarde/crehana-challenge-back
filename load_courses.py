# import sqlite3
import os

# import environ
import pandas as pd
from sqlalchemy import create_engine

# environ.Env.read_env()

#! DB connection
# SQLite local
# con = sqlite3.connect("db.sqlite3")

#! Postgres local
# login = pd.read_csv("password.txt")
# pw = login.iloc[0]["PW"]

# pw = os.environ['SECRET_KEY']
# engine = create_engine('postgresql://{}:{}@localhost:5432/{}'.format('Jose', pw, 'jose-velarde-drf'))

#! Postgres heroku

import dj_database_url

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(db_from_env)


engine = create_engine(
    "postgresql://{}:{}@{}:{}/{}".format(
        DATABASES["default"].USER,
        DATABASES["default"].PASSWORD,
        DATABASES["default"].HOST,
        DATABASES["default"].PORT,
        DATABASES["default"].NAME,
    )
)

#! Data process
courses = pd.read_excel("_documentation\courses_list.xlsx", sheet_name="Query result")
courses_course = (
    courses[
        [
            # "id",
            "course_name",
            "category_name",
            "subcategory_name",
            "level",
            "username",
            "real_price",
            "discount",
            "course_score",
            "users",
        ]
    ]
    .rename(columns={"category_name": "category", "subcategory_name": "subcategory"})
    .replace(to_replace="&", value="y", regex=True)
)

courses_subcategory = (
    courses[["subcategory_name", "category_name"]]
    .drop_duplicates(subset="subcategory_name")
    .rename(columns={"category_name": "category"})
    .sort_values(["category"])
    .reset_index(drop=True)
).replace(to_replace="&", value="y", regex=True)

courses_category = pd.DataFrame(courses["category_name"].sort_values().unique(), columns=["category_name"]).replace(
    to_replace="&", value="y", regex=True
)

print(courses_course)
print(courses_subcategory)
print(courses_category)

#! sql lite load
# courses_category.to_sql(name="crehana_store_category", con=con, if_exists="replace", index_label="id")
# courses_subcategory.to_sql(name="crehana_store_subcategory", con=con, if_exists="replace", index_label="id")
# courses_course.to_sql(name="crehana_store_course", con=con, if_exists="replace", index_label="id")

#!  postgres load
courses_course.to_sql(name="crehana_store_course", con=engine, if_exists="replace", index_label="id")
courses_subcategory.to_sql(name="crehana_store_subcategory", con=engine, if_exists="replace", index_label="id")
courses_category.to_sql(name="crehana_store_category", con=engine, if_exists="replace", index_label="id")


# con.commit()
# con.close()
