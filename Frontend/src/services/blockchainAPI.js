import axios from "axios";

const API_BASE_URL = "http://127.0.0.1:5000";

export const fetchBlockchain = async () => {
    return await axios.get(`${API_BASE_URL}/get_chain`);
};

export const addBlock = async (data) => {
    return await axios.post(`${API_BASE_URL}/add_block`, { data });
};
