from app.db.base_class import Base

# IMPORTAÇÃO EXPLÍCITA DE TODOS OS MODELS
# Isso é necessário para:
# - Alembic detectar as tabelas
# - Base.metadata conter todos os schemas

from app.models.usuario import Usuario
from app.models.conta import Conta
from app.models.cartao import Cartao
from app.models.transacao import Transacao
from app.models.pagamento import Pagamento
from app.models.emprestimo import Emprestimo
from app.models.investimento import Investimento
from app.models.notificacao import Notificacao
