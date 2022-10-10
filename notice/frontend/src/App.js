import logo from './logo.svg';
import './App.css';
import React from "react";
import UserList from "./components/User";
import Footer from "./components/Footer";
import Menu from "./components/Menu";
import axios from "axios";


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
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
    }

    render() {
        return (
            <div>
                <Menu/>
                <UserList users={this.state.users}/>
                <Footer/>
            </div>
        );
    }
}

export default App;
