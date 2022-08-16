<script setup>



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

</script>

<template>
    <q-input
    filled
    :rules="[ val => val && val.length > 0 || 'Please provide a value']"
    label="Set Name"
    bg-color="grey-4"
    class="set-name center-input"
    />

    <div class="q-pa-md">
        <q-table 
        :rows="columns"
        :columns="columns"
        />
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