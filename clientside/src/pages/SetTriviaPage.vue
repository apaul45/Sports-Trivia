<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useSetStore } from 'src/stores/set-store';
import { ref } from 'vue';

const { setBeingViewed } = storeToRefs(useSetStore());

const questionInputs = ref<Array<string>>(Array.from(''.repeat(setBeingViewed.value.questions.length)));

const rightAnswers = ref<number>(-1);

const determineResults = () => {
    rightAnswers.value = 0;

    for (let i=0; i<setBeingViewed.value.questions.length; i++){
        const userAnswer = questionInputs.value[i];

        if (userAnswer.length > 0 &&  userAnswer.includes(setBeingViewed.value.questions[i].answer)){
            rightAnswers.value++;
        }
    }
}
</script>

<template>
    <div class="center-items">

        <h1 id="set-name"> {{setBeingViewed.title}} </h1>

        <div class="q-gutter-md row items-start center-items">
            <h4 class="set-metadata">
                {{setBeingViewed.username}} 
                ({{setBeingViewed.rating}} <q-icon name="star"/>)
            </h4>

            <h4 class="set-metadata">{{setBeingViewed.questions.length}} questions</h4>
        </div>

        <div v-for="(question, index) in setBeingViewed.questions">
            <h6>{{index+1}}. {{question.question}}</h6>
            <q-input
            v-model="questionInputs[index]"
            class="center-input"
            style="width: 30%"
            filled
            bg-color="grey-4"
            />
        </div>

        <q-btn
        @click="determineResults"
        label="Submit"
        type="submit"
        color="primary"
        />

        <div v-if="rightAnswers >= 0" style="color: green">
            {{rightAnswers}}/{{setBeingViewed.questions.length}} correct!
        </div>
    </div>
</template>

<style scoped>
.center-items{
    align-items: center;
    justify-content: center;
    text-align: center;
}
.center-input{
    margin: 2% auto; 
    display: block;
    text-align: center;
}
.set-metadata{
    padding-right: 3%;
}
#set-name {
    font-size: 40px;
    font-weight: 500;
}
</style>