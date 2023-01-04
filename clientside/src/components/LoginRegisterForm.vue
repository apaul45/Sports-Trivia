<script setup lang="ts">
import { ref } from 'vue';
import { useUserStore } from 'src/stores/user-store';

const props = defineProps({registerUser: Boolean})

const username = ref<string>('');
const password = ref<string>('');
const passwordConfirmed = ref<string>('');

const inputCondition = (val: string) => val && val.length > 0 || 'Please provide a value';

const registerLogin = async() => {
    if (props.registerUser){
        const response = await useUserStore().registerUser(username.value, password.value, passwordConfirmed.value);
        if (response.status !== 200) return; //TODO: Need error handling here 
    }
    await useUserStore().loginUser(username.value, password.value);

    username.value = ' ';
    password.value = ' ';
    passwordConfirmed.value = ' ';
}
</script>

<template>
    <q-expansion-item
    expand-separator
    :label="registerUser ? 'Register' : 'Login'"
    >
        <q-form style="padding-left:3%">

            Username:
            <q-input
            filled
            style="width: 97%;"
            v-model="username"
            lazy-rules
            :rules="[inputCondition]"
            label-slot clearable
            />

            Password:
            <q-input
            filled
            style="width: 97%;"
            v-model="password"
            lazy-rules
            :rules="[inputCondition]"
            label-slot clearable
            />

            <div v-if="props.registerUser">
                Password Confirmed:
                <q-input
                filled
                style="width: 97%;"
                v-model="passwordConfirmed"
                lazy-rules
                :rules="[inputCondition]"
                label-slot clearable
                />
            </div>

            <q-btn 
            @click="registerLogin" 
            type="submit" 
            label="Submit" 
            color="primary"
            />
       </q-form>
    </q-expansion-item>
</template>