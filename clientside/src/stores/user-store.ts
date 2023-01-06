import { defineStore } from "pinia";
import backendApi from "src/boot/axios";
import { User } from "src/types";

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
        async loginUser(form: User){
            const formData = new FormData();
            formData.append('grant_type', 'password');
            formData.append('username', form.username);
            formData.append('password', form.password);

            const response = await backendApi.loginUser(formData);
            backendApi.setHeader(response.data.access_token);
            this.user = form.username;
        },
        async registerUser(form: User){
            await backendApi.registerUser(form);
        },
        logout(){
            backendApi.setHeader('');
            this.user = '';
        }
    },
})