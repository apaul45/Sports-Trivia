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
    },
    {
        name: 'tags',
        required: true, 
        label: "Tags",
        align:'center',
        field: (row) => createTagCards(row.tags)
    }
]

const createTagCards = (tags) => {
    return <div style="overflow: auto; line-height: 3.5;"> 
                {
                    tags.map(tag =>
                    <>
                        &nbsp;
                        <div style="display: inline; padding: 7px; text-color: white; border-radius: 25px; background-color: #7CCB96; text-align: center; outline-style: solid">
                            {tag}
                        </div>
                        &nbsp; 
                    </>
                    )
                }
           </div>
}

</script>

<template>
    <h1 id="questions">Browse Questions</h1>
    <div class="q-pa-md">
        <q-table
         id="question-table"
         :rows="questions"
         :columns="columns"
         row-key="name"
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
        <add-question-modal-vue v-model:visible="visible"/>
    </div>
</template>

<style scoped>
    tr{
        background-color: #B9EBC4 !important;
    }
    #questions {
        font-size: 40px;
        font-weight: 500;
        text-align: center;
        justify-content: center;
    }
</style>