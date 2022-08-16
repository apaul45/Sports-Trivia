import { defineStore } from "pinia";
import { Question, Set } from "src/types";
import backendApi from "src/boot/axios";

interface State{
    setBeingAdded: Set
}

const defaultSet: Set = {
    title: '', 
    position: 0, 
    username: 'apaul45', 
    questions: [], 
    rating: 0
};

export const useSetStore = defineStore<string, State>('sets', {  
     state: () => ({
        setBeingAdded: defaultSet,
      }),
      getters: {},
      actions: {
        addToSet(questions: Array<Question>){
            this.setBeingAdded.questions.push(...questions);
            this.setBeingAdded = defaultSet;
        },
        deleteFromSet(questions: Array<Question>){
            this.setBeingAdded.questions = this.setBeingAdded.questions.filter((question: Question) => questions.indexOf(question) == -1);
        },
        updateSet(value: never, field: keyof Set){
            this.setBeingAdded[field] = value;
        },
        async saveToDb(){
            await backendApi.createSet(this.setBeingAdded);
            this.setBeingAdded = defaultSet;
            console.log(this.setBeingAdded);
        }
      },
});