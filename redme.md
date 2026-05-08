#Iniciando o alenbic

no terminal:
``` bash
python -m alembic init migrations 
```

#Apagar o valor da linha 89 - no arqivo alembic.ini
dixe assim:

sqlalchemy.url = 

#Edite o arquivo migrations/env.py:

from dotenv import load_dotenv
import os
import database
from database import Base

load_dotenv()

config.set_main_option("sqlachemy.url", os.getenv("DATABASE_URL"))

target_metadata = Base.metadata

#Gere a migration com autogenerate
``` bash
python -m alembic revision --autogenerate -m "Criar tabela usuarios"
```

#Aplicar a migrations
``` bash
python -m alembic upgrade head
```