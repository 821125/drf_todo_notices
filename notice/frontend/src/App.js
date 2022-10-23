import './App.css';
import React from "react";
import UserList from "./components/User";
import Footer from "./components/Footer";
import Menu from "./components/Menu";
import axios from "axios";
import {Route, Link, Switch, BrowserRouter} from 'react-router-dom'


const NotFound404 = ({location}) => {
    return (
        <div>
            404 Error Not found: {location.pathname}
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {

        // const users = [
        //     {
        //         'username': 'Alex',
        //         'email': 'alex@mail.ru'
        //     }
        // ]
        //
        // this.setState({
        //     'users': users
        // })

        axios.get('http://127.0.0.1:8000/api/notices/').then(response => {
            this.setState({
                'users': response.data
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <Menu/>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                        <Route exact path='/project' component={() => <ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todo' component={() => <TodoList todos={this.state.todos}/>}/>
                        <Route component={NotFound404}/>
                    </Switch>
                    <Footer/>
                </BrowserRouter>

            </div>
        );
    }
}

export default App;
