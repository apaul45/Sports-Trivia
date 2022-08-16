<script setup>
import backendApi from 'src/boot/axios';
import { onBeforeMount, ref } from 'vue';

const userSets = ref([]);

onBeforeMount(async() => {
    const response = await backendApi.getUserSets("apaul45");
    console.log(response.data[0].doc);
    userSets.value = response.data[0].doc;
});
</script>

<template>
    <h1 id="questions">Welcome Back!</h1>

    <div class="q-gutter-md row items-start user-lists">
        <h2 class="list-headings">Your Lists</h2>
        <q-separator />
        <q-btn outline @click="$router.push('/set')">
            <q-icon name="add" />
        </q-btn>
    </div>

    <div class="q-pa-md row items-start q-gutter-md cards">
        <q-card v-for="set in userSets" class="my-card" clickable>
            <q-card-section>
                <div class="text-h6">{{set.title}}</div>
                <div class="text-subtitle2">{{set.questions.length}} questions</div>
            </q-card-section>
        </q-card>
    </div>

</template>

<style scoped>
    #questions {
        font-size: 40px;
        font-weight: 500;
        text-align: center;
        justify-content: center;
    }
    .list-headings {
        font-size: 40px;
        padding: 0% 0% 0% 2%;
        margin: 0%;
        font-weight: 400;
        text-align: left;
        justify-content: left;
    }
    .user-lists{
        position: relative;
        right: -2%;
    }
    .user-lists:after {
        content:' ';
        display: block;
        position: relative;
        right: -2%;
        border:1px solid black;
        width: 94%;
    }
    .cards{
        position: relative;
        right: -2%;
    }
    .my-card{
        width: 100%;
        max-width: 250px;
    }
</style>