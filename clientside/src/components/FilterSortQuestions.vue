<script setup>
import {onBeforeMount, ref} from 'vue'
import backendApi from 'src/boot/axios';

const props = defineProps({filteredQuestions: Array});
const emit = defineEmits(['update:filteredQuestions']);

const searchText = ref('');
const users = ref([]);
const filteredUsers = ref([]);
const tags = ref([]);
const filteredTags = ref([]);

onBeforeMount(async() => {
    let response = await backendApi.getAllUsers()
    console.log(response)
    users.value = response.data.map((user) => user.username);
    response = await backendApi.getAllTags()
    tags.value = response.data;
});

async function resetQuestions(){
    const response = await backendApi.getAllQuestions();
    filteredTags.value = [];
    filteredUsers.value = [];
    searchText.value = [];
    emit('update:filteredQuestions', response.data);
}

async function filterQuestions(){
    let result = [];

    if (searchText.value.length > 0){
        result.push({player: searchText.value});
    }
    if (filteredUsers.value.length > 0){ 
        result.push({username: {$in: filteredUsers.value}});
    }
    if (filteredTags.value.length > 0){
        result.push({tags: {$in: filteredTags.value}});
    }

    if (result.length == 0) {
        resetQuestions();
        return;
    }

    const response = await backendApi.getFilteredQuestions(result);
    emit('update:filteredQuestions', response.data);
}

</script>

<template>
    <div class="q-gutter-md row items-start" style="align-items: center; justify-content: center;;">
        <q-input 
        style="width: 30%"
        outlined 
        v-model="searchText" 
        >
            <template v-slot:prepend>
                <q-icon name="search" />
            </template>
        </q-input>

        <q-select
        label="Users"
        v-model="filteredUsers"
        :options="users"
        filled
        use-chips
        multiple
        style="width: 10%"
        >
        </q-select>

        <q-select
        label="Tags"
        v-model="filteredTags"
        :options="tags"
        filled
        bg-color="grey-3"
        use-chips
        multiple
        style="width: 10%"
        >
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
        <q-btn @click="resetQuestions" label="Reset" color="grey-3" text-color="black"/>
        <q-btn @click="filterQuestions" label="Submit" type="submit" color="primary"/>
    </div>
</template>