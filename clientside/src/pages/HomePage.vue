<script setup lang="ts">
import backendApi from 'src/boot/axios';
import { Set } from 'src/types';
import { onBeforeMount, ref } from 'vue';
import SetCard from 'src/components/SetCard.vue';
import { storeToRefs } from 'pinia';
import { useUserStore } from 'src/stores/user-store';
import { computed } from '@vue/reactivity';

const { user, userSets } = storeToRefs(useUserStore());

const allSets = ref<Array<Set>>([]);

onBeforeMount(async() => {
    const response = await backendApi.getAllSets();
    allSets.value = response.data;
});

//Since user is a state variable (meaning it's a ref which is reactive), allSets will filter whenever it changes
//Use user state var along with the computed properly to dynamically update the cards shown under "All Lists"
const sets = computed(() => allSets.value.filter((set) => set.username !== user.value));

</script>

<template>
    <h1 id="questions">Welcome Back!</h1>

    <div v-if="user.length > 0">
        <div class="q-gutter-md row items-start lists">
            <h2 class="list-headings">Your Lists</h2>
            <q-separator />
            <q-btn outline @click="$router.push('/set')">
                <q-icon name="add" />
            </q-btn>
        </div>

        <set-card v-model:sets="userSets" />

        <br/><br/>
    </div>

    <div class="q-gutter-md row items-start lists">
        <h2 class="list-headings">All Lists</h2>
        <q-separator />
    </div>

    <set-card v-model:sets="sets" />
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
    .lists{
        position: relative;
        right: -2%;
    }
    .lists:after {
        content:' ';
        display: block;
        position: relative;
        right: -2%;
        border:1px solid black;
        width: 94%;
    }
</style>