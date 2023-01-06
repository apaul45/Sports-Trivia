<script setup lang="ts">
import { reactive } from 'vue';
import { useUserStore } from 'src/stores/user-store';
import { QExpansionItem, QForm, QInput, QBtn } from 'quasar';
import { registerUser } from 'src/boot/axios';
import { User } from 'src/types';

const props = defineProps({registerUser: Boolean});

const refs = reactive<User>({
    username: '',
    password: '',
    password_confirmed: ''
});

const inputCondition = (val: string) => val && val.length > 0 || 'Please provide a value';

const registerLogin = async() => {
    if (props.registerUser){
        await useUserStore().registerUser(refs);
    }
    
    await useUserStore().loginUser(refs);

    Object.keys(refs).forEach(
        (key) => refs[key] = ''
    );
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
            v-model="refs.username"
            lazy-rules
            :rules="[inputCondition]"
            label-slot clearable
            />

            Password:
            <q-input
            filled
            style="width: 97%;"
            v-model="refs.password"
            lazy-rules
            :rules="[inputCondition]"
            label-slot clearable
            />

            <div v-if="props.registerUser">
                Password Confirmed:
                <q-input
                filled
                style="width: 97%;"
                v-model="refs.password_confirmed"
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
       <br/>
    </q-expansion-item>
</template>