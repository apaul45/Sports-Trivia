import { reactive } from 'vue'

export const errorStore = reactive({
  message: "",
  setMessage(message: string) {
    this.message = message;
  }
})