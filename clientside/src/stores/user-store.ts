import { defineStore } from "pinia";
import backendApi from "src/boot/axios";
import { User } from "src/types";
import { errorStore } from "./error-store";

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

            try {
                await backendApi.loginUser(formData);
                this.user = form.username;
            }
            catch {
                errorStore.setMessage("There was a problem trying to log you in. Please check your username/password and try again.");
            }
        },
        async registerUser(form: User){
            try {
                await backendApi.registerUser(form);
            }
            catch {
                errorStore.setMessage("Your account could not be registered. Try changing your username/checking password and try again.")
            }
        },
        async logout(){
            // backendApi.setHeader('');
            await backendApi.logout();
            this.user = '';
        }
    },
})