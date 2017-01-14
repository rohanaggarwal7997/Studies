var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  //router.get gets the url called and res.render is calling the view
  res.render('index', { title: 'Login Server'});
});
router.get('/test/:id',function(req,res,next){

  res.render('test',{output:req.params.id})

  //id indicates a variable  and it is used under the same name in params.id
 //remember access the view named test and making object as variable
})
router.get('/wrong',function(req,res,next){

    res.render('wrong')

})
router.post('/test/submit',function(req,res,next){

  var id=req.body.id;
  var pass=req.body.pass;
  if(id=='rohan.aggarwal' && pass=='brother')
  {res.redirect('/test/'+id);}
  else
  {
    res.redirect('/wrong');

  }


})

module.exports = router;
