<script setup>
import { ref, onBeforeMount } from 'vue'
import { columns } from 'src/table-config.js'
import backendApi from 'src/boot/axios.ts'
import AddQuestionModalVue from '../components/AddQuestionModal.vue';
import FilterSortQuestions from 'src/components/FilterSortQuestions.vue';
import { useSetStore } from 'src/stores/set-store';
import { useRouter } from 'vue-router';
import { useUserStore } from 'src/stores/user-store';

const filteredQuestions = ref([]);
const selectedQuestions = ref([]); //Used when user choosing questions to add to a set
const visible = ref(false); //used to invoke add form modal
const router = useRouter();

onBeforeMount(async() => {
    let response = await backendApi.getAllQuestions()
    filteredQuestions.value = response.data;
});

//Store and function below are only used for AddQuestions page 
const setStore = useSetStore();

function addSetToStore(){
    setStore.addToSet(selectedQuestions.value);
    router.push("/set");
}
</script>

<template>
    <h1 v-if="this.$route.path !== '/questions/add'" id="questions">Browse Questions</h1>
    <div v-else>
        <h1 id="questions">Add Questions</h1>
        <q-btn color="primary" @click="addSetToStore"> Finish Adding </q-btn>
    </div>

    <div class="q-pa-md">
        <br/>
        
        <filter-sort-questions v-model:filteredQuestions="filteredQuestions"/>

        <br/>

        <!-- Make sure to correctly configure the row key to be unique 
        so all rows aren't selected when one row is selected -->
        <q-table v-if="this.$route.path === '/questions/add'"
        :rows="filteredQuestions"
        :columns="columns"
        row-key="question"
        selection="multiple"
        v-model:selected="selectedQuestions"
        />

        <q-table v-else
        id="question-table"
        :rows="filteredQuestions"
        :columns="columns"
        />

        <q-btn 
        @click="visible = true" 
        label="Add a Question" 
        no-caps color="primary"
        />
        
        <!-- v-model can be used to control the displaying and hiding of the add modal, 
        as it is the same as v-binding the visible ref and providing a update:visible event to change 
        the original visible ref in this component. 
        
        In other words, it can be used to sync a prop with a ref variable
        https://vuejs.org/guide/components/events.html#usage-with-v-model
        -->
        <add-question-modal-vue v-model:visible="visible" v-model:filteredQuestions="filteredQuestions"/>
    </div>
</template>

<style scoped>
    #questions {
        font-size: 40px;
        font-weight: 500;
        text-align: center;
        justify-content: center;
    }
</style>