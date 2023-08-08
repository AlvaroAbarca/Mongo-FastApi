from tortoise import Tortoise

import os

async def init_db():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    user=os.getenv("MYSQL_USER", "mysql_zoco")
    password=os.getenv("MYSQL_PASSWORD", "zoco2019")
    host=os.getenv("MYSQL_HOST", "mysqldb")
    port=int(os.getenv("MYSQL_PORT", 3306))
    db=os.getenv("MYSQL_DB", "zocodb")

    await Tortoise.init(
        db_url='mysql://{user}:{password}@{host}:{port}/{db}'.format(
            user=user, password=password, host=host, port=port, db=db
        ),
        modules={'models': ['db.models', 'meli.models']}
    )
    # Generate the schema
    await Tortoise.generate_schemas()