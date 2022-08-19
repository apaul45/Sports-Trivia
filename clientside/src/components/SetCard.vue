<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useSetStore } from 'src/stores/set-store';
import { useUserStore } from 'src/stores/user-store';
import { Set } from 'src/types';
import { useRouter } from 'vue-router';

interface Props{
    sets: Set[]
}

const props = defineProps<Props>();

const setStore = useSetStore();

const userStore = useUserStore()
const { user } = storeToRefs(userStore)

const router = useRouter();

const openSetPage = (set: Set) => {
    setStore.updateSetBeingViewed(set);
    router.push(`/set-page/${set.position}`);
}
</script>

<template>
    <div class="q-pa-md row items-start q-gutter-md cards">
        <q-card v-for="set in props.sets" class="my-card" clickable @click="openSetPage(set)">
            <q-card-section>
                <div class="row items-center no-wrap">
                    <div class="col">
                        <div class="text-h6"> {{set.title}} </div>
                        <div v-if="set.username !== user">
                            {{set.username}}
                        </div>
                        {{set.questions.length}} questions
                        <br/>
                        {{set.rating}}<q-icon name="star" />
                    </div>

                    <div v-if="set.username === user" class="col-auto">
                        <q-btn color="grey-7" round flat icon="more_vert">
                            <q-menu auto-close>
                                <q-list>
                                    <q-item clickable>
                                        <q-item-section>Edit Set</q-item-section>
                                    </q-item>
                                    <q-item clickable>
                                        <q-item-section>Delete Set</q-item-section>
                                    </q-item>
                                </q-list>
                            </q-menu>
                        </q-btn>
                    </div>
                </div>
            </q-card-section>
        </q-card>
    </div>
</template>

<style scoped>
    .cards{
        position: relative;
        right: -2%;
    }
    .card-sections{
        padding-left: 2%;
    }
    .my-card{
        width: 100%;
        max-width: 250px;
    }
</style>