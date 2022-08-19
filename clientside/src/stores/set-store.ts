import { defineStore } from "pinia";
import { Question, Set } from "src/types";
import backendApi from "src/boot/axios";
import { useUserStore } from "./user-store";

interface State{
    setBeingAdded: Set,
    setBeingViewed: Set
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
        setBeingViewed: defaultSet
      }),
      getters: {},
      actions: {
        setDefault(){
            this.setBeingAdded.questions = [];
            this.setBeingAdded.title = '';
            this.setBeingAdded.rating = 0;
        },
        addToSet(questions: Array<Question>){
            this.setBeingAdded.questions.push(...questions);
        },
        deleteFromSet(questions: Array<Question>){
            this.setBeingAdded.questions = this.setBeingAdded.questions.filter((question: Question) => questions.indexOf(question) == -1);
        },
        updateSet(value: never, field: keyof Set){
            this.setBeingAdded[field] = value;
        },
        updateSetBeingViewed(set: Set){
            this.setBeingViewed = set;
        },
        async saveToDb(){
            const response = await backendApi.getNumberOfSets();
            this.setBeingAdded.position = response.data;
            await backendApi.createSet(this.setBeingAdded);
        }
      },
});