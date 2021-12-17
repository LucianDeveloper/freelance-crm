import '../media/login.scss'
import Login from '../components/login/Login'
import Footer from "../components/footer";

const LoginPage = () => {
    return (
        <div className="login-page">
            <Login />
            <Footer/>
        </div>
    )
};
export default LoginPage;