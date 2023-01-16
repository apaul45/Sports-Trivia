<script setup>
import {onBeforeMount, reactive} from 'vue'
import backendApi from 'src/boot/axios';
import { 
    QInput, 
    QIcon, 
    QSelect, 
    QItem, 
    QBtn, 
    QDrawer 
} from 'quasar';
import { errorStore } from 'src/stores/error-store';

const props = defineProps({filteredQuestions: Array, show: Boolean});
const emit = defineEmits(['update:filteredQuestions']);

const refs = reactive({
    searchText: '',
    users: [],
    filteredUsers: [],
    tags: [],
    filteredTags: []
});

onBeforeMount(async() => {
    try {
        let response = await backendApi.getAllUsers();
        refs.users = response.data.map((user) => user.username);
        response = await backendApi.getAllTags();
        refs.tags = response.data;
    }
    catch {
        errorStore.setMessage("There was an error retrieving filters. Please reload the page.");
    }
});

function resetQuestions(){
    refs.filteredTags = [];
    refs.filteredUsers = [];
    refs.searchText = "";
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

    try {
        const response = (
            result.length > 0 
            ? await backendApi.getFilteredQuestions(result)
            : await backendApi.getAllQuestions()
        );

        emit('update:filteredQuestions', response.data);
        emit('update:show', false);
    }
    catch {
        errorStore.setMessage("A problem occurred when filtering, please try again.");
    }
}
</script>

<template>
    <q-drawer
    v-model="show"
    show-if-above
    side="right"
    overlay
    bordered
    class="bg-grey-2"
    :width="400"
    :breakpoint="500"
    >

    <div class="q-pa-sm">
        <h1 class="container">Filters</h1>

        <q-form @submit="filterQuestions" @reset="resetQuestions">
            <q-item>
                <q-input 
                outlined 
                v-model="refs.searchText" 
                class="form-element"
                dense
                >
                    <template v-slot:prepend>
                        <q-icon name="search" />
                    </template>
                </q-input>
            </q-item>

            <q-item>
                <q-select
                label="Users"
                class="form-element"
                v-model="refs.filteredUsers"
                :options="refs.users"
                filled
                use-chips
                multiple
                dense
                />
            </q-item>

            <q-item>
                <q-select
                label="Tags"
                class="form-element"
                v-model="refs.filteredTags"
                :options="refs.tags"
                filled
                bg-color="grey-3"
                use-chips
                multiple
                dense
                />
            </q-item>

            <q-item>
                <q-btn label="Reset" type="reset" flat color="primary"/>
                <q-space/>
                <q-btn label="Submit" type="submit" color="primary"/>
            </q-item>
        </q-form>
    </div>
    </q-drawer>
</template>

<style scoped lang="scss">
.container {
    font-size: 25px;
    font-weight: 400;
    text-align: center;
    line-height: normal;
    margin-top: 10%;
}
.form-element {
    width: 100%;
}
</style>