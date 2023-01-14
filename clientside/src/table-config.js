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
        field: (row) => row.difficulty,
        sortable: true
    },
    {
        name: 'tags',
        required: true, 
        label: "Tags",
        align:'center',
        field: (row) => createTagCards(row.tags)
    }
]

export const createTagCards = (tags) => {
    const style = "display: inline; \
                   padding: 7px; \
                   text-color: white; \
                   border-radius: 25px; \
                   background-color: #7CCB96; \
                   text-align: center; \
                   outline-style: solid;";

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