import axios from 'axios'
axios.defaults.withCredentials = true; //This will cause Axios to automatically send tokens/cookies w/ every request
const api = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    headers:{
        "Accept": "application/json"
    }
});

export const setHeader = (token) => api.defaults.headers.common['Authorization'] = `Bearer ${token}`;

export const createQuestion = (payload) => api.post(`/question`, payload);
export const deleteQuestion = (question) => api.delete(`/question/${question}`);
export const updateQuestion = (question, payload) => api.put(`/question/${question}`, payload);
export const getAllQuestions = () => api.get(`/questions`);

export const createSet = (payload) => api.post(`/set`, payload);
export const deleteSet = (id) => api.delete(`/set/${id}`);
export const updateSet = (id, payload) => api.put(`/set/${id}`, payload);
export const getAllSets = () => api.get(`/sets`);

export const registerUser = (payload) => api.post(`/register`, payload);
export const loginUser = (username, password) => {
    //For logging in, have to send info as form data
    const formData = new FormData();
    formData.append('grant_type', 'password')
    formData.append('username', username);
    formData.append('password', password);
    return api.post(`/login`, formData);
}
//export const logout = () => api.put(`/logout`);


//Query Routes
export const getPlayerQuestions = (player) => {return api.get(`/player-questions/${player}`);};
export const getUserQuestions = (user) => {return api.get(`/user-questions/{user}?username=${user}`);};
export const getTagQuestions = (tags) => api.post(`/tag-questions`, tags);
export const getUserSets = (user) => {return api.get(`/sets/${user}`);};
export const getUsersRatings = () => {return api.get(`/users-ratings`);};

const backendApi = {
    setHeader,

    createQuestion, 
    deleteQuestion,
    updateQuestion, 
    getAllQuestions, 

    createSet,
    deleteSet, 
    updateSet,
    getAllSets,

    registerUser,
    loginUser,

    getPlayerQuestions,
    getUserQuestions,
    getTagQuestions,
    getUserSets,
    getUsersRatings
};

export default backendApi;