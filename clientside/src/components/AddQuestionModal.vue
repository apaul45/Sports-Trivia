<script setup>
import backendApi from 'src/boot/axios';
import { errorStore } from 'src/stores/error-store';
import {reactive} from 'vue';

const props = defineProps({visible: Boolean, filteredQuestions: Array});
const emit = defineEmits(['update:visible', 'update:filteredQuestions']);

const defaultQuestion = {
    question: "", 
    answer: "", 
    difficulty: "", 
    tags: [],
    username: "", 
    player: ""
}

const inputFields = ["question", "answer", "player"]; //Use to reduce duplicate q-inputs
const difficultyOptions = [
    {
        label: 'Easy',
        value: 'easy'
    },
    {
        label: 'Medium',
        value: 'medium'
    },
    {
        label: 'Hard',
        value: 'hard'
    }
]

const question = reactive({...defaultQuestion});

async function addQuestion(){
    try {
        await backendApi.createQuestion(question); 
        const response = await backendApi.getAllQuestions(); 
        emit('update:filteredQuestions', response.data);
        emit('update:visible', false);
    }
    catch(error) {
        errorStore.setMessage("There was a problem adding your question. Please try again.");
    }
}  

function onReset() {
    Object.assign(question, {...defaultQuestion});
}
</script>

<template>
    <q-dialog v-model="props.visible">
        <q-card>
            <q-card-section class="row items-center">
                <q-form 
                class="q-gutter-md"
                @submit="addQuestion" 
                @reset="onReset" 
                >
                    <!-- Use label-slot and v-slot: label to customize the input field's label -->
                    <div v-for= "value in inputFields" :key="value">
                        <q-input
                        filled
                        v-model="question[value]"
                        lazy-rules
                        :rules="[ val => val && val.length > 0 || 'Please provide a value']"
                        label-slot clearable
                        >
                            <template v-slot:label>
                                <div class="row items-center all-pointer-events"> 
                                    {{value[0].toUpperCase() + value.substr(1)}} 
                                </div>
                            </template>
                        </q-input>
                    </div>

                    <q-option-group
                    name="Difficulty"
                    v-model="question.difficulty"
                    :options="difficultyOptions"
                    color="primary"
                    inline
                    />

                    <q-select
                    label="Tags"
                    filled
                    v-model="question.tags"
                    use-input
                    use-chips
                    multiple
                    hide-dropdown-icon
                    input-debounce="0"
                    new-value-mode="add"
                    style="width: 95%"
                    />

                    <q-btn label="Reset" type="reset" color="primary" flat/>
                    <q-btn label="Submit" type="submit" color="primary"/>
                    <q-btn 
                    @click="$emit('update:visible', false)" 
                    label="Cancel" 
                    color="primary"
                    flat
                    v-close-popup
                    />
                </q-form>
            </q-card-section>
        </q-card>
    </q-dialog>
</template>