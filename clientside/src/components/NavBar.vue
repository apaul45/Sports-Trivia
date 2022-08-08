<script setup>

</script>

<template>
    <div class="q-pa-md q-gutter-sm">
        <q-bar class="bg-white">
            <q-btn 
            flat 
            no-caps 
            padding="none"
            :ripple="false" 
            size="40px" 
            class="home"
            > 
                Sports Trivia 
            </q-btn>

            <q-space />

            <q-btn 
            flat 
            no-caps 
            padding="sm"
            size="30px" 
            class="browse"
            >
                Home
            </q-btn>

            <q-btn 
            flat 
            no-caps 
            padding="sm"
            size="30px" 
            class="browse"
            >
                Browse
            </q-btn>
            &nbsp;
            <q-btn class="glossy" round color="primary" icon="card_giftcard" padding="sm" size="20px"  />
        </q-bar>
    </div>
    <q-separator color="black" />
</template>

<style scoped lang="scss">
    .home{
        font-weight: normal;
        .q-focus-helper{
            display: none;
         }
    }
    .browse{
        font-weight: lighter;
        .q-focus-helper{
            display: none;
         }
    }
</style>