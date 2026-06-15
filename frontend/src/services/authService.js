import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export async function login(email, senha) {
  const formData = new URLSearchParams();

  formData.append("username", email);
  formData.append("password", senha);

  const response = await axios.post(
    `${API_URL}/auth/login`,
    formData,
    {
      headers: {
        "Content-Type":
          "application/x-www-form-urlencoded",
      },
    }
  );

  return response.data;
}