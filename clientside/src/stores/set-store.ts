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
    _id: '',
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
        updateSetBeingAdded(set: Set){
            this.setBeingAdded = set;
        },
        updateSetBeingViewed(set: Set){
            this.setBeingViewed = set;
        },
        addToSet(questions: Array<Question>){
            this.setBeingAdded.questions.push(...questions);
        },
        deleteFromSet(questions: Array<Question>){
            this.setBeingAdded.questions = this.setBeingAdded.questions.filter((question: Question) => questions.indexOf(question) == -1);
        },
        updateSetField(value: never, field: keyof Set){
            this.setBeingAdded[field] = value;
        },
        async saveToDb(method: string){
            if (method === 'POST'){
                const response = await backendApi.getNumberOfSets();
                delete this.setBeingAdded._id;
                await backendApi.createSet(this.setBeingAdded);
            }
            else{
                let id = this.setBeingAdded._id;
                delete this.setBeingAdded._id;
                await backendApi.updateSet(id, this.setBeingAdded);
            }
        }
      },
});