<script setup>
import backendApi from 'src/boot/axios';
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

const question = reactive({...defaultQuestion});

async function addQuestion(){
    await backendApi.createQuestion(question.value); //TODO: Add error handling
    const response = await backendApi.getAllQuestions(); 
    emit('update:filteredQuestions', response.data);
    emit('update:visible', false);
}  

function onReset() {
    Object.assign(question, {...defaultQuestion});
}
</script>

<template>
    <q-dialog v-model="props.visible">
        <q-card>
            <q-card-section class="row items-center">
                <q-form @submit="addQuestion" @reset="onReset" class="q-gutter-md">
                    <!-- Use label-slot and v-slot: label to customize the input field's label -->
                    <div v-for= "value in inputFields" v-bind:key="value">
                        <q-input
                        filled
                        v-model="question[value]"
                        lazy-rules
                        :rules="[ val => val && val.length > 0 || 'Please provide a value']"
                        label-slot clearable
                        >
                            <template v-slot:label>
                                <div class="row items-center all-pointer-events"> {{value[0].toUpperCase() + value.substr(1)}} </div>
                            </template>
                        </q-input>
                    </div>

                    <q-radio v-model="question.difficulty" checked-icon="task_alt" unchecked-icon="panorama_fish_eye" val="easy" label="Easy" />
                    <q-radio v-model="question.difficulty" checked-icon="task_alt" unchecked-icon="panorama_fish_eye" val="medium" label="Medium" />
                    <q-radio v-model="question.difficulty" checked-icon="task_alt" unchecked-icon="panorama_fish_eye" val="hard" label="Hard" />

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
                    style="width: 250px"
                    />

                    <q-btn label="Submit" type="submit" color="primary"/>
                    <q-btn label="Reset" type="reset" color="primary" flat/>
                    <q-btn 
                    @click="$emit('update:visible', false)" 
                    label="Cancel" 
                    color="primary"
                    flat
                    v-close-popup/>
                </q-form>
            </q-card-section>
        </q-card>
    </q-dialog>
</template>