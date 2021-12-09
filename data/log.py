import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

#Conecta no banco
engine = sqlalchemy.create_engine(
    "mariadb+mariadbconnector://root:abc123@127.0.0.1:3308/calc")

Base = declarative_base()

#Cria tabela no banco MariaDB
class Log(Base):
    __tablename__ = 'tb_log'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    data_operacao = sqlalchemy.Column(sqlalchemy.DateTime)
    tipo_operacao = sqlalchemy.Column(sqlalchemy.String(length=30))
    operacao = sqlalchemy.Column(sqlalchemy.String(length=30))
    argumentos = sqlalchemy.Column(sqlalchemy.String(length=30))
    resultado = sqlalchemy.Column(sqlalchemy.Float)


Base.metadata.create_all(engine)

#Cria sessão na db
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
sessao = Session()


def addOperacao(operacao, tipo_operacao, data_operacao, argumentos, resultado):
    operacaoRealizada = Log(operacao=operacao, tipo_operacao=tipo_operacao,
                            data_operacao=data_operacao, argumentos=argumentos, resultado=resultado)
    sessao.add(operacaoRealizada)
    sessao.commit()


def operacoesRealizadas():
    operacoes = sessao.query(Log).all()
