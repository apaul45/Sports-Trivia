<script setup lang="ts">
import { storeToRefs } from 'pinia';
import backendApi from 'src/boot/axios';
import { errorStore } from 'src/stores/error-store';
import { useSetStore } from 'src/stores/set-store';
import { useUserStore } from 'src/stores/user-store';
import { Set } from 'src/types';
import { useRouter } from 'vue-router';

interface Props {
    sets: Set[]
}

const props = defineProps<Props>();
const emit = defineEmits(['update:sets']); 

const setStore = useSetStore();

const userStore = useUserStore()
const { user } = storeToRefs(userStore)

const router = useRouter();

const openSetPage = (set: Set) => {
    setStore.updateSet(set);
    router.push(`/set-page/${set._id}`);
}

//For user sets only

const editSet = (event: Event, setToUpdate: Set) => {
    event.stopPropagation();
    setStore.updateSet(setToUpdate);
    router.push(`/set/${setToUpdate._id}`);
}
const deleteSet = async(event: Event, setToDelete: Set) => {
    event.stopPropagation();
    try {
        await backendApi.deleteSet(setToDelete._id);
        emit('update:sets', setToDelete._id);
    }
    catch {
        errorStore.setMessage("Your set could not be deleted. Please try again.");
    }
}
</script>

<template>
    <div class="q-pa-md cards">
        <div class="row q-col-gutter-xs">
            <div class="col-2" v-for="set in props.sets" :key="`xs-${set._id}`">
                <q-card 
                class="my-card row" 
                clickable  
                @click="openSetPage(set)"
                >
                    <q-card-section class="card-sections">
                        <div class="row items-center">
                            <div class="col">
                                <div class="text-h6"> {{set.title}} </div>

                                <div v-if="set.username !== user" id="username"> 
                                    {{set.username}} ({{set.rating}}<q-icon name="star" />)
                                </div>

                                {{set.questions.length}} questions

                                <div v-if="set.username === user" class="col user-btns">
                                    <q-btn 
                                    round flat
                                    @click="(e) => editSet(e, set)"  
                                    icon="draw"
                                    />

                                    <q-btn 
                                    round flat 
                                    @click="(e) => deleteSet(e, set)" 
                                    icon="delete" 
                                    />
                                </div>
                            </div>
                        </div>
                    </q-card-section>
                </q-card>
            </div>
        </div>
    </div>
</template>

<style scoped>
    .cards{
        position: relative;
        right: -2%;
        width: 100%;
    }
    .card-sections{
        padding-right: 0%;
    }
    .my-card{
        max-width: 80%;
        margin-bottom: 4%;
    }
    .my-card:hover {
        background-color: #0a2e67;
        color: white;
    }
    #username {
        padding-bottom: 6%;
    }
    .user-btns {
        margin-top: 13%;
    }
</style>