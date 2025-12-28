// Importa o arquivo de estilos CSS específico da tela de registro
import "./Register.css";

// Importa hooks do React
import { useState } from "react";
import { useNavigate } from "react-router-dom";

// Define e exporta o componente Register
export default function Register() {
  // Estados para armazenar os valores dos campos
  const [nome, setNome] = useState("");
  const [cpf, setCpf] = useState("");
  const [data_nascimento, setDataNascimento] = useState("");
  const [telefone, setTelefone] = useState("");
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [confirmarSenha, setConfirmarSenha] = useState("");

  // Inicializa a função de navegação
  const navigate = useNavigate();

  // Função executada quando o formulário é enviado
  const handleSubmit = (e) => {
    e.preventDefault();

    // Validação simples de senha
    if (senha !== confirmarSenha) {
      alert("As senhas não coincidem!");
      return;
    }

    // Exibe no console os dados cadastrados (apenas para teste)
    console.log("Cadastro enviado", { nome, email, senha });

    // ✅ Salva o e-mail do usuário no localStorage (simulação)
    localStorage.setItem("user", email);

    // Redireciona para o dashboard
    navigate("/dashboard");
  };

  // JSX retornado pelo componente
  return (
    <div className="register-container">
      <div className="register-card">

        {/* Logo */}
        <img
          src="/baking-logo.png"
          alt="Logo"
          className="register-logo"
        />

        {/* Título */}
        <h2 className="register-title">Criar Conta</h2>

        {/* Formulário de cadastro */}
        <form onSubmit={handleSubmit} className="register-form">

          <input
            type="text"
            placeholder="Nome completo"
            value={nome}
            onChange={(e) => setNome(e.target.value)}
            required
          />

          <input
            type="text"
            placeholder="CPF"
            value={cpf}
            onChange={(e) => setCpf(e.target.value)}
            pattern="\d{11}"
            required
          />

          <input
            type="text"
            placeholder="Data nascimento"
            value={data_nascimento}
            onChange={(e) => setDataNascimento(e.target.value)}
            required
          />

          <input
            type="text"
            placeholder="Contato"
            value={telefone}
            onChange={(e) => setTelefone(e.target.value)}
            required
          />

          <input
            type="email"
            placeholder="E-mail"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <input
            type="password"
            placeholder="Senha"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            required
          />

          <input
            type="password"
            placeholder="Confirmar senha"
            value={confirmarSenha}
            onChange={(e) => setConfirmarSenha(e.target.value)}
            required
          />

          <button type="submit">
            Registrar
          </button>

          {/* Botão para voltar ao login */}
          <button
            type="button"
            className="login-button"
            onClick={() => navigate("/")}
          >
            Já tenho conta
          </button>
        </form>
      </div>
    </div>
  );
}
