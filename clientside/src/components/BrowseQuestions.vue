<script setup>
import { ref, onBeforeMount } from 'vue'
import backendApi from 'src/boot/axios.ts'

const questions = ref([])

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
        <!-- <q-btn dropdown color="gray" label="Sort By" dropdown-icon="change_history">
            <q-list>
                <q-item clickable v-close-popup>
                    Difficulty
                </q-item>
                <q-item clickable v-close-popup>
                    Player
                </q-item>
            </q-list>
        </q-btn> -->

        <!-- <q-btn color="red" text-color="white">Press to fill table</q-btn> -->

        <q-table
         :rows="questions"
         :columns="columns"
         row-key="name"
       />
    </div>
</template>

<style scoped lang="scss">
    tr{
        background-color: #B9EBC4 !important;
    }
</style>