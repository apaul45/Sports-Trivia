<script setup>
    import {ref} from 'vue';
    import backendApi from '../boot/axios'

    const props = defineProps({visible: Boolean});

    const defaultQuestion = {
        question: "", 
        answer: "", 
        difficulty: "", 
        tags: [],
        username: "", 
        player: ""
    }

    const inputFields = ["question", "answer", "player"]; //Use to reduce duplicate q-inputs

    const question = ref(defaultQuestion);

    function addQuestion(){
        // question.value.username = "stringapaul32";
        // const response = await backendApi.createQuestion(question.value);
        // console.log(response);
        console.log(question);
    }   
</script>

<template>
        <q-dialog v-model="props.visible">
            <q-card>
                <q-card-section class="row items-center">
                    <q-form class="q-gutter-md">
                        <!-- Use label-slot and v-slot: label to customize the input field's label -->
                        <div v-for= "value in inputFields" v-bind:key= "value">
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

                        <q-radio v-model="question.difficulty" checked-icon="task_alt" unchecked-icon="panorama_fish_eye" val="line" label="easy" />
                        <q-radio v-model="question.difficulty" checked-icon="task_alt" unchecked-icon="panorama_fish_eye" val="rectangle" label="medium" />
                        <q-radio v-model="question.difficulty" checked-icon="task_alt" unchecked-icon="panorama_fish_eye" val="ellipse" label="hard" />

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

                        <q-btn @click="addQuestion" label="Submit" type="submit" color="primary"/>
                        <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />

                    </q-form>
                </q-card-section>

                <q-card-actions>
                    <q-btn flat label="Cancel" color="primary" v-close-popup @click="$emit('update:visible', false)" />
                </q-card-actions>
            </q-card>
        </q-dialog>
</template>