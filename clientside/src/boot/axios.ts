import axios, { AxiosInstance } from 'axios'
import { Question, Set, User } from '../types'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
  }
}

const api = axios.create({
  baseURL: 'https://sports-trivia-bn57cau7zq-uc.a.run.app/',
  headers: {
    Accept: 'application/json'
  },
})

export function setHeader(token: string){
  api.defaults.headers.common.Authorization = `Bearer ${token}`
}

export const createQuestion = (payload: Question) => api.post('/question', payload)
export const deleteQuestion = (question: string) => api.delete(`/question/${question}`)
export const updateQuestion = (question: string, payload: unknown) => api.put(`/question/${question}`, payload)

export const createSet = (payload: Set) => api.post('/set', payload)
export const deleteSet = (id: any) => api.delete(`/set/${id}`)
export const updateSet = (id: any, payload: Set) => api.put(`/set/${id}`, payload)

export const registerUser = (payload: User) => api.post('/register', payload)
export const loginUser = (form: FormData) => { return api.post('/login', form) }

// Query Routes
export const getAllQuestions = () => api.get<Question[]>('/questions')
export const getAllUsers = () => api.get<User[]>('/users')
export const getAllTags = () => api.get<String[]>('/tags')
export const getAllSets = () => api.get<Set[]>('/sets')
export const getNumberOfSets = () => api.get<number>(`/sets?is_count=${true}`)

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
