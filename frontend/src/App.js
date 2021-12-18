import React, {useState, useEffect} from "react";
import {BrowserRouter, Routes, Route} from "react-router-dom";

import HistoryThief from "./components/utils/HistoryThief";
import {useAuth} from "./utils/authContext";

import {NotificationContainer} from "react-notifications";
// import Header from "./components/Header";
// import Home from "./pages/Home";
import Login from "./pages/LoginPage";
import Header from "./components/Header";
import Home from "./pages/Home";
import Clients from "./pages/Clients";
import Products from "./pages/Products";

import '../src/media/style.scss'
import Documents from "./pages/Documents";


function App() {
    // let auth = useAuth();

    // useEffect(() => {}, [auth.user])

    return <BrowserRouter>
        <HistoryThief />
        <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/*"
                   element={<>
                       <Header />
                       <div className='mainContentLayout'>
                           <Routes>
                               <Route path='/products' element={<Products />}/>
                               <Route path='/documents' element={<Documents />}/>
                               <Route path='/clients' element={<Clients />}/>
                               <Route path='/' element={<Home />}/>
                           </Routes>
                       </div>
                       <NotificationContainer/>
                   </>
                   }
            />
        </Routes>
    </BrowserRouter>
}

export default App;
