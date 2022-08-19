import axios, { AxiosInstance, AxiosResponse } from 'axios'
import { Question, Set, User } from '../types'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
  }
}

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    Accept: 'application/json'
  }
})

export function setHeader(token: string){
  api.defaults.headers.common.Authorization = `Bearer ${token}`
}

export const createQuestion = (payload: Question) => api.post('/question', payload)
export const deleteQuestion = (question: string) => api.delete(`/question/${question}`)
export const updateQuestion = (question: string, payload: unknown) => api.put(`/question/${question}`, payload)

export const createSet = (payload: Set) => api.post('/set', payload)
export const deleteSet = (id: number) => api.delete(`/set/${id}`)
export const updateSet = (id: number, payload: unknown) => api.put(`/set/${id}`, payload)

export const registerUser = (payload: User) => api.post('/register', payload)
export const loginUser = (form: FormData) => { return api.post('/login', form) }
// export const logout = () => api.put(`/logout`);

// Query Routes
export const getAllQuestions = () => api.get('/questions')
export const getAllUsers = () => api.get('/users')
export const getAllTags = () => api.get('/tags')
export const getAllSets = () => api.get<Set[]>('/sets')
export const getNumberOfSets = () => api.get<number>('/set-count')

export const getFilteredQuestions = (filters: Array<object>) => api.post('/filter-questions', filters);

export const getPlayerQuestions = (player: string) => { return api.get(`/player-questions/${player}`) }
export const getUserQuestions = (user: string) => { return api.get(`/user-questions/{user}?username=${user}`) }
export const getTagQuestions = (tags: Array<string>) => api.post('/tag-questions', tags)
export const getUserSets = (user: string) => { return api.get<Set[]>(`/sets/${user}`) }
export const getUsersRatings = () => { return api.get('/users-ratings') }

const backendApi = {
  setHeader,

  createQuestion,
  deleteQuestion,
  updateQuestion,

  createSet,
  deleteSet,
  updateSet,

  registerUser,
  loginUser,

  getFilteredQuestions,

  getAllQuestions,
  getAllUsers,
  getAllTags,
  getAllSets,
  getNumberOfSets,
  getPlayerQuestions,
  getUserQuestions,
  getTagQuestions,
  getUsersRatings
}

export default backendApi
