import React from "react";
import "./Dashboard.css";

export default function Dashboard({ onLogout }) {
  const user = localStorage.getItem("user");

  // Dados bancários de exemplo
  const dadosBancarios = {
    saldo: "R$ 5.480,00",
    conta: "12345-6",
    agencia: "0001"
  };

  const icons = [
    { emoji: "💳", label: "Cartões" },
    { emoji: "💰", label: "Transações" },
    { emoji: "📊", label: "Relatórios" },
    { emoji: "⚙️", label: "Configurações" },
    { emoji: "📩", label: "Mensagens" },
    { emoji: "🏦", label: "Contas" },
  ];

  const handleLogout = () => {
    localStorage.removeItem("user");
    if (onLogout) onLogout();
    window.location.href = "/";
  };

  return (
    <div className="dashboard-container">

      {/* SIDEBAR */}
      <div className="dashboard-sidebar">

        {/* Usuário */}
        <div className="dashboard-user">
          <h3>{user}</h3>
          <span>Usuário logado</span>
        </div>

        {/* Dados bancários */}
        <div className="dashboard-info">
          <p><strong>Saldo:</strong> {dadosBancarios.saldo}</p>
          <p><strong>Conta:</strong> {dadosBancarios.conta}</p>
          <p><strong>Agência:</strong> {dadosBancarios.agencia}</p>
        </div>

        {/* Campo de pesquisa */}
        <input 
          type="text"
          placeholder="Pesquisar..."
          className="dashboard-search"
        />

        {/* Botões */}
        <div className="dashboard-actions">
          <button className="dashboard-btn-blue">🔔 Notificações</button>
          <button className="dashboard-btn-red" onClick={handleLogout}>🚪 Sair</button>
        </div>
      </div>

      {/* MAIN */}
      <div className="dashboard-main">
        {icons.map((icon, index) => (
          <button key={index} className="dashboard-btn-main">
            <span className="dashboard-btn-emoji">{icon.emoji}</span>
            <span className="dashboard-btn-label">{icon.label}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
