<script setup>

</script>

<template>
    <div class="q-pa-md q-gutter-sm">
        <q-bar class="bg-white">
            <q-btn flat no-caps size="40px" class="home"> Sports Trivia </q-btn>
            <q-space />
            <q-btn flat no-caps size="30px" class="browse">Home</q-btn>
            <q-btn flat no-caps size="30px" class="browse">Browse</q-btn>
        </q-bar>
    </div>
    <q-separator color="black" />
</template>

<style scoped lang="scss">
    q-bar{
        background-color: white;
    }
    .home{
        font-weight: normal;
    }
    .browse{
        font-weight: lighter;
    }
</style>