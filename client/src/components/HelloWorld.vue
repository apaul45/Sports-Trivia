<script>
import {ref} from 'vue';
import backendApi from '../axios-api';

export default({
  setup(){
    const value = ref('');

    async function login(){
      const response = await backendApi.registerUser({username: "k2p", passwordHash: "i like pp", email: "k2p@ilovepp", sets: []});
      console.log(response);
      const response2 = await backendApi.createQuestion({
          "question": "string",
  "answer": "string",
  "username": "string",
  "difficulty": "string",
  "player": "string",
  "tags": []
      });
      console.log(response2);
    }

    return{
      value, login
    };
  },
});

</script>

<template>
  <div class="hello">
    <button @click="login">
      Click this button to login
    </button>
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
