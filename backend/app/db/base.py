from app.db.base_class import Base

# Importa todos os modelos para registrar no metadata
from app.models.cartao import Cartao
from app.models.conta import Conta
from app.models.emprestimo import Emprestimo
from app.models.investimento import Investimento
from app.models.notificacao import Notificacao
from app.models.pagamento import Pagamento
from app.models.transacao import Transacao
from app.models.usuario import Usuario
