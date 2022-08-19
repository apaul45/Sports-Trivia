<script setup>
import { storeToRefs } from 'pinia';
import { useSetStore } from 'src/stores/set-store';
import { useUserStore } from 'src/stores/user-store';
import { columns } from 'src/table-config.js';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const setStore = useSetStore();
const { setBeingAdded } = storeToRefs(setStore);

const userStore = useUserStore();

const router = useRouter();

const questionsToDelete = ref([]);

async function saveSet(){
    await setStore.saveToDb();
    setStore.setDefault();
    router.push('/home');
}
</script>

<template>

    <q-input
    v-model="setBeingAdded.title"
    filled
    :rules="[ val => val && val.length > 0 || 'Please provide a value']"
    label="Set Name"
    bg-color="grey-4"
    class="set-name center-input"
    @blur="() => setStore.updateSet(setBeingAdded.title, 'title')"
    />

    <div class="q-pa-md">
        <q-btn color="primary" 
        @click="() => setStore.deleteFromSet(questionsToDelete)"> 
            Delete Selected Questions 
        </q-btn>

        <q-btn color="primary" 
        @click="() => setStore.setDefault()"> 
            Reset 
        </q-btn>

        <q-table 
        :rows="setStore.setBeingAdded.questions"
        :columns="columns"
        row-key="question"
        selection="multiple"
        v-model:selected="questionsToDelete"
        />

        <br/>

        <q-btn @click="$router.push('/questions/add')" color="primary" style="width:100%">
            Add More Questions
        </q-btn>

        <br/><br/>
        
        <q-btn @click="saveSet" color="primary" style="width:100%" >
            Save
        </q-btn>
    </div>

</template>

<style scoped>
    .center-input{
        margin: 2% auto; 
        display: block;
        text-align: center;
    }
    .set-name{
        width: 15%; 
    }
</style>