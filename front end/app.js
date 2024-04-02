const express = require('express');
const path = require('path');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'login.html'));
});

app.post('/login', (req, res) => {
    res.send('Login successful');
});

app.get('/user/home', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'user_home.html'));
});

app.get('/user/location', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'user_location.html'));
});

app.post('/user/location', (req, res) => {
    const garages = ['Garage 1', 'Garage 2', 'Garage 3'];
    res.render('garage_list', { garages });
});

app.get('/garage/availability', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'garage_availability.html'));
});

app.post('/garage/availability', (req, res) => {
    res.send('Availability updated');
});

app.get('/manager/dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'garage_manager_dashboard.html'));
});

app.get('/admin/dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'views', 'admin_dashboard.html'));
});

app.listen(PORT, () => {
    console.log(Server is running on port ${PORT});
});