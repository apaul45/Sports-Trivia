import { defineStore } from "pinia";
import { Question, Set } from "src/types";
import backendApi from "src/boot/axios";
import { errorStore } from "./error-store";

interface State {
    set: Set
}

const defaultSet: Set = {
    title: '', 
    username: 'apaul45', 
    questions: [], 
    rating: 0
};

export const useSetStore = defineStore<string, State>('sets', {  
     state: () => ({
        set: defaultSet
      }),
      getters: {},
      actions: {
        setDefault() {
            this.set.questions = [];
            this.set.title = '';
            this.set.rating = 0;
            this.set._id = undefined;
        },
        updateSet(set: Set) {
            this.set = set;
        },
        addToSet(questions: Array<Question>) {
            this.set.questions.push(...questions);
        },
        deleteFromSet(questions: Array<Question>) {
            this.set.questions = this.set.questions.filter(
                (question) => questions.indexOf(question) == -1
            );
        },
        updateSetField(value: never, field: keyof Set) {
            this.set[field] = value;
        },
        async saveToDb(method: string) {
            //TODO: Add error handling
            try {
                if (method === 'POST'){
                    await backendApi.createSet(this.set);
                    return;
                }
                
                await backendApi.updateSet(this.set._id, this.set);
            }
            catch(error) {
                errorStore.setMessage("There was a problem saving your set. Please try again.");
            }
        }
      },
});