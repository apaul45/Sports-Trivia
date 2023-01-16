<template>
  <nav-bar />
  <router-view :key="$route.path"/>
  <error-modal />
</template>

<script setup>
import { RouterView } from 'vue-router';
import NavBar from './components/NavBar.vue';
import ErrorModal from './components/ErrorModal.vue';
</script>
