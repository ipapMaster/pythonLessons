# db_session.py - создание БД и сессии по работе с ней
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

SqlAlchemyBase = orm.declarative_base()

created = None  # создана ли сессия


def global_init(db_file):
    global created

    if created:
        return

    if not db_file or not db_file.strip():
        raise Exception('Забыли подключить файл базы данных')

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    # Для нужд отладки (потом можно и отключить)
    print(f'Мы подключились к {conn_str} успешно')

    # создание движка для работы с БД
    engine = sa.create_engine(conn_str, echo=False)
    created = orm.sessionmaker(bind=engine)

    from . import all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global created
    return created()
