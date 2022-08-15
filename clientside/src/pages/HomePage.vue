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


    <h2 class="list-headings">Your Lists</h2>
    <div class="q-pa-md row items-start q-gutter-md">
        <q-card v-for="set in userSets" class="my-card">
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
        padding-left: 2%;
        font-weight: 400;
        text-align: left;
        justify-content: left;
    }
    h2:after {
        content:' ';
        display:block;
        border:1px solid black;
        width: 98%;
    }
    .my-card{
        width: 100%;
        max-width: 250px;
    }
</style>