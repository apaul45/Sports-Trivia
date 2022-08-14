<script setup>
import {onBeforeMount, ref, watch} from 'vue'
import backendApi from 'src/boot/axios';

const props = defineProps({filteredQuestions: Array, questions: Array});
const emit = defineEmits(['update:filteredQuestions']);

const searchText = ref('');
const users = ref([])
const tags = ref([])

onBeforeMount(async() => {
    let response = await backendApi.getAllUsers()
    console.log(response)
    users.value = response.data
    response = await backendApi.getAllTags()
    tags.value = response.data
});

const doNothing = () => {}

watch(searchText, (newText) => {
    filterQuestions(newText, 'player');
});

const filterQuestions = (newText, field) => {
    let result = [];
    
    if (newText.length == 0) result = props.questions;
    else result = props.filteredQuestions.filter((question) => question[field] === newText);

    console.log(result);

    emit('update:filteredQuestions', result);
}
</script>

<template>
    <div class="q-gutter-md row items-start">
        <q-input 
        style="width: 40%"
        outlined 
        v-model="searchText" 
        >
            <template v-slot:prepend>
                <q-icon name="search" />
            </template>
        </q-input>

        <q-space />
        
        <q-btn-dropdown color="grey-3" text-color="black" size="lg" no-caps label="Users">
            <q-list>
                <q-item v-for="user in users" clickable v-close-popup @click="filterQuestions(user.username, 'username')">
                    {{user.username}}
                </q-item>
            </q-list>
        </q-btn-dropdown>

        <q-select
        filled
        bg-color="grey-3"
        label="Tags"
        v-model="model"
        use-input
        use-chips
        multiple
        :options="tags"
        @filter="filterFn"
        style="width: 250px"
        >
            <template v-slot:append>
                <q-btn @click="doNothing" color="primary" type="submit"  label="Submit"/>
            </template>
        </q-select>

        <q-btn-dropdown color="grey-3" text-color="black" size="lg"  no-caps label="Sort By">
            <q-list>
                <q-item clickable v-close-popup @click="onItemClick">
                    <q-item-section>
                        <q-item-label>Difficulty</q-item-label>
                    </q-item-section>
                </q-item>
            </q-list>
        </q-btn-dropdown>
    </div>
</template>