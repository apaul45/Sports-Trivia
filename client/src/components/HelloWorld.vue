<script>
import {ref} from 'vue';
import backendApi from '../axios-api';

export default({
  setup(){
    const value = ref('');
    const query = ref('');

    async function login(){
      console.log("reached login function")
      const response1 = await backendApi.loginUser("apaul21", "testingfromvue");
      console.log(response1);
      backendApi.setHeader(response1.data.access_token);

      const response2 = await backendApi.createQuestion({
          "question": "With what pick did the New York Giants draft Odell Beckham Jr in the 2014 NFL Draft?",
          "answer": "12",
          "difficulty": "easy",
          "player": "Odell Beckham Jr",
          "tags": ["NFL", "NFL Draft", "Giants", "New York Giants", "New York Football Giants"]
      });
      console.log(response2);
    }

    async function getQuery(){
      let response = null;
      if (query.value.includes(" ")) response = await backendApi.getPlayerQuestions(query.value);
      else response = await backendApi.getUserQuestions(query.value);

      console.log(response);
      value.value = response.data;
    }

    return{
      value, login, query, getQuery
    };
  },
});

</script>

<template>
  <div class="hello">
    <button @click="login">
      Click this button to login
    </button>

    <h5>Please enter a query</h5>
    <input v-model="query">
    <button @click="getQuery">Submit</button>

    <h6>Query Value: {{value}}</h6>
  </div>
</template>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
