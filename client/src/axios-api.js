import axios from 'axios'
axios.defaults.withCredentials = true; //This will cause Axios to automatically send tokens/cookies w/ every request
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000'
});

export const createQuestion = (payload) => api.post(`/questions`, payload);
export const deleteQuestion = (id) => api.delete(`/questions/${id}`);
export const updateQuestion = (id, payload) => api.put(`/questions/${id}`, payload);
export const getAllQuestions = () => api.get(`/questions/get_all`);
export const getQuestion = (id) => api.get(`/questions/${id}`);

export const createSet = (payload) => api.post(`/sets/`, payload);
export const deleteSet = (id) => api.delete(`/sets/${id}`);
export const updateSet = (id, payload) => api.put(`/sets/${id}`, payload);
export const getAllSets = () => api.get(`/sets/`);
export const getSet = (id) => api.get(`/sets/${id}`);

export const registerUser = (payload) => api.post(`/register`, payload);
export const loginUser = (username, password) => api.post(`/login`, {username: username, password: password});
export const updateUserSet = (payload) => api.put(`/usersets`, payload);
export const logout = () => api.put(`/logout`);

const backendApi = {
    createQuestion, 
    deleteQuestion,
    updateQuestion, 
    getAllQuestions, 
    getQuestion,

    createSet,
    deleteSet, 
    updateSet,
    getAllSets,
    getSet,

    registerUser,
    loginUser,
    updateUserSet,
    logout
};

export default backendApi;