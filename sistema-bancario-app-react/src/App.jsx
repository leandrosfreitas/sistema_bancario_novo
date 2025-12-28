import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "./features/auth/Login";
import Dashboard from "./features/dashboard/Dashboard";
import Register from "./features/register/Register";


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}
