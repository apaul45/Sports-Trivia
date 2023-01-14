<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useSetStore } from 'src/stores/set-store';
import { TrackedSet } from 'src/types';
import { Ref, ref } from 'vue';

const { set } = storeToRefs(useSetStore());

const index: Ref<number> = ref(-1);
const trackedSet: Ref<TrackedSet> = ref(set.value);

const checkAnswer = () => {
    const inputtedAnswer = trackedSet.value.questions[index.value].inputtedAnswer?.toLowerCase();
    const correctAnswer = trackedSet.value.questions[index.value].answer.toLowerCase();

    trackedSet.value.questions[index.value].correct = (inputtedAnswer === correctAnswer);
}

const getCorrectCount = () => {
    let correctCount = 0;

    trackedSet.value.questions.forEach((question) => {
        if (question.correct) {
            correctCount++;
        }
    });

    return correctCount;
}

const reset = () => {
    index.value = 0;

    trackedSet.value.questions.map((question) => {
        question.correct = undefined;
        question.inputtedAnswer = "";
    });
}
</script>

<template>
    <div class="q-pa-xl center-items">
        <h1 id="set-name"> {{set.title}} </h1>
        
        <h6 id="set-user"> 
            {{set.username}} ({{set.rating}}<q-icon name="star"/>) 
        </h6>

        <q-card>
            <q-card-section v-if="index<0" class="fade-in-text">
                <h4 class="header">
                    Put your knowledge to the test!
                </h4>

                <q-btn @click="index=0">
                    Start
                </q-btn>
            </q-card-section>

            <q-card-section v-else-if="index < trackedSet.questions.length">
                <h5 class="header"> 
                    <q-icon 
                    v-if="trackedSet.questions[index].correct" 
                    name="check" 
                    color="green" />

                    <q-icon 
                    v-else-if="trackedSet.questions[index].correct !== undefined" 
                    name="close" 
                    color="red" 
                    />

                    {{ index + 1 }}. {{ trackedSet.questions[index].question }} 
                </h5>
                
                <q-input
                v-model="trackedSet.questions[index].inputtedAnswer"
                class="center-input"
                filled
                bg-color="grey-4"
                label="Answer"
                :disable="trackedSet.questions[index].correct !== undefined"
                @keyup.enter="checkAnswer"
                />

                <div 
                v-if="trackedSet.questions[index].correct !== undefined && !trackedSet.questions[index].correct"
                id="answer-txt"
                >
                    Correct Answer: <b> {{ trackedSet.questions[index].answer }} </b>
                </div>

                <q-btn 
                v-if="index > 0" 
                @click="index--" 
                class="question-button" 
                round>
                    <q-icon name="arrow_back_ios" />
                </q-btn> 
                
                &nbsp;

                <q-btn color="red" 
                @click="checkAnswer" 
                class="question-button"
                :disable="trackedSet.questions[index].correct !== undefined">
                    <q-icon name="check" /> &nbsp; Check answer
                </q-btn> 
                
                &nbsp;

                <q-btn 
                @click="index++" 
                class="question-button" 
                round>
                    <q-icon name="arrow_forward_ios" />
                </q-btn>
            </q-card-section>

            <q-card-section v-else class="fade-in-text">
                <h4 class="header">
                    You got <b> {{ getCorrectCount() }} </b> questions right!
                </h4>

                <q-btn @click="reset" color="primary">
                    Start over
                </q-btn>
            </q-card-section>
        </q-card>
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
    width: 20%;
}
#answer-txt {
    padding-bottom: 2%;
    font-size: large;
}
#answer-txt > b {
    padding-bottom: 2%;
    font-size: large;
    color: red;
}
#set-name {
    font-size: 50px;
    font-weight: 500;
}
#set-user {
    font-size: 25px;
    font-weight: 350;
    padding-bottom: 4%;
}
h1, h6 {
    margin-top: 0%;
    margin-bottom: 0%;
}
.header {
    margin-bottom: 0%;
    margin-top: 1.6%;
}
.question-button {
    margin-bottom: 1.6%;
}
.fade-in-text {
  font-family: Arial;
  font-size: 60px;
  animation: fadeIn 2s;
  -webkit-animation: fadeIn 2s;
  -moz-animation: fadeIn 2s;
  -o-animation: fadeIn 2s;
  -ms-animation: fadeIn 2s;
}

@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-moz-keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-webkit-keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-o-keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@-ms-keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}
</style>