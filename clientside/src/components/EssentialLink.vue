<script setup>
import { ref } from 'vue'
import backendApi from 'src/boot/axios.ts'

const value = ref('')
const query = ref('')

async function login () {
  console.log('reached login function')
  const response1 = await backendApi.loginUser('apaul21', 'testingfromvue')
  console.log(response1)
  backendApi.setHeader(response1.data.access_token)

  const response2 = await backendApi.createQuestion({
    question: 'With what pick did the New York Giants draft Odell Beckham Jr in the 2014 NFL Draft?',
    answer: '12',
    difficulty: 'easy',
    player: 'Odell Beckham Jr',
    tags: ['NFL', 'NFL Draft', 'Giants', 'New York Giants', 'New York Football Giants']
  })
  console.log(response2)
}

async function getQuery () {
  const response = await backendApi.getPlayerQuestions(query.value)
  console.log(response.data)
  if (response.status === 200 && response.data.length > 0) value.value = response.data
  else value.value = null
}
</script>

<template>
  <div>
    <q-btn color="primary" @click="login">Press this button to login</q-btn>

    <h5>Please enter a query</h5>
    <input v-model="query">
    <q-btn color="primary" @click="getQuery">Submit</q-btn>

    <div v-if="value != null">
      <div v-for="list in value" v-bind:key="list.doc">
        <q-responsive :ratio="5/1">
          <q-card
          class="my-card text-white"
          style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"
          v-for="question in list.doc" v-bind:key="question.question"
          >
            <q-card-section>
              <div class="text-h6">Question: {{question.question}}</div>
              <div class="text-subtitle2">Answer: {{question.answer}}</div>
            </q-card-section>
          </q-card>
        </q-responsive>
      </div>
    </div>
    <div v-else>
      Could not retrieve questions related to this player. Please check spelling or try again.
    </div>

  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
  h3 {
    margin: 40px 0 0;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  a {
    color: #42b983;
  }
</style>
