var express = require('express');
var router = express.Router();
var mongo=require('mongodb');
var assert=require('assert');
var url='mongodb://localhost:27017/test';

/* GET home page. */
router.get('/', function(req, res, next) {
 res.render('index', { title: 'Login Server'});
});
router.get('/userregister', function(req, res, next) {
    res.render('userregister', { title: 'User Register'});
});
router.get('/test/:id',function(req,res,next){

  res.render('test',{output:req.params.id})

 })
router.get('/wrong',function(req,res,next){

    res.render('wrong')

})
router.post('/test/submit',function(req,res,next){

  var id=req.body.id;
  var pass=req.body.pass;
  mongo.connect(url,function (err,db) {
    assert.equal(null,err);
    var cursor=db.collection('user-data').find();
    cursor.forEach(function (doc,err) {
      assert.equal(null,err);
        if(id==doc.username && pass==doc.pass)
        {res.redirect('/test/'+id);}


    });
          res.redirect('/wrong');
  });
  /*

  */
})

router.post('/register',function(req,res,next){

   var item={
     username:req.body.id,
       pass:req.body.pass
   };

   mongo.connect(url,function(err,db){
     assert.equal(null,err);
     db.collection('user-data').insertOne(item,function(err,result){
       assert.equal(null,err);
       db.close();
     })
   })
   res.redirect('/');
})


module.exports = router;
