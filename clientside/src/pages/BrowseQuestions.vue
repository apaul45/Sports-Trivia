<script setup>
import { ref, onBeforeMount } from 'vue'
import { columns } from 'src/table-config.js'
import backendApi from 'src/boot/axios.ts'
import AddQuestionModalVue from '../components/AddQuestionModal.vue';
import FilterSortQuestions from 'src/components/FilterSortQuestions.vue';
import { useSetStore } from 'src/stores/set-store';
import { useRouter } from 'vue-router';
import { storeToRefs } from 'pinia';
import { useUserStore } from 'src/stores/user-store';
import { errorStore } from 'src/stores/error-store';

const showQuestionModal = ref(false);
const showFilters = ref(false);
const filteredQuestions = ref([]);

const router = useRouter();
const currentRoute = router.currentRoute.value.path;

const setStore = useSetStore();
const { set } = storeToRefs(setStore);
const { user } = storeToRefs(useUserStore());

onBeforeMount(async() => {
    if (currentRoute === '/set') {
        setStore.setDefault();
    }

    try {
        let response = await backendApi.getAllQuestions()
        filteredQuestions.value = response.data;
    }
    catch {
        errorStore.setMessage("There was a problem retrieving questions. Please reload the page.");
    }
});

const saveSet = async() => {
    await setStore.saveToDb(currentRoute === '/set' ? 'POST' : 'PUT');
    setStore.setDefault();
    router.push('/home');
}
</script>

<template>
    <div class="q-pa-md">

        <h1 v-if="$route.path === '/questions'" id="questions">
            Browse Questions
        </h1>

        <q-input
        v-else
        v-model="set.title"
        filled
        :rules="[ val => val && val.length > 0 || 'Please provide a value']"
        label="Set Name"
        bg-color="grey-4"
        class="set-name center-input"
        />

        <q-item class="buttons">
            <q-btn 
            @click="showFilters = !showFilters" 
            v-bind:label="(showFilters ? 'CLOSE' : 'SHOW') + ' FILTERS'" 
            no-caps 
            v-bind:color="showFilters ? 'black' : 'white'"
            v-bind:text-color="showFilters ? 'white' : 'black'"
            >
                <q-icon name="filter_list" />
            </q-btn>
        </q-item>

        <q-item v-if="user.length>0" class="buttons">
            <q-btn 
            @click="showQuestionModal = true" 
            label="Add a Question" 
            no-caps color="primary"
            />
        </q-item>

        <q-layout view="hHh Lpr lff" 
        container 
        v-bind:style="$route.path === '/questions' ? 'height: 1000px;' : 'height:1070px'" 
        class="rounded-borders"
        >
            <filter-sort-questions 
            v-model:show="showFilters"
            v-model:filteredQuestions="filteredQuestions"
            />

            <q-page-container>
                <!-- Make sure to correctly configure the row key to be unique 
                so all rows aren't selected when one row is selected -->
                <q-table 
                v-if="$route.path === '/questions'"
                :rows="filteredQuestions"
                :columns="columns"
                :loading="filteredQuestions.length === 0"
                dark
                />

                <q-table v-else
                :rows="filteredQuestions"
                :columns="columns"
                row-key="question"
                selection="multiple"
                v-model:selected="set.questions"
                :loading="filteredQuestions.length === 0"
                dark
                >
                    <template v-slot:top>
                        <q-btn color="primary" @click="saveSet"> 
                            Finish Adding To Set
                        </q-btn>
                    </template>
                </q-table>
                
                <!-- v-model can be used to control the displaying and hiding of the add modal, 
                as it is the same as v-binding the visible ref and providing a update:visible event to change 
                the original visible ref in this component. 
                
                In other words, it can be used to sync a prop with a ref variable
                https://vuejs.org/guide/components/events.html#usage-with-v-model
                -->
                <add-question-modal-vue 
                v-model:visible="showQuestionModal" 
                v-model:filteredQuestions="filteredQuestions"
                />
            </q-page-container>
        </q-layout>
    </div>
</template>

<style scoped>
#questions {
    font-size: 40px;
    font-weight: 500;
    text-align: center;
    justify-content: center;
}
.center-input{
    margin: 2% auto; 
    display: block;
    text-align: center;
}
.set-name{
    width: 15%; 
}
.buttons {
    float: right;
}
</style>