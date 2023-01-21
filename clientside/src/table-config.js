export const columns = [
    {
        name: 'username',
        required: true,
        label: 'User',
        align: 'left',
        field: (row) => row.username,
        sortable: true
    },
    {
        name: 'question',
        required: true,
        label: 'Question',
        align: 'left',
        field: (row) => row.question
    },
    {
        name: 'answer',
        required: true,
        label: 'Answer',
        align: 'left',
        field: (row) => <details> 
                            <summary>
                                {row.answer} 
                            </summary>
                        </details>
    },
    {
        name: 'difficulty',
        required: true,
        label: 'Difficulty',
        align: 'left',
        field: (row) => row.difficulty[0].toUpperCase() + row.difficulty.substring(1),
        sortable: true,
        sort: (a,b) => sortByDifficulty(a,b)
    },
    {
        name: 'tags',
        required: true, 
        label: "Tags",
        align:'center',
        field: (row) => createTagCards(row.tags),
        // sortable: true,
        // sort: (a, b) => a.childElementCount - b.childElementCount
    }
]

const difficulty = ["Easy", "Medium", "Hard"];

const sortByDifficulty = (a, b) => {
    const aIndex = difficulty.findIndex((d) => d === a);
    const bIndex = difficulty.findIndex((d) => d === b);

    return aIndex - bIndex;
}

export const createTagCards = (tags) => {
    const style = "display: inline; \
                   padding: 7px; \
                   color: black; \
                   border-radius: 25px; \
                   background-color: #7CCB96; \
                   text-align: center;";

    return <div style="overflow: auto; line-height: 3.5;"> 
                {
                    tags.map(tag =>
                    <>
                        &nbsp;
                        <div style={style}>{tag}</div>
                        &nbsp; 
                    </>
                    )
                }
           </div>
}