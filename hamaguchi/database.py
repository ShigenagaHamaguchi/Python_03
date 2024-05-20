from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(
    **{
        "user":"root",
        "password":"mysql",
        "host":"localhost",
        "database":"ENSHU"
    }
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo= True
)

session = scoped_session(
    session_factory=sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base  = declarative_base()
Base.query = session.query_property()