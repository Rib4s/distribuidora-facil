import { useContext } from "react";
import { useNavigate } from "react-router-dom";

import { Button } from "@mui/material";

import { AuthContext } from "../context/AuthContext";

function Dashboard() {
    const { logout } =
        useContext(AuthContext);

    const navigate = useNavigate();

    function handleLogout() {
        logout();

        navigate("/");
    }

    return (
        <div style={{ padding: "20px" }}>
            <h1>Dashboard</h1>

            <p>
                Bem-vindo ao Distribuidora Fácil!
            </p>

            <Button
                variant="contained"
                color="error"
                onClick={handleLogout}
            >
                Sair
            </Button>
        </div>
    );
}

export default Dashboard;