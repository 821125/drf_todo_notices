import React from "react";

const TodoItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.create}
            </td>
            <td>
                {todo.update}
            </td>
            <td>
                {todo.is_active}
            </td>
            <td>
                {todo.project}
            </td>
            <td>
                <button onClick={() => deleteTodo(todo.id)} type='button'>DELETE</button>
            </td>
        </tr>
    )
}

const TodoList = ({todos, deleteTodo}) => {
    return (
        <div className="outer">

            <div className="inner">
                <table className="Table">
                    <th>
                        Description
                    </th>
                    <th>
                        Create_at
                    </th>
                    <th>
                        Update_at
                    </th>
                    <th>
                        is_active
                    </th>
                    <th>
                        Project name
                    </th>
                    <tbody>
                        {todos.map((todo, idx) => <TodoItem todo={todo} key={todo.id} deleteTodo={deleteTodo}/>)}
                    </tbody>
                </table>
            </div>

        </div>
    )
}


export default TodoList