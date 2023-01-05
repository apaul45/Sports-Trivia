import { defineStore } from "pinia";
import { Question, Set } from "src/types";
import backendApi from "src/boot/axios";

interface State {
    setBeingAdded: Set,
    setBeingViewed: Set
}

const defaultSet: Set = {
    title: '', 
    username: 'apaul45', 
    questions: [], 
    rating: 0
};

export const useSetStore = defineStore<string, State>('sets', {  
     state: () => ({
        setBeingAdded: defaultSet,
        setBeingViewed: defaultSet
      }),
      getters: {},
      actions: {
        setDefault() {
            this.setBeingAdded.questions = [];
            this.setBeingAdded.title = '';
            this.setBeingAdded.rating = 0;
        },
        updateSetBeingAdded(set: Set) {
            this.setBeingAdded = set;
        },
        updateSetBeingViewed(set: Set) {
            this.setBeingViewed = set;
        },
        addToSet(questions: Array<Question>) {
            this.setBeingAdded.questions.push(...questions);
        },
        deleteFromSet(questions: Array<Question>) {
            this.setBeingAdded.questions = this.setBeingAdded.questions.filter((question) => questions.indexOf(question) == -1);
        },
        updateSetField(value: never, field: keyof Set) {
            this.setBeingAdded[field] = value;
        },
        async saveToDb(method: string) {
            //TODO: Add error handling
            if (method === 'POST'){
                await backendApi.createSet(this.setBeingAdded);
                return;
            }
            
            await backendApi.updateSet(this.setBeingAdded._id, this.setBeingAdded);
        }
      },
});