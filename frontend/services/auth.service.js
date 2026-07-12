import api from "./api";

export const login = async (credentials) => {
    const response = await api.post("/auth/login/", credentials);

    return {
        user: response.data.data.user,
        tokens: response.data.data.tokens,
    };
};

export const register = async (userData) => {
    const response = await api.post("/auth/register/", userData);
    return response.data;
};

export const getProfile = async (accessToken) => {
    const response = await api.get("/auth/profile/", {
        headers: {
            Authorization: `Bearer ${accessToken}`,
        },
    });

    return response.data;
};

export const refreshToken = async (refresh) => {
    const response = await api.post("/auth/refresh/", {
        refresh,
    });

    return response.data;
};