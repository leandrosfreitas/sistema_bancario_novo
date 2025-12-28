// Importa o arquivo de estilos CSS específico da tela de login
import "./Login.css";

// Importa o hook useState do React para controlar estados (valores dinâmicos)
import { useState } from "react";

// Importa o hook useNavigate para fazer navegação entre rotas
import { Navigate, useNavigate } from "react-router-dom";

// Define e exporta o componente Login
export default function Login() {
  // Cria um estado para armazenar o valor do campo de e-mail
  // email = valor atual
  // setEmail = função para atualizar o valor
  const [email, setEmail] = useState("");

  // Cria um estado para armazenar o valor do campo de senha
  const [senha, setSenha] = useState("");

  // Inicializa a função de navegação entre páginas
  const navigate = useNavigate();

  // Função executada quando o formulário é enviado
  const handleSubmit = (e) => {

    // Evita o comportamento padrão do formulário (recarregar a página)
    e.preventDefault();

    // Exibe no console os dados digitados (apenas para teste)
    console.log("Login enviado", { email, senha });

    // ✅ Salva o e-mail do usuário no localStorage
    localStorage.setItem("user", email);

    // Redireciona o usuário para a rota "/dashboard"
    navigate("/dashboard");
  };

  // JSX retornado pelo componente (interface visual)
  return (
    <div className="login-container">
      <div className="login-card">

        {/* Exibe o logo da aplicação */}
        <img
          src="/baking-logo.png"
          alt="Logo"
          className="login-logo"
        />

        {/* Título da página de login */}
        <h2 className="login-title">Acessar Conta</h2>

        {/* Formulário de login */}
        <form onSubmit={handleSubmit} className="login-form">

          {/* Campo de entrada para o e-mail */}
          <input
            type="email"
            placeholder="E-mail"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          {/* Campo de entrada para a senha */}
          <input
            type="password"
            placeholder="Senha"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            required
          />

          {/* Botão que envia o formulário */}
          <button type="submit">
            Entrar
          </button>

          {/* Botão para redirecionar ao cadastro */}
          <button
            type="button"
            className="register-button"
            onClick={() => navigate("/register")}
          >
            Cadastrar
          </button>

        </form>
      </div>
    </div>
  );
}
