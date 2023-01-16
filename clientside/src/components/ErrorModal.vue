<script setup lang="ts">
import { errorStore } from 'src/stores/error-store';
import { computed } from 'vue';

const isError = computed(() => 
    errorStore.message.length > 0
);

const clearError = () => {
    errorStore.setMessage("");
}

</script>

<template>
    <q-dialog v-model="isError">
        <q-card>
            <q-card-section>
                {{ errorStore.message }}
            </q-card-section>

            <q-card-actions align="right">
                <q-btn 
                @click="clearError"
                flat 
                label="OK" 
                color="primary" 
                v-close-popup />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>