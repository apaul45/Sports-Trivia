import { defineStore } from "pinia";
import { Question, Set } from "src/types";
import backendApi from "src/boot/axios";

interface State{
    setBeingAdded: Set
}

export const useSetStore = defineStore<string, State>('sets', {  
     state: () => ({
        setBeingAdded: {
            title: '', 
            position: 0, 
            username: 'apaul21', 
            questions: [], 
            rating: 0
        },
      }),
      getters: {},
      actions: {
        addToSet(questions: Array<Question>){
            this.setBeingAdded.questions.push(...questions);
        },
        async saveToDb(){
            await backendApi.createSet(this.setBeingAdded);
        }
      },
});