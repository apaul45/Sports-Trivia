<script setup lang="ts">
import { reactive } from 'vue';
import { useUserStore } from 'src/stores/user-store';
import { QExpansionItem, QForm, QInput, QBtn } from 'quasar';
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
    :label="props.registerUser ? 'Register' : 'Login'"
    >
        <q-form 
        @submit="registerLogin"  
        class="form">

            Username:
            <q-input
            filled
            class="input"
            v-model="refs.username"
            lazy-rules
            :rules="[inputCondition]"
            label-slot clearable
            />

            Password:
            <q-input
            filled
            class="input"
            v-model="refs.password"
            lazy-rules
            :rules="[inputCondition]"
            label-slot clearable
            />

            <div v-if="props.registerUser">
                Password Confirmed:
                <q-input
                filled
                class="input"
                v-model="refs.password_confirmed"
                lazy-rules
                :rules="[inputCondition]"
                label-slot clearable
                />
            </div>

            <q-btn 
            type="Submit" 
            label="Submit" 
            color="primary"
            />
       </q-form>
       <br/>
    </q-expansion-item>
</template>

<style scoped lang="scss">
.form {
    padding-left:3%;
}
.input {
    width: 97%;
}
</style>