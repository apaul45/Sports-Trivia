<script setup>
import { storeToRefs } from 'pinia';
import { useUserStore } from 'src/stores/user-store';
import LoginRegisterForm from './LoginRegisterForm.vue';

const { user } = storeToRefs(useUserStore());

</script>

<template>
    <div class="q-pa-md q-gutter-sm">
        <q-bar class="bg-white">
            <q-btn 
            @click="$router.push('/')"
            flat 
            no-caps 
            padding="none"
            size="40px"
            class="home"
            v-close-popup
            > 
                Sports Trivia
            </q-btn>

            <q-space />

            <q-btn 
            @click="$router.push('/')"
            flat 
            no-caps 
            padding="sm"
            size="30px" 
            :class="'browse ' + ($route.path === '/' ? 'nav-buttons' : '')"
            >
                Home
            </q-btn>

            <q-btn
            @click="$router.push('/questions')"
            flat 
            no-caps 
            padding="sm"
            size="30px" 
            :class="'browse ' + ($route.path === '/questions' ? 'nav-buttons' : '')"
            >
                Browse
            </q-btn>

            &nbsp;

            <q-btn 
            class="glossy" 
            round 
            color="primary" 
            padding="sm" 
            size="20px">
                <q-icon v-if="user.length > 0" name="person" />
                <q-icon v-else name="no_accounts" />

                <q-menu style="width: 20%">
                    <q-list v-if="user.length <= 0">
                        <login-register-form />
                        <login-register-form :registerUser="true" />
                    </q-list>
                    <q-item v-else clickable @click="useUserStore().logout()">
                       <q-item-section> Logout </q-item-section>
                    </q-item>
                </q-menu>
            </q-btn>
            
        </q-bar>
    </div>
    <q-separator color="black" />
</template>

<style scoped lang="scss">
.home{
    font-weight: normal;
    .q-focus-helper{
        display: none;
        }
}
.browse{
    font-weight: lighter;
    .q-focus-helper{
        display: none;
        }
}
.nav-buttons {
  text-decoration-line: underline;
  text-decoration-style: solid;
  text-decoration-thickness: 1%;
}
</style>