import axios, { AxiosInstance } from 'axios'
import { Question, Set, User } from '../types'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
  }
}
// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    Accept: 'application/json'
  }
})

export function setHeader (token: string) {
  api.defaults.headers.common.Authorization = `Bearer ${token}`
}

export const createQuestion = (payload: Question) => api.post('/question', payload)
export const deleteQuestion = (question: string) => api.delete(`/question/${question}`)
export const updateQuestion = (question: string, payload: unknown) => api.put(`/question/${question}`, payload)
export const getAllQuestions = () => api.get('/questions')

export const createSet = (payload: Set) => api.post('/set', payload)
export const deleteSet = (id: number) => api.delete(`/set/${id}`)
export const updateSet = (id: number, payload: unknown) => api.put(`/set/${id}`, payload)
export const getAllSets = () => api.get('/sets')

export const registerUser = (payload: User) => api.post('/register', payload)
export const loginUser = (form: FormData) => { return api.post('/login', form) }
// export const logout = () => api.put(`/logout`);

// Query Routes
export const getPlayerQuestions = (player: string) => { return api.get(`/player-questions/${player}`) }
export const getUserQuestions = (user: string) => { return api.get(`/user-questions/{user}?username=${user}`) }
export const getTagQuestions = (tags: Array<string>) => api.post('/tag-questions', tags)
export const getUserSets = (user: string) => { return api.get(`/sets/${user}`) }
export const getUsersRatings = () => { return api.get('/users-ratings') }

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
}

export default backendApi
