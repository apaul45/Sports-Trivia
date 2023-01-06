<script setup>
import {onBeforeMount, reactive} from 'vue'
import backendApi from 'src/boot/axios';
import { QInput, QIcon, QSelect, QBtnDropdown, QList, QItem, QItemSection, QItemLabel, QBtn } from 'quasar';

const props = defineProps({filteredQuestions: Array});
const emit = defineEmits(['update:filteredQuestions']);

const refs = reactive({
    searchText: '',
    users: [],
    filteredUsers: [],
    tags: [],
    filteredTags: []
});

onBeforeMount(async() => {
    let response = await backendApi.getAllUsers();
    refs.users = response.data.map((user) => user.username);
    response = await backendApi.getAllTags();
    refs.tags = response.data;
});

async function resetQuestions(){
    const response = await backendApi.getAllQuestions();
    refs.filteredTags = [];
    refs.filteredUsers = [];
    refs.searchText = "";
    emit('update:filteredQuestions', response.data);
}

async function filterQuestions(){
    let result = [];

    if (refs.searchText.length > 0){
        result.push({player: refs.searchText});
    }
    if (refs.filteredUsers.length > 0){ 
        result.push({username: {$in: refs.filteredUsers}});
    }
    if (refs.filteredTags.length > 0){
        result.push({tags: {$in: refs.filteredTags}});
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
        v-model="refs.searchText" 
        >
            <template v-slot:prepend>
                <q-icon name="search" />
            </template>
        </q-input>

        <q-select
        label="Users"
        v-model="refs.filteredUsers"
        :options="refs.users"
        filled
        use-chips
        multiple
        style="width: 10%"
        >
        </q-select>

        <q-select
        label="Tags"
        v-model="refs.filteredTags"
        :options="refs.tags"
        filled
        bg-color="grey-3"
        use-chips
        multiple
        style="width: 10%"
        >
        </q-select>

        <q-btn-dropdown color="grey-3" text-color="black" size="lg"  no-caps label="Sort By">
            <q-list>
                <q-item clickable v-close-popup>
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