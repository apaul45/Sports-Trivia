interface Question{
    question: string
    answer: string
    difficulty: string
    username: string
    player: string
    tags: Array<string>
  }
  
  interface Set{
    position: number
    username: string
    set: Array<Question>
    rating: number
  }
  
  interface User{
    username: string
    password: string
    passwordConfirmed?: string
  }
  
  interface AggregateQuestions{
    doc: Array<Question>
    _id: string
  }
  
  export {
    Question, Set, User, AggregateQuestions
  }
  