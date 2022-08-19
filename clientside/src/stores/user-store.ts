import { defineStore } from "pinia";
import backendApi from "src/boot/axios";
import { Set } from "src/types";

interface State { 
    user: string,
    userSets: Array<Set>
}

const defaultUser = '';

export const useUserStore = defineStore<string, State>('users', {
    state: () => ({
        user: defaultUser,
        userSets: []
    }),
    getters: {},
    actions: {
        async loginUser(username: string, password: string){
            console.log("reached login user");
            const formData = new FormData();
            formData.append('grant_type', 'password')
            formData.append('username', username)
            formData.append('password', password)
            const response1 = await backendApi.loginUser(formData);
            console.log(response1);
            backendApi.setHeader(response1.data.access_token);
            this.user = username;
            const response2 = await backendApi.getUserSets(this.user);
            this.userSets = response2.data;
        },
        async registerUser(username: string, password: string, password_confirmed: string){
            const response = await backendApi.registerUser({username, password, password_confirmed});
            return response;
        }
    },
})