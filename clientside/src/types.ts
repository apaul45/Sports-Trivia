interface Question {
    question: string
    answer: string
    difficulty: string
    username: string
    player: string
    tags: Array<string>
  }

  interface TrackedQuestion extends Question {
    correct?: boolean;
    inputtedAnswer?: string
  }
  
  interface Set {
    _id?: string,
    title: string
    username: string
    questions: Array<Question>
    rating: number
  }

  interface TrackedSet extends Set {
    questions: Array<TrackedQuestion>;
  }
  
  interface User {
    username: string
    password: string
    password_confirmed?: string
  }
  
  interface AggregateQuestions {
    doc: Array<Question>
    _id: string
  }
  
  export {
    Question, 
    Set, 
    TrackedSet,
    User, 
    AggregateQuestions
  }
  