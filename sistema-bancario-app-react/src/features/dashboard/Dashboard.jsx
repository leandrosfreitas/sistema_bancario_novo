// Importa o React (necessário para criar componentes)
import React from "react";

// Importa o arquivo de estilos CSS do Dashboard
import "./Dashboard.css";

// Componente Dashboard
// Recebe a função onLogout como propriedade (props)
export default function Dashboard({ onLogout }) {

  // Recupera o e-mail do usuário salvo no localStorage
  const userEmail = localStorage.getItem("user") || "";

  // Extrai apenas o nome do usuário (parte antes do "@")
  // Exemplo: leandro@mail.com → leandro
  const userName = userEmail.includes("@")
    ? userEmail.split("@")[0]
    : userEmail || "Usuário";

  // Objeto com dados bancários de exemplo (dados mockados)
  const dadosBancarios = {
    saldo: "R$ 5.480,00",
    conta: "12345-6",
    agencia: "0001"
  };

  // Lista de ícones que serão exibidos no painel principal
  // Cada item tem um emoji e um rótulo (label)
  const icons = [
    { emoji: "💳", label: "Cartões" },
    { emoji: "💰", label: "Transações" },
    { emoji: "📊", label: "Relatórios" },
    { emoji: "⚙️", label: "Configurações" },
    { emoji: "📩", label: "Mensagens" },
    { emoji: "🏦", label: "Contas" },
  ];

  // Função responsável por realizar o logout do usuário
  const handleLogout = () => {

    // Remove o usuário do localStorage
    localStorage.removeItem("user");

    // Se a função onLogout foi passada como prop, ela é executada
    if (onLogout) onLogout();

    // Redireciona o usuário para a página inicial
    window.location.href = "/";
  };

  // Retorno do JSX (estrutura visual do componente)
  return (
    <div className="dashboard-container">

      {/* ===== SIDEBAR ===== */}
      <div className="dashboard-sidebar">

        {/* Informações do usuário */}
        <div className="dashboard-user">
          <h3>{userName}</h3>
          <span>Usuário logado</span>
        </div>

        {/* Dados bancários exibidos na sidebar */}
        <div className="dashboard-info">
          <p><strong>Saldo:</strong> {dadosBancarios.saldo}</p>
          <p><strong>Conta:</strong> {dadosBancarios.conta}</p>
          <p><strong>Agência:</strong> {dadosBancarios.agencia}</p>
        </div>

        {/* Campo de pesquisa (ainda sem funcionalidade) */}
        <input 
          type="text"
          placeholder="Pesquisar..."
          className="dashboard-search"
        />

        {/* Área de botões da sidebar */}
        <div className="dashboard-actions">

          {/* Botão de notificações */}
          <button className="dashboard-btn-blue">
            🔔 Notificações
          </button>

          {/* Botão de logout */}
          <button 
            className="dashboard-btn-red" 
            onClick={handleLogout}
          >
            🚪 Sair
          </button>
        </div>
      </div>

      {/* ===== ÁREA PRINCIPAL ===== */}
      <div className="dashboard-main">

        {/* Percorre a lista de ícones e cria um botão para cada item */}
        {icons.map((icon, index) => (
          <button 
            key={index} 
            className="dashboard-btn-main"
          >
            <span className="dashboard-btn-emoji">
              {icon.emoji}
            </span>
            <span className="dashboard-btn-label">
              {icon.label}
            </span>
          </button>
        ))}
      </div>
    </div>
  );
}
