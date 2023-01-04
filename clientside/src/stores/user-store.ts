import { defineStore } from "pinia";
import backendApi from "src/boot/axios";

interface State { 
    user: string
}

const defaultUser = '';

export const useUserStore = defineStore<string, State>('users', {
    state: () => ({
        user: defaultUser,
    }),
    getters: {},
    actions: {
        async loginUser(username: string, password: string){
            const formData = new FormData();
            formData.append('grant_type', 'password')
            formData.append('username', username)
            formData.append('password', password)
            const response1 = await backendApi.loginUser(formData);
            backendApi.setHeader(response1.data.access_token);
            this.user = username;
        },
        async registerUser(username: string, password: string, password_confirmed: string){
            const response = await backendApi.registerUser({username, password, password_confirmed});
            return response;
        },
        logout(){
            backendApi.setHeader('');
            this.user = '';
        }
    },
})