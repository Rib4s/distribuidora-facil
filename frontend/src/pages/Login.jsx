import { useState } from "react";
import { useContext } from "react";
import { useNavigate } from "react-router-dom";

import { AuthContext } from "../context/AuthContext";
import {
  Box,
  Button,
  Container,
  Paper,
  TextField,
  Typography,
} from "@mui/material";

import { login } from "../services/authService";

function Login() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const { login: authLogin } =
    useContext(AuthContext);

  const navigate = useNavigate();

  async function handleLogin(e) {
    e.preventDefault();

    try {
      const data = await login(email, senha);

      console.log("TOKEN:", data.access_token);

      authLogin(
        data.access_token
      );

      navigate("/dashboard");
    } catch (error) {
      console.error(error);

      alert("Email ou senha inválidos");
    }
  }

  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          minHeight: "100vh",
          display: "flex",
          alignItems: "center",
        }}
      >
        <Paper
          elevation={3}
          sx={{
            p: 4,
            width: "100%",
          }}
        >
          <Typography
            variant="h4"
            gutterBottom
          >
            Distribuidora Fácil
          </Typography>

          <form onSubmit={handleLogin}>
            <TextField
              fullWidth
              label="Email"
              margin="normal"
              value={email}
              onChange={(e) =>
                setEmail(e.target.value)
              }
            />

            <TextField
              fullWidth
              label="Senha"
              type="password"
              margin="normal"
              value={senha}
              onChange={(e) =>
                setSenha(e.target.value)
              }
            />

            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 2 }}
            >
              Entrar
            </Button>
          </form>
        </Paper>
      </Box>
    </Container>
  );
}

export default Login;