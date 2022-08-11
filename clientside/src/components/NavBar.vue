<script setup>
import router from 'src/router';
</script>

<template>
    <div class="q-pa-md q-gutter-sm">
        <q-bar class="bg-white">
            <q-btn 
            @click="$router.push('/')"
            flat 
            no-caps 
            padding="none"
            size="40px" ß
            class="home"
            v-close-popup
            > 
                Sports Trivia
            </q-btn>

            <q-space />

            <q-btn 
            @click="$router.push('/home')"
            flat 
            no-caps 
            padding="sm"
            size="30px" 
            class="browse"
            >
                Home
            </q-btn>

            <q-btn
            @click="$router.push('/questions')"
            flat 
            no-caps 
            padding="sm"
            size="30px" 
            class="browse"
            >
                Browse
            </q-btn>

            &nbsp;
            <q-btn class="glossy" round color="primary" icon="card_giftcard" padding="sm" size="20px"  />
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
</style>