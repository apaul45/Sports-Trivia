<script setup>
import { ref, onBeforeMount } from 'vue'
import backendApi from 'src/boot/axios.ts'
import AddQuestionModalVue from './AddQuestionModal.vue';

const questions = ref([])
const visible = ref(false); //used to invoke add form modal

onBeforeMount(async() => {
    const response = await backendApi.getAllQuestions()
    console.log(response);
    questions.value = response.data
})

const columns = [
    {
        name: 'user',
        required: true,
        label: 'User',
        align: 'left',
        field: (row) => row.username
    },
    {
        name: 'question',
        required: true,
        label: 'Question',
        align: 'left',
        field: (row) => row.question
    },
    {
        name: 'answer',
        required: true,
        label: 'Answer',
        align: 'left',
        field: (row) => row.answer
    },
    {
        name: 'difficulty',
        required: true,
        label: 'Difficulty',
        align: 'left',
        field: (row) => row.difficulty
    }
]

</script>

<template>
    <div class="q-pa-md">
        <q-table
         :rows="questions"
         :columns="columns"
         row-key="name"
       />
        <q-btn label="Add a Question" no-caps color="primary" @click="visible = true" />
        
        <!-- v-model can be used to control the displaying and hiding of the add modal, 
        as it is the same as v-binding the visible ref and providing a update:visible event to change 
        the original visible ref in this component. 
        
        In other words, it can be used to sync a prop with a ref variable
        https://vuejs.org/guide/components/events.html#usage-with-v-model
        -->
        <add-question-modal-vue v-model:visible="visible"/>
    </div>
</template>

<style scoped lang="scss">
    tr{
        background-color: #B9EBC4 !important;
    }
</style>