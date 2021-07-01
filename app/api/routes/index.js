var express = require('express');
var router = express.Router();
var gdb = require('../utils/graphdb');

/* GET home page. */
router.get('/filmes', async function(req, res) {
  var myquery = `SELECT DISTINCT ?id ?titulo ?ano ?classificacao WHERE {
    ?id a :Filme ;
        :titulo ?titulo ;
        :ano ?ano ;
        :classificacao ?classificacao ;
        FILTER (xsd:int(?classificacao) ).
  }
  order by ?ano
  `
  var result = await gdb.execQuery(myquery);

  var dados = result.results.bindings.map(b =>{

    return {
      id: b.id.value.split('#')[1],
      titulo: b.titulo.value,
      ano: b.ano.value,
      classificacao: b.classificacao.value,
    }
  })
  res.jsonp(dados)
});

router.get('/atores', async function(req, res) {
  var myquery = `SELECT distinct ?a ?nome WHERE {
    ?s a :Filme .
    ?s :temAtor ?a .
    ?a :nome ?nome
  }
  order by ?nome
  `
  
  var result = await gdb.execQuery(myquery);

  var dados = result.results.bindings.map(b =>{
    return {
      id: b.a.value.split('#')[1],
      nome: b.nome.value
    }
  })
  res.jsonp(dados)
});


router.get('/atores/ator/:id', async function(req, res) {
  var myquery = `SELECT ?ator ?atorNome WHERE {
    ?id a :Filme ;
      :temAtor ?ator .
    ?ator :nome ?atorNome .
    FILTER (?ator = :${req.params.id} ).
  }
  limit 1
  `

  var result = await gdb.execQuery(myquery);

  var dados = result.results.bindings.map(b =>{
    return {
      id: b.ator.value.split('#')[1],
      nome: b.atorNome.value
    }
  })

  res.jsonp(dados)
});

// Atores que participaram no filme
router.get('/atores/filme/:id', async function(req, res) {
  var myquery = `SELECT ?ator ?atorNome WHERE {
    ?id a :Filme ;
      :temAtor ?ator .
    OPTIONAL{?ator :nome ?atorNome .}
    FILTER (?id = :${req.params.id} ).
  }
  order by ?atorNome
  `

  var result = await gdb.execQuery(myquery);

  var dados = result.results.bindings.map(b =>{

    var nome = ''
    if(b.atorNome) nome = b.atorNome.value

    return {
      id: b.ator.value.split('#')[1],
      nome: nome
    }
  })

  res.jsonp(dados)
});


// Filmes em que participou
router.get('/filmes/ator/:id', async function(req, res) {
  var myquery = `SELECT ?id ?titulo WHERE {
    ?id a :Filme ;
      :temAtor :${req.params.id} ;
      :titulo ?titulo .
  }
  `

  var result = await gdb.execQuery(myquery);

  var dados = result.results.bindings.map(b =>{
    return {
      id: b.id.value.split('#')[1],
      titulo: b.titulo.value
    }
  })

  res.jsonp(dados)
});


router.get('/generos', async function(req, res) {
  var myquery = `SELECT distinct ?g WHERE {
    ?s a :Filme .
    ?s :temGenero ?g .
  }
  order by ?g
  `
  
  var result = await gdb.execQuery(myquery);

  var dados = result.results.bindings.map(b =>{
    return {
      genero: b.g.value.split('#')[1]
    }
  })
  res.jsonp(dados)
});


router.get('/filmes/filme/:id', async function(req, res) {
  var myquery = `SELECT ?id ?titulo ?ano ?pais ?duracao ?c_criticos ?c_utilizadores ?descricao ?n_votos ?classificacao ?linguagem ?diretor ?realizador ?escritor ?produtor ?genero WHERE {
    ?id a :Filme ;
        :titulo ?titulo ;
        :ano ?ano ;
        :pais ?pais ;
        :duracao ?duracao ;
        :criticas_criticos ?c_criticos ;
        :criticas_utilizadores ?c_utilizadores ;
        :descricao ?descricao ;
        :numero_votos ?n_votos ;
        :classificacao ?classificacao ;
        :linguagem ?linguagem ;
        :temDiretor ?diretor ;
        :temGenero ?g .
    ?g :nome ?genero .
        OPTIONAL{:id :temRealizador ?realizador .}
        OPTIONAL{:id :temEscritor ?escritor .}
        OPTIONAL{:id :temProdutor ?produtor .}
    FILTER (?id = :${req.params.id} ).
  }
  limit 1
  `
  //:id "${req.params.id}" ;
  var result = await gdb.execQuery(myquery);
  dados = result.results.bindings.map(b =>{

    var realizador = ''
    if(b.realizador) realizador = b.realizador.value.split('#')[1]
    var escritor = ''
    if(b.escritor) escritor = b.escritor.value.split('#')[1]
    var produtor = ''
    if(b.produtor) produtor = b.produtor.value.split('#')[1]

    return {
      id: b.id.value.split('#')[1],
      titulo: b.titulo.value,
      ano: b.ano.value,
      pais: b.pais.value,
      duracao: b.duracao.value,
      c_criticos: b.c_criticos.value,
      c_utilizadores: b.c_utilizadores.value,
      descricao: b.descricao.value,
      n_votos: b.n_votos.value,
      classificacao: b.classificacao.value,
      linguagem: b.linguagem.value,
      diretor: b.diretor.value.split('#')[1],
      realizador: realizador,
      escritor: escritor,
      produtor: produtor,
      genero: b.genero.value
    }
  })
  res.jsonp(dados)
});


module.exports = router;
