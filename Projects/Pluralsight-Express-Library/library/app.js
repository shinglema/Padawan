const express = require('express');
const chalk =require('chalk');
const path= require('path');


const app=express();
const port=process.env.PORT || 3000;



app.use(express.static(path.join(__dirname,'/public/')));


/* app.get('/', function(request, response){
    response.send('Hello from My Library App');


}) */


app.set('views', './src/views');
app.set('view engine','pug');

app.get('/', (request,response)=>{


    response.sendFile(path.join(__dirname,'views','index.html'));
    console.log('This is the root page');
})


app.get('/about', (request,response)=>{


    response.sendFile(path.join(__dirname,'views','index2.html'));
    console.log('This is the about page');
})


app.get('/contact', (request, response)=> {

    response.sendFile(path.join(__dirname,'views','index3.html'));
    console.log('This is the contact page');


})


/* app.get('/', (request,response) => {


    response.render('index');
})
 */

app.listen(port, ()=>{

    console.log('Listening on Port: ' + chalk.green(port));
});
