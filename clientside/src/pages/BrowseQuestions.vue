<template>

    <h1 v-if="this.$route.path !== '/questions/add'" id="questions">Browse Questions</h1>
    <h1 v-else id="questions">Add Questions</h1>

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
        <add-question-modal-vue v-model:visible="visible"/>
    </div>
</template>

<script setup>
import { ref, onBeforeMount } from 'vue'
import backendApi from 'src/boot/axios.ts'
import AddQuestionModalVue from '../components/AddQuestionModal.vue';
import FilterSortQuestions from 'src/components/FilterSortQuestions.vue';

const filteredQuestions = ref([]);
const selectedQuestions = ref([]); //Used when user choosing questions to add to a set
const visible = ref(false); //used to invoke add form modal

onBeforeMount(async() => {
    let response = await backendApi.getAllQuestions()
    filteredQuestions.value = response.data;
});

const columns = [
    {
        name: 'username',
        required: true,
        label: 'User',
        align: 'left',
        field: (row) => row.username,
        sortable: true
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
        field: (row) => row.difficulty,
        sortable: true
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
    const style = "display: inline; \
                   padding: 7px; \
                   text-color: white; \
                   border-radius: 25px; \
                   background-color: #7CCB96; \
                   text-align: center; \
                   outline-style: solid;";

    return <div style="overflow: auto; line-height: 3.5;"> 
                {
                    tags.map(tag =>
                    <>
                        &nbsp;
                        <div style={style}>{tag}</div>
                        &nbsp; 
                    </>
                    )
                }
           </div>
}

</script>

<style scoped>
    #questions {
        font-size: 40px;
        font-weight: 500;
        text-align: center;
        justify-content: center;
    }
</style>